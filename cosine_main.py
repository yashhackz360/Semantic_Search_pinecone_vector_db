import os
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer, CrossEncoder
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
from sklearn.feature_extraction.text import TfidfVectorizer
from query_handler import get_query
from query_preprocessing import parse_user_query

# --- CONFIGS ---
INDEX_NAME = "laptop-hybrid-search-v2"
EMBEDDING_MODEL_NAME = "all-mpnet-base-v2"
RERANKER_MODEL_NAME = "cross-encoder/ms-marco-MiniLM-L-6-v2"
ALPHA = 0.5  # Weight for semantic score in final ranking

# --- LOADING ENVIRONMENT ---
load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENV")

# --- INITIALIZING MODELS ---
embedding_model = SentenceTransformer(EMBEDDING_MODEL_NAME)
reranker = CrossEncoder(RERANKER_MODEL_NAME)

# --- HELPER FUNCTIONS ---

def generate_sentence(row):
    ssd = int(row['SSD']) if row['SSD'] != "N/A" else 0
    hdd = int(row['HDD']) if row['HDD'] != "N/A" else 0
    storage_parts = []
    if ssd > 0:
        storage_parts.append(f"{ssd} GB SSD storage")
    if hdd > 0:
        storage_parts.append(f"{hdd} GB HDD storage")
    storage_str = " and ".join(storage_parts) if storage_parts else "no storage"
    return (
        f"The {row['Company']} {row['TypeName']} is a laptop equipped with {row['Ram']} GB of RAM and a {row['Cpu_brand']} processor. "
        f"It offers {storage_str} for your files and applications. "
        f"For graphics, it uses a {row['Gpu_brand']} GPU. "
        f"The laptop runs on {row['Os']} and is priced at ₹{row['Price']}."
    )

def generate_query_sentence(parsed):
    ssd = int(parsed['SSD']) if parsed['SSD'] != "N/A" else 0
    hdd = int(parsed['HDD']) if parsed['HDD'] != "N/A" else 0
    storage_parts = []
    if ssd > 0:
        storage_parts.append(f"{ssd} GB SSD storage")
    if hdd > 0:
        storage_parts.append(f"{hdd} GB HDD storage")
    storage_str = " and ".join(storage_parts) if storage_parts else "no storage"
    return (
        f"The {parsed['Company']} {parsed['TypeName']} is a laptop equipped with {parsed['Ram']} GB of RAM and a {parsed['Cpu_brand']} processor. "
        f"It offers {storage_str} for your files and applications. "
        f"For graphics, it uses a {parsed['Gpu_brand']} GPU. "
        f"The laptop runs on {parsed['Os']} and is priced at ₹{parsed['Price']}."
    )

# --- SETTING UP PINECONE INDEX (Efficient) ---
def setup_index():
    pc = Pinecone(api_key=PINECONE_API_KEY)
    # Create index only if it doesn't exist
    if INDEX_NAME not in pc.list_indexes().names():
        print("Creating new Pinecone index...")
        pc.create_index(
            name=INDEX_NAME,
            dimension=768,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region=PINECONE_ENV)
        )
    index = pc.Index(INDEX_NAME)
    stats = index.describe_index_stats()
    # Upsert only if index is empty
    if stats['total_vector_count'] == 0:
        print("Index is empty. Upserting data...")
        df = pd.read_csv("data/laptop_data_cleaned.csv")
        df.fillna("N/A", inplace=True)

        sentences = df.apply(generate_sentence, axis=1).tolist()
        embeddings = embedding_model.encode(sentences, batch_size=32, show_progress_bar=True)
        items = [
            {
                "id": f"id-{i}",
                "values": emb.tolist(),
                "metadata": {
                    "text": sent,
                    "brand": str(row["Company"]),
                    "ram": str(row["Ram"]),
                    "cpu": str(row["Cpu_brand"]),
                    "ssd": str(row["SSD"]),
                    "hdd": str(row["HDD"]),
                    "os": str(row["Os"]),
                    "gpu": str(row["Gpu_brand"]),
                    "price": str(row["Price"])
                }
            }
            for i, (emb, sent, (_, row)) in enumerate(zip(embeddings, sentences, df.iterrows()))
        ]
        batch_size = 200
        for i in range(0, len(items), batch_size):
            index.upsert(items[i:i+batch_size])
        print(f"Inserted {len(items)} vectors into Pinecone.")
    else:
        print("Index already populated. Skipping upsert.")
        # You still need the sentences for TF-IDF; load from CSV
        df = pd.read_csv("data/laptop_data_cleaned.csv")
        df.fillna("N/A", inplace=True)
        sentences = df.apply(generate_sentence, axis=1).tolist()
    return index, sentences

# --- HYBRID SEARCH ---
def hybrid_search(query, index, all_sentences, top_k=30, rerank_top=5, alpha=ALPHA):
    query_vec = embedding_model.encode([query])[0].tolist()
    semantic_results = index.query(vector=query_vec, top_k=top_k, include_metadata=True)
    semantic_candidates = {m['id']: m for m in semantic_results.get('matches', [])}

    tfidf_vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf_vectorizer.fit_transform(all_sentences)
    query_tfidf = tfidf_vectorizer.transform([query])
    keyword_scores = (tfidf_matrix * query_tfidf.T).toarray().flatten()
    top_keyword_indices = keyword_scores.argsort()[::-1][:top_k]
    keyword_candidates = {
        f"id-{i}": {
            "id": f"id-{i}",
            "metadata": {"text": all_sentences[i]},
            "keyword_score": float(keyword_scores[i])
        }
        for i in top_keyword_indices
    }

    all_candidates = semantic_candidates.copy()
    for k, v in keyword_candidates.items():
        if k not in all_candidates:
            all_candidates[k] = v
        else:
            all_candidates[k]["keyword_score"] = v["keyword_score"]

    pairs = [(query, c["metadata"]["text"]) for c in all_candidates.values()]
    rerank_scores = reranker.predict(pairs)
    for idx, c in enumerate(all_candidates.values()):
        c["semantic_score"] = float(rerank_scores[idx])
        c["keyword_score"] = c.get("keyword_score", 0.0)
        c["final_score"] = alpha * c["semantic_score"] + (1 - alpha) * c["keyword_score"]

    reranked_results = sorted(all_candidates.values(), key=lambda x: x["final_score"], reverse=True)[:rerank_top]
    return reranked_results

# --- MAIN ---
if __name__ == "__main__":
    index, all_sentences = setup_index()
    query = get_query()
    parsed = parse_user_query(query)
    query_sentence = generate_query_sentence(parsed)
    print("\nStructured Query Sentence for Embedding:", query_sentence)
    results = hybrid_search(query_sentence, index, all_sentences)

    if not results or results[0]['final_score'] < -5.0:
        print("\nNo relevant results found for your query. Please try a different search.")
    else:
        print(f"\nTop {len(results)} Hybrid Reranked Results:")
        for i, match in enumerate(results):
            print(f"\nResult {i+1}")
            print(f"Final Score: {match['final_score']:.4f}")
            print(f"Text: {match['metadata']['text']}")

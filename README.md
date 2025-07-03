# 🔍 Semantic Search with Pinecone Vector DB

This project demonstrates how to build a **semantic search application** using **Pinecone**, a fully managed vector database. It provides end-to-end code for generating embeddings, storing them, and performing search based on meaning using vector similarity (cosine similarity or dot product).

---

## 🔖 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Setup](#-setup)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [How It Works](#️-how-it-works)
- [Query Processing Explained](#-query-processing-explained)
- [Main Code Logic](#-main-code-logic)
- [Customization](#-customization)
- [References](#-references)

---

## 🧠 Overview

Semantic search uses **vector embeddings** to represent both queries and documents, enabling searches based on **meaning** rather than exact keywords.  
This repository demonstrates semantic search on a sample dataset (`laptop_data_cleaned.csv`), but the approach can be adapted to any textual or tabular data.

---

## ✅ Features

- ✨ Embedding generation using **Sentence Transformers** or **OpenAI embeddings**
- 📦 Scalable vector storage using **Pinecone**
- 📐 Semantic search using **cosine similarity** and **dot product**
- 🧹 Query preprocessing and handling
- 📁 Sample dataset for testing and demonstration

---

## 🗂️ Project Structure

| File/Folder              | Description                                |
|--------------------------|--------------------------------------------|
| `cosine_main.py`         | Search using cosine similarity             |
| `dotproduct_main.py`     | Search using dot product similarity        |
| `query_handler.py`       | Handles and processes user queries         |
| `query_preprocessing.py` | Preprocessing logic for queries            |
| `laptop_data_cleaned.csv`| Sample dataset (laptop product data)       |
| `requirements.txt`       | Python dependencies                        |
| `README.md`              | Project documentation                      |

---

## ⚙️ Setup

### 🔧 Prerequisites

- Python 3.8+
- Pinecone account (Free API key)
- (Recommended) Virtual environment

### 📥 Installation

```bash
git clone https://github.com/yashhackz360/Semantic_Search_pinecone_vector_db.git
cd Semantic_Search_pinecone_vector_db
pip install -r requirements.txt
```

---

## 🔐 Configuration

Create a `.env` file in the project root with the following values:

```env
PINECONE_API_KEY=your-pinecone-api-key
PINECONE_ENV=your-pinecone-environment  # e.g., us-west1-gcp
PINECONE_INDEX=your-index-name
```

You can find these in your [Pinecone Dashboard](https://app.pinecone.io).

---

## 🚀 Usage

### 📂 Step 1: Prepare Data

Ensure `laptop_data_cleaned.csv` is present.  
The script will embed the data and **upsert** it to Pinecone.

### 🔍 Step 2: Run Semantic Search

**Cosine Similarity:**

```bash
python cosine_main.py
```

**Dot Product Similarity:**

```bash
python dotproduct_main.py
```

Enter your search query when prompted.

---

## ⚙️ How It Works

1. **Embedding**  
   Each row in the CSV is transformed into a **descriptive sentence** and encoded as a vector.

2. **Upsert to Pinecone**  
   The encoded vectors are stored in a Pinecone index.

3. **Query Handling**  
   A user query is parsed, converted to a semantic sentence, embedded, and used for querying.

4. **Hybrid Search + Rerank**  
   Combines **semantic** similarity (vector) and **keyword-based** similarity (TF-IDF), reranks using a **CrossEncoder**, and returns top results.

---

## 🧪 Query Processing Explained

### 📁 `query_handler.py`

This module prompts the user:

```python
def get_query():
    print("\n=== Laptop Semantic Search ===")
    return input("Enter your search query: ")
```

### 📁 `query_preprocessing.py`

Uses **regex** to extract structured data from natural language input:

```python
def parse_user_query(query):
    ...
    return {
        'Company': ...,
        'TypeName': "N/A",
        'Ram': ...,
        'Cpu_brand': ...,
        'SSD': ...,
        'HDD': ...,
        'Gpu_brand': ...,
        'Os': ...,
        'Price': ...
    }
```

#### 🧠 Example

**Input:**
```
Looking for a Dell laptop with 16GB RAM, 512GB SSD, Intel CPU, under ₹60000
```

**Parsed Output:**
```json
{
  "Company": "Dell",
  "Ram": "16",
  "Cpu_brand": "Intel",
  "SSD": "512",
  "HDD": "0",
  "Gpu_brand": "N/A",
  "Os": "N/A",
  "Price": "60000"
}
```

Then converted to:
```
"The Dell N/A is a laptop equipped with 16 GB of RAM and an Intel processor. It offers 512 GB SSD storage..."
```

---

## 💻 Main Code Logic

### 🔁 `cosine_main.py` / `dotproduct_main.py`

Both scripts follow the same logic, with a different similarity metric (`cosine` vs `dotproduct`).

### 🔧 Key Steps:

1. **Environment Setup**
   - Load `.env`
   - Load SentenceTransformer and CrossEncoder models

2. **Index Initialization**
   - Create Pinecone index if not exists
   - Load CSV data and generate descriptive sentences
   - Encode using SentenceTransformer
   - Upsert vectors into Pinecone

3. **Query to Vector Pipeline**
   - Accept user input
   - Parse and structure using regex
   - Generate a semantic query sentence
   - Encode query as a vector

4. **Hybrid Search Process**
   - Query Pinecone (semantic match)
   - TF-IDF match on all sentences
   - Combine results
   - Rerank using CrossEncoder
   - Final score:  
     \[
     \text{final\_score} = \alpha \cdot \text{semantic\_score} + (1 - \alpha) \cdot \text{keyword\_score}
     \]

5. **Result Display**
   - Top matches with metadata and score shown to user

---

## 🛠️ Customization

- 🔄 **Change Dataset**: Replace `laptop_data_cleaned.csv` with your own data
- 🧠 **Switch Embedding Model**: Update SentenceTransformer
- 🧮 **Change Similarity Metric**: Use cosine, dot product, or custom

---

## 📚 References

- [Pinecone Docs – Semantic Search](https://docs.pinecone.io/docs/semantic-search)
- [Pinecone Learn – Tutorials](https://www.pinecone.io/learn/)
- [Sentence Transformers](https://www.sbert.net/)
- [Hugging Face CrossEncoder](https://huggingface.co/cross-encoder)

---

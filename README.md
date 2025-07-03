<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Semantic Search with Pinecone</title>
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background-color: #f8f9fa;
      margin: 0;
      padding: 2rem;
      color: #333;
      line-height: 1.6;
    }
    h1, h2, h3 {
      color: #0057b7;
    }
    code, pre {
      background-color: #e9ecef;
      padding: 0.3rem 0.5rem;
      border-radius: 4px;
      font-family: monospace;
    }
    .container {
      max-width: 900px;
      margin: auto;
      background-color: #fff;
      padding: 2rem;
      border-radius: 10px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    ul, ol {
      padding-left: 1.5rem;
    }
    .project-structure pre {
      background-color: #f1f1f1;
      padding: 1rem;
      border-radius: 6px;
      overflow-x: auto;
    }
    a {
      color: #0057b7;
      text-decoration: none;
    }
    a:hover {
      text-decoration: underline;
    }
    .badge {
      background: #0057b7;
      color: white;
      padding: 0.25em 0.6em;
      font-size: 0.75em;
      border-radius: 0.4em;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Semantic Search 🔍🧠</h1>
    <p><strong>Semantic_Search_pinecone_vector_db</strong> is a Python-based semantic search system that leverages vector embeddings and the Pinecone vector database to enable search by meaning rather than keyword matching. It uses cosine similarity or dot product to return highly relevant results.</p>

    <h2>📌 Features</h2>
    <ul>
      <li>🔹 <strong>Vector Embeddings</strong> – Converts text into dense vector representations using language models.</li>
      <li>🔹 <strong>Pinecone Integration</strong> – Stores embeddings in a scalable, real-time vector database.</li>
      <li>🔹 <strong>Semantic Matching</strong> – Retrieves results based on meaning, not keywords.</li>
      <li>🔹 <strong>Multiple Similarity Metrics</strong> – Supports both cosine similarity and dot product.</li>
      <li>🔹 <strong>Modular Query Handling</strong> – Clean separation of preprocessing and search logic.</li>
    </ul>

    <h2>🛠 Tech Stack</h2>
    <ul>
      <li><strong>Language:</strong> Python</li>
      <li><strong>Libraries/Services:</strong> Sentence Transformers / OpenAI Embeddings, Pinecone, dotenv</li>
      <li><strong>Concepts Used:</strong> Vector Embedding, Semantic Search, Dot Product & Cosine Similarity</li>
    </ul>

    <h2>📂 Project Structure</h2>
    <div class="project-structure">
      <pre>
📦 Semantic_Search_pinecone_vector_db
 ├── 📜 cosine_main.py          # Search using cosine similarity
 ├── 📜 dotproduct_main.py      # Search using dot product similarity
 ├── 📜 query_handler.py        # Handles user queries
 ├── 📜 query_preprocessing.py  # Preprocessing logic for queries
 ├── 📜 laptop_data_cleaned.csv # Sample dataset for demo
 ├── 📜 requirements.txt        # Python dependencies
 ├── 📜 README.md               # Project documentation
 ├── 📜 .env                    # Pinecone configuration (user-defined)
 ├── 📜 .gitignore              # Git ignored files
      </pre>
    </div>

    <h2>🚀 Getting Started</h2>
    <h3>🔧 Prerequisites</h3>
    <ul>
      <li>Python 3.8 or above</li>
      <li>Pinecone account & API key</li>
      <li>Virtual environment (recommended)</li>
    </ul>

    <h3>⚙️ Installation & Setup</h3>
    <pre><code>git clone https://github.com/yashhackz360/Semantic_Search_pinecone_vector_db.git
cd Semantic_Search_pinecone_vector_db
pip install -r requirements.txt</code></pre>

    <h3>🔐 Configuration</h3>
    <p>Create a <code>.env</code> file in the root directory with:</p>
    <pre><code>PINECONE_API_KEY=your-pinecone-api-key
PINECONE_ENV=your-environment  # e.g., us-west1-gcp
PINECONE_INDEX=your-index-name</code></pre>

    <h2>📈 Usage</h2>
    <h3>🗃️ Step 1: Prepare Dataset</h3>
    <p>Ensure <code>laptop_data_cleaned.csv</code> is in the project directory.</p>

    <h3>🔍 Step 2: Run Semantic Search</h3>
    <pre><code># Cosine Similarity
python cosine_main.py

# Dot Product Similarity
python dotproduct_main.py</code></pre>

    <h2>⚙️ How It Works</h2>
    <ol>
      <li><strong>Embedding:</strong> Converts input data and queries into vectors using a language model.</li>
      <li><strong>Upsert to Pinecone:</strong> Stores vectors in the Pinecone index.</li>
      <li><strong>Query Processing:</strong> Preprocesses and embeds user query.</li>
      <li><strong>Similarity Search:</strong> Compares vectors using cosine similarity or dot product to return results.</li>
    </ol>

    <h2>✏️ Customization</h2>
    <ul>
      <li><strong>Replace Dataset:</strong> Swap <code>laptop_data_cleaned.csv</code> with your own CSV.</li>
      <li><strong>Change Embedding Model:</strong> Modify embedding logic to use another model.</li>
      <li><strong>Alter Similarity Logic:</strong> Add more metrics like Euclidean distance.</li>
    </ul>

    <h2>📜 License</h2>
    <p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>

    <h2>🤝 Contributing</h2>
    <p>Contributions are welcome! Fork the repo, submit issues, or create pull requests.</p>

    <h2>📧 Contact</h2>
    <p>For questions or collaborations, connect via <a href="https://www.linkedin.com/in/yashwanth-sai-kasarabada-ba4265258/">LinkedIn</a>.</p>
  </div>
</body>
</html>

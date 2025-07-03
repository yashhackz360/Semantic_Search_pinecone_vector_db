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

| File/Folder            | Description                                |
|------------------------|--------------------------------------------|
| `cosine_main.py`       | Search using cosine similarity             |
| `dotproduct_main.py`   | Search using dot product similarity        |
| `query_handler.py`     | Handles and processes user queries         |
| `query_preprocessing.py` | Preprocessing logic for queries         |
| `laptop_data_cleaned.csv` | Sample dataset (laptop product data)   |
| `requirements.txt`     | Python dependencies                        |
| `README.md`            | Project documentation                      |

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
   Each record in the dataset is converted into a **vector** using a language model.

2. **Upsert to Pinecone**  
   These vectors are stored in a Pinecone **index**.

3. **Query Handling**  
   User queries are **preprocessed** and converted into a **query vector**.

4. **Semantic Search**  
   The query vector is compared with stored vectors using a **similarity metric**.  
   The most similar records are retrieved.

---

## 🛠️ Customization

- 🔄 **Change Dataset**: Replace `laptop_data_cleaned.csv` with your own CSV file.
- 🧠 **Switch Embedding Model**: Modify the embedding logic in the script.
- 🧮 **Adjust Similarity Metric**: Use **cosine**, **dot product**, or implement others like **Euclidean distance**.

---

## 📚 References

- [Pinecone Docs – Semantic Search](https://docs.pinecone.io/docs/semantic-search)
- [Pinecone Learn – Tutorials](https://www.pinecone.io/learn/)
- [Pinecone Example Projects](https://github.com/pinecone-io/examples)

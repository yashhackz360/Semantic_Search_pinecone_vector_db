# Semantic_Search_pinecone_vector_db
Semantic Search with Pinecone Vector Database
This project demonstrates how to build a semantic search application using the Pinecone vector database and Python. It provides end-to-end code for embedding, storing, and searching data by meaning, not just keywords, using vector similarity measures such as cosine similarity and dot product.

Table of Contents
Overview

Features

Project Structure

Setup

Configuration

Usage

How It Works

Customization

References

Overview
Semantic search leverages vector embeddings to represent both queries and documents, enabling search by meaning rather than exact keyword match. This repository uses Pinecone—a fully managed vector database—to store and search these embeddings at scale.

The included example focuses on semantic search over a sample dataset (laptop_data_cleaned.csv), but the approach can be adapted to any tabular or textual data.

Features
Vector embedding generation using a language model (e.g., sentence transformers or OpenAI embeddings).

Storage of embeddings in Pinecone for scalable, high-performance search.

Semantic search using cosine similarity and dot product.

Query preprocessing and handling.

Sample dataset for demonstration and testing.

Project Structure
File/Folder	Description
cosine_main.py	Main script for semantic search using cosine similarity
dotproduct_main.py	Main script for semantic search using dot product similarity
query_handler.py	Handles and processes user queries
query_preprocessing.py	Preprocesses queries for embedding
laptop_data_cleaned.csv	Sample dataset (e.g., laptop product data)
requirements.txt	Python dependencies
README.md	Project documentation (this file)
Setup
Prerequisites
Python 3.8+

Pinecone account (get a free API key at Pinecone)

(Recommended) Virtual environment

Installation
Clone the repository:

text
git clone https://github.com/yashhackz360/Semantic_Search_pinecone_vector_db.git
cd Semantic_Search_pinecone_vector_db
Install dependencies:

text
pip install -r requirements.txt
Set up Pinecone:

Sign up at Pinecone and create an API key.

Create a new index in your Pinecone dashboard.

Configuration
Create a .env file in the project root with the following variables:

text
PINECONE_API_KEY=your-pinecone-api-key
PINECONE_ENV=your-pinecone-environment
PINECONE_INDEX=your-index-name
PINECONE_API_KEY: Your Pinecone API key (required)

PINECONE_ENV: The environment (e.g., us-west1-gcp)

PINECONE_INDEX: The name of your Pinecone index

Tip: You can find these values in your Pinecone dashboard.

Usage
1. Prepare Data and Index
Ensure the dataset (laptop_data_cleaned.csv) is present.

The scripts will generate embeddings for each row and upsert them into Pinecone.

2. Run Semantic Search
Cosine Similarity Search:

text
python cosine_main.py
Dot Product Similarity Search:

text
python dotproduct_main.py
Follow the prompts to enter your search query.

How It Works
Data Embedding:
The dataset is embedded into vectors using a language model (e.g., Sentence Transformers or OpenAI embeddings).

Upsert to Pinecone:
The embeddings are stored in a Pinecone index for efficient vector similarity search.

Query Handling:
User queries are preprocessed and embedded using the same model.

Semantic Search:
The query vector is compared to stored vectors using cosine similarity or dot product. The most relevant records are returned, ranked by similarity score.

Customization
Change Dataset:
Replace laptop_data_cleaned.csv with your own CSV or data source.

Swap Embedding Model:
Update the embedding logic in the scripts to use your preferred language model.

Adjust Similarity Metric:
Use either cosine similarity or dot product, or implement additional metrics as needed.

References
Pinecone Docs: Semantic Search

Pinecone Learn: Semantic Search

Pinecone Example Projects

Build scalable, production-ready semantic search with Pinecone and Python.

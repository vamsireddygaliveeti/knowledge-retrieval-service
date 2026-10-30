# LangChain Knowledge Retrieval Service

A document search API built with Python, FastAPI, LangChain, and Pinecone. It uses semantic search to find relevant documents based on natural-language questions instead of exact keyword matches.

## Tech Stack

- Python
- FastAPI
- LangChain
- Pinecone
- Hugging Face Sentence Transformers
- Uvicorn

## How It Works

The application reads documents from a JSON file and generates embeddings using the `all-MiniLM-L6-v2` model. The embeddings are stored in Pinecone along with the document text and metadata.

When a question is submitted, the application generates an embedding for the question and searches Pinecone for similar vectors. The matching documents are returned through a FastAPI endpoint.

The Pinecone index uses 384 dimensions and cosine similarity.

## Getting Started

### Install Dependencies

```bash
python -m pip install fastapi uvicorn python-dotenv pinecone langchain-core langchain-pinecone langchain-huggingface sentence-transformers
```

### Configure Pinecone

Create a dense-vector index with 384 dimensions and cosine similarity, using your own embeddings.

Add a `.env` file with your Pinecone credentials:

```env
PINECONE_API_KEY=your_api_key
PINECONE_INDEX_NAME=company-vectors
```

### Upload Documents

```bash
python upload_documents.py
```

### Search Documents

```bash
python search.py
```

### Run the API

```bash
python -m uvicorn api:app --reload
```

Open `http://127.0.0.1:8000/docs` to test the API.

## API Example

**POST `/search`**

Request:

```json
{
  "question": "Can I work remotely?"
}
```

Example response:

```json
{
  "question": "Can I work remotely?",
  "results": [
    {
      "title": "Remote Work Policy",
      "content": "Employees can work from home with manager approval."
    },
    {
      "title": "Leave Policy",
      "content": "Employees receive 15 days of annual paid leave."
    }
  ]
}
```

The API returns the two most relevant matching documents based on similarity.
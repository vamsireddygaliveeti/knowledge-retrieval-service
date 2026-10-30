
import os

from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel, Field
from pinecone import Pinecone
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore

load_dotenv()

# Connect to Pinecone
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index(os.getenv("PINECONE_INDEX_NAME"))

# Load embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Connect LangChain to Pinecone
vector_store = PineconeVectorStore(
    index=index,
    embedding=embeddings
)

# Create FastAPI application
app = FastAPI(title="Knowledge Retrieval Service")

# Define the incoming request
class SearchRequest(BaseModel):
    question: str = Field(min_length=1)

# Create search endpoint
@app.post("/search")
def search_documents(request: SearchRequest):
    results = vector_store.similarity_search(
        request.question,
        k=2
    )

    return {
        "question": request.question,
        "results": [
            {
                "title": doc.metadata.get("title"),
                "content": doc.page_content
            }
            for doc in results
        ]
    }

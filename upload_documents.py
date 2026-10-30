
import json
import os

from dotenv import load_dotenv
from pinecone import Pinecone
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore

# 1. Load Pinecone API key
load_dotenv()

api_key = os.getenv("PINECONE_API_KEY")
index_name = os.getenv("PINECONE_INDEX_NAME")

# 2. Connect to Pinecone
pc = Pinecone(api_key=api_key)
index = pc.Index(index_name)

# 3. Load the embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# 4. Connect LangChain to Pinecone
vector_store = PineconeVectorStore(
    index=index,
    embedding=embeddings
)

# 5. Read our JSON file
with open("records.json", "r", encoding="utf-8") as file:
    records = json.load(file)

# 6. Convert records into LangChain documents
documents = []

for record in records:
    document = Document(
        page_content=record["content"],
        metadata={"title": record["title"]}
    )
    documents.append(document)

# 7. Upload documents to Pinecone
vector_store.add_documents(
    documents=documents,
    ids=[str(record["id"]) for record in records]
)

print("Documents uploaded successfully!")


import os
from dotenv import load_dotenv
from pinecone import Pinecone
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore

# Load our Pinecone settings
load_dotenv()

# Connect to Pinecone
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index(os.getenv("PINECONE_INDEX_NAME"))

# Use the same embedding model as uploading
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Connect LangChain to our vector database
vector_store = PineconeVectorStore(
    index=index,
    embedding=embeddings
)

# Ask a question
question = input("Enter your question: ")

# Search for the two most relevant documents
results = vector_store.similarity_search(question, k=2)

# Display the results
for i, document in enumerate(results, start=1):
    print(f"\nResult {i}")
    print("Title:", document.metadata.get("title"))
    print("Content:", document.page_content)

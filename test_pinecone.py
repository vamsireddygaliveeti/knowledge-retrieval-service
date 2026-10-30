
import os
from dotenv import load_dotenv
from pinecone import Pinecone

# Read the .env file
load_dotenv()

# Get our Pinecone settings
api_key = os.getenv("PINECONE_API_KEY")
index_name = os.getenv("PINECONE_INDEX_NAME")

# Check that settings exist
if not api_key or not index_name:
    raise ValueError("Missing Pinecone settings in .env")

# Connect to Pinecone
pc = Pinecone(api_key=api_key)

# Get information about our index
index_info = pc.describe_index(name=index_name)

print("Connected successfully!")
print("Index:", index_info.name)
print("Dimensions:", index_info.dimension)
print("Metric:", index_info.metric)

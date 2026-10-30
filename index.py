
import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec

load_dotenv()

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

index_name = "company-vectors"

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )
    print("Index created successfully!")
else:
    print("Index already exists!")

info = pc.describe_index(index_name)
print("Index:", info.name)
print("Dimensions:", info.dimension)
print("Metric:", info.metric)

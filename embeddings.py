
from sentence_transformers import SentenceTransformer
from sentence_transformers import util

# Load a pretrained embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Sample company information
documents = [
    "Employees can work from home with manager approval.",
    "Employees receive 15 days of annual paid leave.",
    "Contact IT support for password resets."
]

# User question
question = "Can I work remotely?"

# Convert text into embeddings
document_vectors = model.encode(documents)
question_vector = model.encode(question)

# Compare the question with each document
scores = util.cos_sim(
    question_vector,
    document_vectors
)[0]

# Find the most similar document
best_index = scores.argmax().item()

print("Question:", question)
print("Best match:", documents[best_index])
print("Similarity score:", round(scores[best_index].item(), 3))

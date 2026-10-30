
import json

# Step 1: Load records from JSON
with open("records.json", "r") as file:
    records = json.load(file)

# Step 2: Create a search function
def search_records(question):
    for record in records:
        if question.lower() in record["content"].lower():
            return record["content"]

    return "No matching information found."

# Step 3: Ask the user for input
question = input("Enter your question: ")

# Step 4: Search the records
answer = search_records(question)

# Step 5: Display the result
print("Result:", answer)

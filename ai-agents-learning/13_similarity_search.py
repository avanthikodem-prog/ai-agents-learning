from sentence_transformers import SentenceTransformer, util

# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Documents
documents = [
    "Python is a programming language.",
    "Python is used for machine learning.",
    "FastAPI is a framework for building APIs.",
    "I like eating pizza."
]

# User query
query = "What is Python used for?"

# Convert documents and query into embeddings
document_embeddings = model.encode(documents, convert_to_tensor=True)
query_embedding = model.encode(query, convert_to_tensor=True)

# Calculate similarity
similarities = util.cos_sim(query_embedding, document_embeddings)[0]

# Get the most similar documents
results = similarities.argsort(descending=True)

print("Query:")
print(query)

print("\nSimilarity results:")

for index in results:
    print(
        f"{similarities[index]:.4f} -> {documents[index]}"
    )
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# Our documents
documents = [
    "Python is a popular programming language used for machine learning.",
    "Java is widely used for enterprise application development.",
    "FastAPI is a Python framework for building APIs.",
    "LangGraph is used to build stateful AI agent workflows.",
    "Docker is used to package applications into containers."
]


# Convert documents into embeddings
document_embeddings = model.encode(documents)


# Get user's question
query = input("\nEnter your question: ")


# Convert question into an embedding
query_embedding = model.encode([query])


# Calculate similarity
similarities = cosine_similarity(
    query_embedding,
    document_embeddings
)[0]


# Find the most similar document
best_index = similarities.argmax()


# Display results
print("\nQuestion:")
print(query)

print("\nMost relevant document:")
print(documents[best_index])

print("\nSimilarity score:")
print(similarities[best_index])
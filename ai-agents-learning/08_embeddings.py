from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# Texts we want to convert into embeddings
sentences = [
    "I love Python programming",
    "Python is my favorite programming language",
    "I like cricket"
]


# Convert text into embeddings
embeddings = model.encode(sentences)


# Display embedding information
for sentence, embedding in zip(sentences, embeddings):
    print("\nSentence:", sentence)
    print("Vector length:", len(embedding))
    print("First 5 values:", embedding[:5])


# Calculate similarity between sentences
similarity = cosine_similarity(embeddings)


print("\nSimilarity Matrix:")
print(similarity)
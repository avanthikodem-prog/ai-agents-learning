from sentence_transformers import SentenceTransformer

# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Sample sentences
sentences = [
    "Python is a programming language.",
    "Python is used for machine learning.",
    "I like eating pizza."
]

# Convert sentences into embeddings
embeddings = model.encode(sentences)

print("Number of sentences:", len(sentences))
print("Embedding shape:", embeddings.shape)

for sentence, embedding in zip(sentences, embeddings):
    print("\nSentence:", sentence)
    print("First 10 embedding values:", embedding[:10])
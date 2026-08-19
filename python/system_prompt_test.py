import ollama

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "system",
            "content": "You are a Java teacher. Always explain Java concepts for beginners using simple English and a small example."
        },
        {
            "role": "user",
            "content": "Explain polymorphism."
        }
    ]
)

print(response["message"]["content"])
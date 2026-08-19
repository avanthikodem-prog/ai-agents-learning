import ollama

prompt = """
Explain the four pillars of OOP in Java.

Return the answer in exactly this format for each pillar:

Pillar:
Definition:
Java Example:
Why it is useful:

Do this for:
1. Encapsulation
2. Abstraction
3. Inheritance
4. Polymorphism

Use simple English.
"""

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(response["message"]["content"])
import ollama

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": """Classify each statement as EASY or HARD.

Example 1:
Java is a programming language.
Answer: EASY

Example 2:
Polymorphism allows objects to take multiple forms.
Answer: HARD

Example 3:
A variable stores a value.
Answer: EASY

Now classify:

Inheritance allows one class to acquire properties and methods from another class.

Return only:
EASY or HARD"""
        }
    ]
)

print(response["message"]["content"])
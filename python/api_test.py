import requests

url = "http://localhost:11434/api/chat"

prompt = input("Enter your prompt: ")

data = {
    "model": "llama3.2",
    "messages": [
        {
            "role": "user",
            "content": prompt
        }
    ],
    "stream": False
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)

result = response.json()

print("\nAI Response:")
print(result["message"]["content"])
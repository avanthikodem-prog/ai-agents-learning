from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import requests
import json

app = FastAPI()


class ChatRequest(BaseModel):
    prompt: str


def ollama_stream(prompt: str):
    url = "http://localhost:11434/api/chat"

    data = {
        "model": "llama3.2",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": True
    }

    response = requests.post(
        url,
        json=data,
        stream=True
    )

    response.raise_for_status()

    for line in response.iter_lines():
        if line:
            result = json.loads(line)

            content = result.get("message", {}).get("content", "")

            if content:
                yield f"data: {content}\n\n"


@app.post("/chat/stream")
def chat_stream(request: ChatRequest):
    return StreamingResponse(
        ollama_stream(request.prompt),
        media_type="text/event-stream"
    )
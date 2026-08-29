from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import requests
import json
import os

app = FastAPI(title="Docker Ollama API")


class ChatRequest(BaseModel):
    prompt: str


# Ollama URL
OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://host.docker.internal:11434/api/chat"
)


def ollama_stream(prompt: str):
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

    try:
        response = requests.post(
            OLLAMA_URL,
            json=data,
            stream=True,
            timeout=120
        )

        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        yield f"data: Ollama connection error: {str(e)}\n\n"
        return

    for line in response.iter_lines():
        if line:
            result = json.loads(line)

            content = result.get(
                "message", {}
            ).get("content", "")

            if content:
                yield f"data: {content}\n\n"


@app.get("/")
def home():
    return {
        "message": "Docker Ollama API is running"
    }


@app.post("/chat/stream")
def chat_stream(request: ChatRequest):
    return StreamingResponse(
        ollama_stream(request.prompt),
        media_type="text/event-stream"
    )
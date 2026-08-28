from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio

app = FastAPI()


async def event_generator():
    messages = [
        "Hello",
        "This",
        "is",
        "Server-Sent",
        "Events",
        "using",
        "FastAPI"
    ]

    for message in messages:
        yield f"data: {message}\n\n"
        await asyncio.sleep(1)


@app.get("/events")
async def events():
    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream"
    )
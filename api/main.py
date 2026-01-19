import tiktoken
from fastapi import FastAPI
from fastapi.responses import StreamingResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
import requests

from api.settings import settings
from api.models import ChatRequest
from api.helpers import trim_history
from api.db import get_client, find_nearest_embeddings


app = FastAPI()
app.mount("/css", StaticFiles(directory="api/ui/css"), name="css")
app.mount("/js", StaticFiles(directory="api/ui/js"), name="js")


client_qdrant = get_client(
    host=settings.db_host,
    port=settings.db_port,
)


encoding = tiktoken.encoding_for_model(settings.llm_model)


@app.get("/", response_class=HTMLResponse)
async def index():
    """
    TODO
    """
    global CONTEXT_PAGES
    CONTEXT_PAGES = []

    with open(settings.path_html, "r") as f:
        return f.read()


@app.post("/api/chat/stream")
async def todo(
    req: ChatRequest,
):
    """
    Stream response from chatting with AI.
    """
    global CONTEXT_PAGES

    # Create embedding from user's text
    url = f"{settings.url_base}/api/text-to-embedding"
    payload = {"text": req.text}
    response = requests.post(url, json=payload)
    embedding = response.json()["embedding"]

    # Find nearest embeddings
    nearest_embeddings = find_nearest_embeddings(
        client=client_qdrant,
        collection_name=settings.db_collection_name,
        embedding=embedding,
        limit=settings.limit_nearest_embeddings,
        file=req.file,
    )

    CONTEXT_PAGES.extend(nearest_embeddings)

    unique_pages = {each.payload.get("page_number"): each for each in CONTEXT_PAGES}
    CONTEXT_PAGES = list(unique_pages.values())
    
    CONTEXT_PAGES.sort(key=lambda x: x.payload.get("page_number"))

    text_similar = "\n\n".join(
        f"page number: {each.payload.get('page_number')}\n\n{each.payload.get('text')}"
        for each in CONTEXT_PAGES
    )

    history = trim_history(
        encoding=encoding,
        history=(req.history or []),
        threshold_history_max_tokens=settings.threshold_history_max_tokens,
    )

    message_user = {
        "role": "user",
        "content": f"Answer the question {req.text} based on these pages:\n\n{text_similar}"
    }

    upstream_payload = {
        "history": [{"role":each.get("role"), "content": each.get("content")}for each in history],
        "message_user": message_user,
        "prompt_system_name": "chat_manuals",
    }

    upstream_stream = requests.post(
        f"{settings.url_base}/api/chat/stream",
        json=upstream_payload,
        stream=True,
    )

    def event_generator():
        for chunk in upstream_stream.iter_content(chunk_size=None):
            if chunk:
                yield chunk

    return StreamingResponse(event_generator(), media_type="text/plain")

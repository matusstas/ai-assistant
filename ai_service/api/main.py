import base64
from openai import OpenAI
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse

from ai_service.api.settings import settings
from ai_service.api.models import ImageToTextReponse, TextToEmbeddingRequest, TextToEmbeddingReponse, ChatRequest

app = FastAPI()

client_openai = OpenAI(
    api_key=settings.api_key_openai,
)


@app.post("/api/image-to-text")
async def image_to_text(
    file: UploadFile = File(...),
) -> ImageToTextReponse:
    """
    Extract text from image.
    """
    image = await file.read()
    image_base64 = base64.b64encode(image).decode("utf-8")

    response = client_openai.responses.create(
        model=settings.llm_model,
        input=[
            {
                "role": "system",
                "content": [
                    {
                        "type": "input_text",
                        "text": settings.prompts.get("image_to_text"),
                    }
                ],
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{image_base64}",
                        "detail": settings.llm_detail,
                    }
                ],
            },
        ],
    )

    return ImageToTextReponse(text=response.output_text)


@app.post("/api/text-to-embedding")
async def text_to_embedding(
    req: TextToEmbeddingRequest,
) -> TextToEmbeddingReponse:
    """
    Create embedding from text.
    """
    response = client_openai.embeddings.create(
        input=req.text,
        model=settings.embedding_model,
    )

    return TextToEmbeddingReponse(embedding=response.data[0].embedding)


@app.post("/api/chat/stream")
async def chat_stream(
    req: ChatRequest,
) -> StreamingResponse:
    """
    Stream response from chatting with AI.
    """
    stream = client_openai.chat.completions.create(
        model=settings.llm_model,
        messages=[
            {"role": "system", "content": settings.prompts.get(req.prompt_system_name)},
            *req.history,
            req.message_user,
        ],
        stream=True,
    )

    def event_generator():
        for chunk in stream:
            if chunk.choices and chunk.choices[0].delta:
                delta = chunk.choices[0].delta.content
                if delta:
                    yield delta.encode("utf-8")

    return StreamingResponse(event_generator(), media_type="text/plain")
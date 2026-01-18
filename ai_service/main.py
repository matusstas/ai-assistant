import base64
from openai import OpenAI
from fastapi import FastAPI, UploadFile, File

from ai_service.settings import settings
from ai_service.models import ImageToTextReponse, TextToEmbeddingRequest, TextToEmbeddingReponse

client_openai = OpenAI(api_key=settings.api_key_openai)
app = FastAPI()


@app.post("/api/image-to-text")
async def image_to_text(
    file: UploadFile = File(...),
) -> ImageToTextReponse:
    """
    TODO
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
    TODO
    """
    response = client_openai.embeddings.create(
        input=req.text,
        model=settings.embedding_model,
    )

    return TextToEmbeddingReponse(embedding=response.data[0].embedding)

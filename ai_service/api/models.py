from pydantic import BaseModel
from typing import List, Optional

class ImageToTextReponse(BaseModel):
    """
    Response model for the endpoint /api/image-to-text.
    """
    text: str


class TextToEmbeddingRequest(BaseModel):
    """
    Request model for the endpoint /api/text-to-embedding.
    """
    text: str


class TextToEmbeddingReponse(BaseModel):
    """
    Response model for the endpoint /api/text-to-embedding.
    """
    embedding: List[float]


class ChatRequest(BaseModel):
    """
    Request model for the endpoint /api/chat/stream.
    """
    history: Optional[List[dict]] = []
    message_user: dict
    prompt_system_name: str
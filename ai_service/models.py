from pydantic import BaseModel
from typing import List

class ImageToTextReponse(BaseModel):
    """
    TODO
    """
    text: str


class TextToEmbeddingRequest(BaseModel):
    """
    TODO
    """
    text: str


class TextToEmbeddingReponse(BaseModel):
    """
    TODO
    """
    embedding: List[float]
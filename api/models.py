from pydantic import BaseModel
from typing import List, Optional


class ChatRequest(BaseModel):
    """
    Request model for the endpoint /api/chat/stream.
    """
    file: str
    text: str
    history: Optional[List[dict]] = []

from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from qdrant_client.models import PointStruct
from typing import List
import uuid


def get_client(
    host: str,
    port: str,
) -> QdrantClient:
    """
    TODO
    """
    client = QdrantClient(
        host=host,
        port=port,
    )

    return client


def create_collection(
    client: QdrantClient,
    collection_name: str,
    size: int,
) -> None:
    """
    TODO
    """
    if not client.collection_exists(collection_name):
        client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(
                size=size,
                distance=Distance.COSINE,
            ),
        )


def insert_embeddings(
    client: QdrantClient,
    collection_name: str,
    embeddings: List[dict],
) -> None:
    """
    TODO
    """
    points = []

    for each in embeddings:
        id = str(uuid.uuid4())
        vector = each.get("embedding")
        payload = {k: v for k, v in each.items() if k != "embedding"}

        points.append(
            PointStruct(
                id=id,
                vector=vector,
                payload=payload,
            )
        )

    client.upsert(
        collection_name=collection_name,
        points=points,
    )

from qdrant_client import QdrantClient
from qdrant_client.http import models
from typing import List


def get_client(
    host: str,
    port: str,
) -> QdrantClient:
    """
    Connect to Qdrant. 
    """
    client = QdrantClient(
        host=host,
        port=port,
    )

    return client


def find_nearest_embeddings(
    client: QdrantClient,
    collection_name: str,
    embedding: List[float],
    limit: int,
    file: str,
):
    """
    Find `limit` nearest embeddings in specified `file`.
    """
    nearest_embeddings = client.query_points(
        collection_name=collection_name,
        query=embedding,
        limit=limit,
        query_filter=models.Filter(
            must=[
                models.FieldCondition(
                    key="file",
                    match=models.MatchValue(value=file),
                )
            ]
        )
    )
    
    return nearest_embeddings.points
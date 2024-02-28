import os


from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

QDRANT_CLINET: QdrantClient | None = None


def get_qdrant_client() -> QdrantClient:
    """Get a qdrant client."""
    global QDRANT_CLINET

    if QDRANT_CLINET is not None:
        return QDRANT_CLINET

    url = os.environ.get("QDRANT_CLINET_URL")
    if not url:
        raise ValueError("QDRANT_CLINET_URL not set")
    QDRANT_CLINET = QdrantClient(url)
    return QDRANT_CLINET


def create_collection(
    client:QdrantClient, 
    collection_name: str,
    vector_size: int = 1536,
    distance: Distance = Distance.COSINE
) -> None:
    client.create_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(
            size=vector_size,
            distance=distance,
        ),
    )

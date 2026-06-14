# rag/embeddings.py

from sentence_transformers import (
    SentenceTransformer
)

_model = None

def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model


def generate_embedding(text):

    if not text:
        return []

    model = get_model()
    embedding = model.encode(
        text,
        convert_to_numpy=True
    )

    return embedding.tolist()
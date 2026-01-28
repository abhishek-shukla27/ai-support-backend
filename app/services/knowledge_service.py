from app.ai.embeddings import get_embedding
from app.ai.vector_store import add_text

def add_knowledge(content: str):
    embedding = get_embedding(content)
    add_text(embedding, content)

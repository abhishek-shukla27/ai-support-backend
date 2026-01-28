
from app.ai.vector_store import add_text

BUSINESS_KNOWLEDGE = {}

def add_knowledge(business_id: str, content: str):
    BUSINESS_KNOWLEDGE[business_id] = content
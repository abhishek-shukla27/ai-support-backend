from app.ai.embeddings import get_embedding
from app.ai.vector_store import search
from app.ai.llm import ask_llm


# Temporary in-memory knowledge store
BUSINESS_KNOWLEDGE = {}

def add_knowledge(business_id: str, content: str):
    BUSINESS_KNOWLEDGE[business_id] = content

def answer_question(business_id: str, question: str):
    context = BUSINESS_KNOWLEDGE.get(business_id)

    if not context:
        return "I don't have information about this business yet."

    prompt = f"""
You are a customer support assistant.
Answer ONLY using the information below.

Business Info:
{context}

Question:
{question}

Answer:
"""
    return ask_llm(prompt)

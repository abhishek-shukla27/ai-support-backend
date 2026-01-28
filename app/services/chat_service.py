from app.services.knowledge_service import BUSINESS_KNOWLEDGE
from app.ai.vector_store import search
from app.ai.llm import ask_llm


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

from app.services.knowledge_service import BUSINESS_KNOWLEDGE,normalize_business_id
from app.ai.llm import ask_llm


def answer_question(business_id: str, question: str):
    key=normalize_business_id(business_id)
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

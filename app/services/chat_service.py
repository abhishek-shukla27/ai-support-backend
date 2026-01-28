from app.ai.embeddings import get_embedding
from app.ai.vector_store import search
from app.ai.llm import ask_llm

def answer_question(question: str):
    query_embedding = get_embedding(question)
    contexts = search(query_embedding)

    if not contexts:
        return "Sorry, I don't have information on that."

    context_text = "\n".join(contexts)

    prompt = f"""
Use ONLY the context below to answer.

Context:
{context_text}

Question:
{question}

Answer in a friendly, professional tone:
"""

    return ask_llm(prompt)

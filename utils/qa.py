from utils.embed_store import search
from utils.hf_api import query_hf

def answer_query(question):
    retrieved_docs = search(question)

    context = "\n\n".join(retrieved_docs)

    prompt = f"""
You are a helpful AI assistant. Use ONLY the context below to answer.

CONTEXT:
{context}

QUESTION:
{question}

If answer is not in context, say "The document does not contain that information."
"""

    return query_hf(prompt)

from groq import Groq
from rag.retrieval import retrieve_context

_client = None

def get_groq_client():
    global _client
    if _client is None:
        from config.settings import GROQ_API_KEY
        if not GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY environment variable is not set")
        _client = Groq(api_key=GROQ_API_KEY)
    return _client


def answer_question(
    question,
    document_id
):
    client = get_groq_client()

    chunks = retrieve_context(
    question,
    document_id
)

    context = "\n".join(
        [
            chunk["chunk_text"]
            for chunk in chunks
        ]
    )

    prompt = f"""
Answer using ONLY the context.

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
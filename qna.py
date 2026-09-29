from gemini_client import (
    generate_text,
    GeminiError
)


def answer_question(question: str) -> str:

    prompt = f"""
You are EduGenie, an AI educational assistant.

Answer the student's question accurately
and in simple language.

Rules:

1. Give the direct answer first.
2. Explain the answer clearly.
3. Use an example when useful.
4. Keep the response suitable for students.
5. Do not invent sources.
6. If the question is ambiguous, mention the assumption.

Student Question:

{question}
"""

    try:

        return generate_text(prompt)

    except GeminiError as error:

        return (
            "Q&A service is currently unavailable.\n\n"
            f"Details: {error}"
        )
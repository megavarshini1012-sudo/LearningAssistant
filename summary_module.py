from gemini_client import (
    generate_text,
    GeminiError
)


def summarize_text(text: str) -> str:

    prompt = f"""
Summarize the following educational passage.

Requirements:

- Keep the important information.
- Remove repetition.
- Use simple language.
- Make it useful for quick revision.
- Do not add information that is not in the passage.
- Include important points as bullet points.

Educational Passage:

{text}
"""

    try:

        return generate_text(
            prompt
        )

    except GeminiError as error:

        return (
            "Summarization service is unavailable.\n\n"
            f"Details: {error}"
        )
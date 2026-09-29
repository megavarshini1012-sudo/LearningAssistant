from functools import lru_cache

from transformers import pipeline

from config import settings

from gemini_client import (
    generate_text,
    GeminiError
)


@lru_cache(maxsize=1)
def get_local_model():

    return pipeline(
        "text2text-generation",
        model=settings.local_model_name,
        tokenizer=settings.local_model_name
    )


def local_explanation(topic: str) -> str:

    model = get_local_model()

    prompt = f"""
Explain the following topic to a beginner.

Topic:
{topic}

Give:

1. Simple definition
2. Important points
3. Easy example
4. Short recap

Use simple language.
"""

    result = model(
        prompt,
        max_new_tokens=200,
        do_sample=False
    )

    return result[0]["generated_text"].strip()


def explain_topic(topic: str) -> str:

    # Try local LaMini model first
    if settings.enable_local_model:

        try:

            return local_explanation(topic)

        except Exception:

            # Fall back to Gemini
            pass

    # Gemini fallback

    prompt = f"""
Explain the following topic to a beginner.

Topic:
{topic}

Structure your answer as:

1. Simple Definition
2. Key Points
3. Easy Example
4. One-line Recap

Keep the explanation concise and easy to understand.
"""

    try:

        return generate_text(prompt)

    except GeminiError as error:

        return (
            "Explanation service is unavailable.\n\n"
            f"Details: {error}"
        )
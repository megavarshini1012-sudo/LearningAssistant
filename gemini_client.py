from functools import lru_cache

from google import genai

from config import settings


class GeminiError(Exception):
    """
    Custom exception for Gemini-related errors.
    """
    pass


@lru_cache(maxsize=1)
def get_client():

    if not settings.gemini_api_key:

        raise GeminiError(
            "GEMINI_API_KEY is not configured. "
            "Please add your Gemini API key to the .env file."
        )

    return genai.Client(
        api_key=settings.gemini_api_key
    )


def generate_text(prompt: str) -> str:

    try:

        client = get_client()

        response = client.models.generate_content(
            model=settings.gemini_model,
            contents=prompt
        )

        text = getattr(
            response,
            "text",
            None
        )

        if not text:

            raise GeminiError(
                "Gemini returned an empty response."
            )

        return text.strip()

    except GeminiError:

        raise

    except Exception as error:

        raise GeminiError(
            f"Gemini request failed: {error}"
        ) from error
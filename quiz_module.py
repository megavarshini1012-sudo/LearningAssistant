import json
import re

from gemini_client import (
    generate_text,
    GeminiError
)


def clean_json_block(text: str) -> str:

    text = text.strip()

    # Remove ```json
    text = re.sub(
        r"^```(?:json)?\s*",
        "",
        text,
        flags=re.IGNORECASE
    )

    # Remove ```
    text = re.sub(
        r"\s*```$",
        "",
        text
    )

    return text.strip()


def validate_quiz(data):

    if not isinstance(data, list):

        raise ValueError(
            "Quiz response must be a list."
        )

    if len(data) != 3:

        raise ValueError(
            "Quiz must contain exactly 3 questions."
        )

    for question in data:

        if not isinstance(question, dict):

            raise ValueError(
                "Each question must be an object."
            )

        required_fields = [
            "question",
            "options",
            "answer"
        ]

        for field in required_fields:

            if field not in question:

                raise ValueError(
                    f"Missing field: {field}"
                )

        if not isinstance(
            question["options"],
            list
        ):

            raise ValueError(
                "Options must be a list."
            )

        if len(question["options"]) != 4:

            raise ValueError(
                "Each question must have 4 options."
            )

        if question["answer"] not in question["options"]:

            raise ValueError(
                "Correct answer must match one option."
            )

    return data


def generate_quiz(passage: str):

    prompt = f"""
Create exactly 3 multiple-choice questions
from the educational passage below.

Each question must have exactly 4 options.

Return ONLY valid JSON.

Do NOT use Markdown.

JSON format:

[
  {{
    "question": "Question text",
    "options": [
      "Option A",
      "Option B",
      "Option C",
      "Option D"
    ],
    "answer": "Correct option"
  }}
]

Make the questions relevant to the passage.

Educational Passage:

{passage}
"""

    try:

        response = generate_text(
            prompt
        )

        cleaned = clean_json_block(
            response
        )

        data = json.loads(
            cleaned
        )

        return validate_quiz(
            data
        )

    except GeminiError as error:

        return {
            "error": f"Gemini error: {error}"
        }

    except json.JSONDecodeError as error:

        return {
            "error": (
                "Could not parse the quiz response "
                f"as JSON: {error}"
            )
        }

    except ValueError as error:

        return {
            "error": str(error)
        }

    except Exception as error:

        return {
            "error": (
                f"Quiz generation failed: {error}"
            )
        }
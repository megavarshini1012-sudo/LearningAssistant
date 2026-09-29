from gemini_client import (
    generate_text,
    GeminiError
)


def get_learning_recommendations(
    topic: str
) -> str:

    prompt = f"""
Create a personalized learning path
for the following topic:

{topic}

Organize the learning path from
BEGINNER to ADVANCED.

Include:

1. Level
2. Concepts to learn
3. Suggested timeline
4. Practice activities
5. Resource types such as:
   - Videos
   - Articles
   - Books
   - Documentation
6. A checkpoint after every stage.

Make the learning plan practical
and easy to follow.

Do not invent specific URLs.
"""

    try:

        return generate_text(
            prompt
        )

    except GeminiError as error:

        return (
            "Learning recommendation service "
            "is unavailable.\n\n"
            f"Details: {error}"
        )
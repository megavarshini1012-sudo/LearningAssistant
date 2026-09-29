import os

from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()


@dataclass(frozen=True)
class Settings:

    gemini_api_key: str = os.getenv(
        "GEMINI_API_KEY",
        ""
    )

    gemini_model: str = os.getenv(
        "GEMINI_MODEL",
        "gemini-2.5-flash"
    )

    local_model_name: str = os.getenv(
        "LOCAL_MODEL_NAME",
        "MBZUAI/LaMini-Flan-T5-783M"
    )

    enable_local_model: bool = os.getenv(
        "ENABLE_LOCAL_MODEL",
        "true"
    ).lower() in {
        "1",
        "true",
        "yes",
        "on"
    }


settings = Settings()
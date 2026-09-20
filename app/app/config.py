import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT", "")
    azure_openai_api_key = os.getenv("AZURE_OPENAI_API_KEY", "")
    azure_openai_api_version = os.getenv(
        "AZURE_OPENAI_API_VERSION",
        "2024-10-21"
    )

    azure_openai_chat_deployment = os.getenv(
        "AZURE_OPENAI_CHAT_DEPLOYMENT",
        ""
    )

    azure_openai_embedding_deployment = os.getenv(
        "AZURE_OPENAI_EMBEDDING_DEPLOYMENT",
        ""
    )

    top_k = int(os.getenv("TOP_K", "4"))

    app_name = os.getenv(
        "APP_NAME",
        "azure-openai-genai-rca"
    )

    log_level = os.getenv(
        "LOG_LEVEL",
        "INFO"
    )


settings = Settings()

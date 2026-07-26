from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application configuration.

    Every configurable value should come from environment variables.
    """

    APP_NAME: str = "Enterprise Knowledge Assistant"

    APP_VERSION: str = "1.0.0"

    API_PREFIX: str = "/api/v1"

    OPENAI_API_KEY: str

    MODEL_NAME: str = "gpt-4.1-mini"

    EMBEDDING_MODEL: str = "text-embedding-3-small"

    DATA_DIRECTORY: str = "./data/uploaded_pdfs"

    CHROMA_DB_PATH: str = "./chroma_db"

    CHUNK_SIZE: int = 1000

    CHUNK_OVERLAP: int = 200

    TOP_K: int = 10

    RERANK_TOP_K: int = 5

    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
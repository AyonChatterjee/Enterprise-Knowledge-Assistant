from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Central configuration for the application.

    Every configurable value should come from the environment.
    """

    OPENAI_API_KEY: str

    MODEL_NAME: str = "gpt-4.1-mini"

    EMBEDDING_MODEL: str = "text-embedding-3-small"

    CHROMA_DB_PATH: str = "./chroma_db"

    DATA_DIRECTORY: str = "./data/uploaded_pdfs"

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
def get_settings() -> Settings:
    """
    Return a cached Settings instance.

    Using lru_cache ensures we load configuration only once.
    """
    return Settings()


settings = get_settings()
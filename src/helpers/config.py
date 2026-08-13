from __future__ import annotations

from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # ---------------- CONFIGURATION MECHANICS ----------------
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # ---------------- CORE SERVICE APP STATE ----------------
    APP_NAME: str = "FastAPI Production Service"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: Literal["local", "staging", "production"] = "local"
    LOG_LEVEL: Literal["DEBUG", "INFO", "WARNING", "ERROR"] = "INFO"

    # ---------------- FILE UPLOAD CONFIGURATION ----------------
    FILE_ALLOWED_TYPES: list[str] = ["text/plain", "application/pdf"]
    FILE_MAX_SIZE: int = 10  # In MB
    FILE_DEFAULT_CHUNK_SIZE: int = 512000  # 512KB

    # ---------------- LLM SPECS ----------------
    GENERATION_PROVIDER: str = "OPENAI"
    GENERATION_MODEL_NAME: str = "gpt-4o-mini"
    GENERATION_DEFAULT_MAX_TOKENS: int = 200
    GENERATION_DEFAULT_TEMPERATURE: float = 0.1
    INPUT_DEFAULT_MAX_CHARACTERS: int = 1024

    EMBEDDING_PROVIDER: str = "COHERE"
    EMBEDDING_MODEL_NAME: str = "embed-multilingual-light-v3.0"
    EMBEDDING_MODEL_SIZE: int = 384

    GOOGLE_API_KEY: str | None = None

    # ---------------- VECTORSTORE SPECS ----------------
    VECTORSTORE_PROVIDER: str = "CHROMA"
    VECTORSTORE_COLLECTION_NAME: str = "rag_knowledge_base"
    VECTORSTORE_PERSIST_DIR: str = "src/assets/vectorstores"

    # ---------------- RAG SPECS ----------------
    CHUNK_SIZE: int = 500
    CHUNK_OVERLAP: int = 50

    # Retrieval Specs
    RETRIEVAL_SEARCH_TYPE: str = "similarity"
    RETRIEVAL_K: int = 4

    # ---------------- REUSABLE HELPERS ----------------
    @property
    def is_local(self) -> bool:
        """Quick boolean flag to evaluate local runtime contexts."""
        return self.ENVIRONMENT == "local"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Returns a cached singleton instance of the system configuration.
    
    Prevents repeated disk read operational overhead during API requests.
    """
    return Settings()

from pydantic_settings import BaseSettings, SettingsConfigDict


class ApiConfig(BaseSettings):
    """
    API configuration

    For local development use .env file if you are lazy to EXPORT env vars.
    """
    model_config = SettingsConfigDict(
        env_nested_delimiter="__",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )
    # LLM
    llm_model: str

    # DB
    db_host: str
    db_port: str
    db_collection_name: str

    # AI SERVICE
    url_base: str

    # MISCELLANEOUS
    threshold_history_max_tokens: int
    path_html: str
    limit_nearest_embeddings: int


settings = ApiConfig()

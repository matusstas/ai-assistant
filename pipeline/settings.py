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
    # MISCELLANEOUS
    folder_root: str
    folder_data_images: str
    folder_data_text: str
    folder_data_embeddings: str
    dpi: int

    # AI SERVICE
    url_base: str


settings = ApiConfig()

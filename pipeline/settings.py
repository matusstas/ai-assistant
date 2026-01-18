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
    folder_cloud_storage: str
    folder_data: str
    dpi: int


settings = ApiConfig()

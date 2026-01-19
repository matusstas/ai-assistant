# from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

# class DBConfig(BaseModel):
#     """
#     Postgres configuration
#     """
#     instance_connection: str = ""       # DB__INSTANCE_CONNECTION
#     host: str = ""                      # DB__HOST 
#     user: str = ""                      # DB__USER
#     port: str = ""                      # DB__PORT
#     password: str = ""                  # DB__PASSWORD
#     db: str = ""                        # DB__DB



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

    # EMBEDDING
    embedding_dimension_size: int

    # DB
    db_host: str
    db_port: str
    db_collection_name: str


settings = ApiConfig()

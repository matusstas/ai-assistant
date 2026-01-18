from pydantic_settings import BaseSettings, SettingsConfigDict
import os
import errno
from pathlib import Path
from typing import Optional
from pydantic import BaseModel


class PromptsConfig(BaseModel):
    """
    Prompts configuration
    """
    @classmethod
    def load_from_folder(cls) -> "PromptsConfig":
        """
        Dynamically loads all prompt files from the directory `ai_service/prompts`
        and assigns their content as attributes in the config.
        """
        prompts_directory = Path("ai_service/prompts")
        prompts = {}

        # Check if the directory exists
        if not prompts_directory.is_dir():
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), str(prompts_directory))

        # Iterate over all files in the directory
        for file_path in prompts_directory.iterdir():
            if file_path.is_file() and file_path.suffix == ".md":
                attribute_name = file_path.stem.lower()

                try:
                    prompts[attribute_name] = file_path.read_text(encoding="utf-8")
                except Exception as e:
                    raise Exception(f"Error reading {file_path}: {str(e)}")

        return prompts


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
    # API KEYS
    api_key_openai: str

    # LLM
    llm_model: str
    llm_detail: str
    prompts: Optional[PromptsConfig] = None

    # EMBEDDING
    embedding_model: str


settings = ApiConfig()
settings.prompts = PromptsConfig.load_from_folder()

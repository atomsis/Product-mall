from os import getenv
from pydantic_settings import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    db_url: str = f"sqlite+aiosqlite:///{BASE_DIR}/shop.db"
    echo: bool = True
    # echo: bool = False


settings = Settings()

# settings.db_url =

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Supercharging Developers Demo"
    DEBUG: bool = False
    DATABASE_URL: str = (
        "postgresql://admin:admin@db/reference"  # only for demo purposes
    )

    CORS_ORIGINS: list[str] = ["*"]
    CORS_HEADERS: list[str] = ["*"]
    CORS_ORIGINS_REGEX: str | None = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

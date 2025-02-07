from pydantic import BaseSettings

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    YOUTUBE_API_KEY: str
    DATABASE_URL: str
    REDIS_URL: str
    SECRET_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()

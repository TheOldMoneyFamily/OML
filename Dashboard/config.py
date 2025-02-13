from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "mysql+mysqlconnector://your_db_user:your_db_password@localhost/dashboard_db"
    SECRET_KEY: str = "your-secret-key"  # change this to a random secret in production
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()

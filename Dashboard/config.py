from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = os.get.env("mysql+mysqlconnector://db_user:your_db_password@localhost/dashboard_db")
    SECRET_KEY: str = os.get.env("secret-key")  
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()

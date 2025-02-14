from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
    PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")
    YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
    GOOGLE_ANALYTICS_VIEW_ID = os.getenv("GOOGLE_ANALYTICS_VIEW_ID")
    GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 8000))
    ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "*")
    DATABASE_URL = os.getenv("DATABASE_URL")
    STATIC_FILES_DIR = os.getenv("STATIC_FILES_DIR", "frontend/static")

settings = Settings()

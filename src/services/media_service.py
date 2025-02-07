import os
import pyttsx3
from gtts import gTTS

UPLOAD_DIR = "media"

def generate_audio(text: str, format: str = "mp3"):
    \"\"\"
    Converts text to audio (MP3/WAV).
    \"\"\"
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    file_path = os.path.join(UPLOAD_DIR, f"output.{format}")

    if format == "mp3":
        tts = gTTS(text=text, lang="en")
        tts.save(file_path)
    elif format == "wav":
        engine = pyttsx3.init()
        engine.save_to_file(text, file_path)
        engine.runAndWait()
    
    return file_path

def generate_video_script(article: str):
    \"\"\"
    Generates a script for video production.
    \"\"\"
    return f"Video script: {article}"

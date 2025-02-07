import openai
from config import settings

openai.api_key = settings.OPENAI_API_KEY

def generate_oml_article(request):
    \"\"\"
    Generates an article chapter in OML style.
    \"\"\"
    prompt = f"Write a chapter {request.chapterNumber} on {request.subject} in OML style."
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )

    return response.choices[0]["message"]["content"]

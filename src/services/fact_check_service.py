import requests

def fact_check(content):
    \"\"\"
    Uses an external API to verify facts in the content.
    \"\"\"
    api_url = f"https://api.google.com/factcheck?q={content}"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    return {"error": "Fact-checking service unavailable"}

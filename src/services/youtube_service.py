import requests
from config import settings

YOUTUBE_API_URL = "https://www.googleapis.com/youtube/v3/search"

def get_channel_performance(channel_id: str):
    \"\"\"
    Fetches YouTube analytics for a channel.
    \"\"\"
    params = {
        "part": "snippet",
        "channelId": channel_id,
        "key": settings.YOUTUBE_API_KEY
    }

    response = requests.get(YOUTUBE_API_URL, params=params)
    if response.status_code == 200:
        return response.json()
    
    return {"error": "Failed to retrieve YouTube insights"}

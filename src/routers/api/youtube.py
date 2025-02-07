from fastapi import APIRouter, HTTPException, Depends
from services.youtube_service import get_channel_performance
from dependencies import get_current_active_user

router = APIRouter(prefix="/api/youtube", tags=["YouTube Insights"])

@router.get("/insights")
async def youtube_insights(channelId: str, user=Depends(get_current_active_user)):
    \"\"\"
    Fetches YouTube analytics for a given channel.
    \"\"\"
    insights = get_channel_performance(channelId)
    if not insights:
        raise HTTPException(status_code=500, detail="Failed to retrieve YouTube insights.")
    return insights,

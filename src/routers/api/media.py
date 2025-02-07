from fastapi import APIRouter, HTTPException, Depends
from services.media_service import generate_audio, generate_video_script
from schemas import MediaRequest, MediaResponse
from dependencies import get_current_active_user

router = APIRouter(prefix="/api/media", tags=["Media"])

@router.post("/generate")
async def generate_media(request: MediaRequest, user=Depends(get_current_active_user)):
    """
    Generates audio/video versions of an article.
    """
    if request.format == "mp3" or request.format == "wav":
        audio_url = generate_audio(request.completeArticle, request.format)
        return MediaResponse(audioVersion=audio_url, videoVersion=None)
    
    elif request.format == "mp4":
        video_script = generate_video_script(request.completeArticle)
        return MediaResponse(audioVersion=None, videoVersion=video_script)

    raise HTTPException(status_code=400, detail="Invalid media format. Choose 'mp3', 'wav', or 'mp4'.")

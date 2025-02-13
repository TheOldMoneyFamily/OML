from fastapi import APIRouter, HTTPException
from services.ai_service import generate_oml_article
from schemas import ChapterRequest, ChapterResponse

router = APIRouter(prefix="/api/articles", tags=["Articles"])

@router.post("/write")
async def write_article(request: ChapterRequest) -> ChapterResponse:
    result = generate_oml_article(request)
    if not result:
        raise HTTPException(status_code=500, detail="Article generation failed.")
    return result

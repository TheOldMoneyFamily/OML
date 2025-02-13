from fastapi import APIRouter, HTTPException
from services.fact_check_service import fact_check

router = APIRouter(prefix="/api/fact_check", tags=["Fact-Check"])

@router.post("/")
async def check_facts(content: str):
    result = fact_check(content)
    if not result:
        raise HTTPException(status_code=500, detail="Fact-checking failed.")
    return result

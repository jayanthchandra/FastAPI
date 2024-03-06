from typing import Annotated

from fastapi import APIRouter, Depends

from ...core.security import verify_token

router = APIRouter(tags=["sample"])

@router.get("/health")
async def health_check():
    return {"message": "OK"}

from fastapi import APIRouter

from .welder import router as welder_router


v1_router = APIRouter()
v1_router.include_router(welder_router, prefix="/v1", tags=["welders"])
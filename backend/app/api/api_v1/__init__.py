from fastapi import APIRouter

from .welder_endpoints import router as welder_router
from .ndt_endpoints import router as ndt_router


v1_router = APIRouter()
v1_router.include_router(welder_router, prefix="/v1", tags=["welders"])
v1_router.include_router(ndt_router, prefix="/v1", tags=["ndts"])
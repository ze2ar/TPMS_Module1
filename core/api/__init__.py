from fastapi import APIRouter

from .base_api import router as base_router


router = APIRouter()
router.include_router(base_router)

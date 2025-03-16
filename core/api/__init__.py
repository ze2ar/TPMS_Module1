from fastapi import APIRouter

from .base_api import router as base_router
from .task1_api import router as task1_router


router = APIRouter()
router.include_router(base_router)
router.include_router(task1_router)

from fastapi import APIRouter

from .base_api import router as base_router
from .task1_api import router as task1_router
from .task2_1_api import router as task2_1_router
from .task2_2_api import router as task2_2_router


router = APIRouter()
router.include_router(base_router)
router.include_router(task1_router)
router.include_router(task2_1_router)
router.include_router(task2_2_router)

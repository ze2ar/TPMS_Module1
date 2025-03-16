from fastapi import FastAPI

from core.api import router as api_router

app = FastAPI(title="TPMS (Module1) Service")
app.include_router(api_router)

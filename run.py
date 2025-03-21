import uvicorn

from core.settings import settings

uvicorn.run(
    app="core.app:app",
    host=settings.server_host,
    port=settings.server_port,
    reload=False,
)

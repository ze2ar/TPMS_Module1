from zoneinfo import ZoneInfo
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    server_host: str = "0.0.0.0"
    server_port: int = "8080"
    timezone: str = "Asia/Yekaterinburg"


settings = Settings(
    _env_file=".env",
    _env_file_encoding="utf-8",
)

timezone = ZoneInfo(settings.timezone)

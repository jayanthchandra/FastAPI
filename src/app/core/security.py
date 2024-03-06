from typing import Any, Literal

from .config import settings

async def verify_token(token: str) -> bool:
    return token == settings.token

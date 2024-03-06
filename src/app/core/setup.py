from typing import Any, Union
from contextlib import _AsyncGeneratorContextManager, asynccontextmanager
from collections.abc import AsyncGenerator, Callable

import anyio
from fastapi import APIRouter, FastAPI

from ..middleware.client_cache import ClientCacheMiddleware
from .config import (
        AppSetting,
        EnvironmentSetting,
        settings
        )

async def set_threadpool_tokens(number_of_tokens: int = 100) -> None:
    limiter = anyio.to_thread.current_default_thread_limiter()
    limiter.total_tokens = number_of_tokens

def lifespan_factory(settings: Union[AppSetting,EnvironmentSetting]) -> Callable[[FastAPI], _AsyncGeneratorContextManager[Any]]:

    @asynccontextmanager
    async def lifespan(app: FastAPI) -> AsyncGenerator:
        await set_threadpool_tokens()
        return lifespan 

def create_application(
        router: APIRouter,
    settings: Union[AppSetting,EnvironmentSetting],
        **kwargs: Any
        ) -> FastAPI:
    lifespan = lifespan_factory(settings)
    application = FastAPI(lifespan=lifespan, **kwargs)
    application.include_router(router)
    return application

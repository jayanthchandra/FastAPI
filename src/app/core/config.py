import os
from enum import Enum

from pydantic_settings import BaseSettings
from starlette.config import Config

current_file_dir = os.path.dirname(os.path.realpath(__file__))
env_path = os.path.join(current_file_dir, "..", "..", "..", ".env")
config = Config(env_path)

class AppSetting(BaseSettings):
    APP_NAME: str = config("APP_NAME", default="Klub AI")
    APP_VERSION: str = config("APP_VERSION", default="0.0.0")

class DefaultRateLimitSetting(BaseSettings):
    DEFAULT_RATE_LIMIT: int = config("DEFAULT_RATE_LIMIT", default=10)
    DEFAULT_RATE_LIMIT_PERIOD: int = config("DEFAULT_RATE_LIMIT", default=3600)

class CryptSetting(BaseSettings):
    SECRET_KEY: str = config("SECRET_KEY")

class EnvironmentOption(Enum):
    LOCAL = "local"
    STAGING = "stage"
    PRODUCTION = "prod"

class EnvironmentSetting(BaseSettings):
    ENVIRONMENT: EnvironmentOption = config("ENV", default="local")

class Settings(
        AppSetting,
        DefaultRateLimitSetting,
        EnvironmentSetting,
        ):
    pass

settings = Settings()

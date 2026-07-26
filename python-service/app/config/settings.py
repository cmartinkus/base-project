from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str
    LOG_LEVEL: str = "INFO"

    JOB1_ENABLED: bool = True
    JOB1_INTERVAL_SECONDS: int = 30

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

'''lru_cache ensures if get_settings() is called anywhere in the app, get_settings()
will only be run that one time. all settings objects will point to same object
in memory.'''
@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
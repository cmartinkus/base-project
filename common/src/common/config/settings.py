from functools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    APP_NAME: str
    LOG_LEVEL: str = "INFO"

    JOB1_ENABLED: bool = True
    JOB1_INTERVAL_SECONDS: int = 30

    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    @property
    def database_url(self):

        return (
            f"postgresql+psycopg://"
            f"{self.POSTGRES_USER}:"
            f"{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:"
            f"{self.POSTGRES_PORT}/"
            f"{self.POSTGRES_DB}"
        )

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

'''lru_cache ensures if get_settings() is called anywhere in the app, get_settings()
will only be run that one time. all settings objects will point to same object
in memory.'''
@lru_cache
def get_settings():
    return Settings()

settings = get_settings()
from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str

    LOG_LEVEL: str

    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DATABASE: str
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
            f"{self.POSTGRES_DATABASE}"
        )


@lru_cache
def get_settings():

    return Settings()


settings = get_settings()
from pydantic_settings import BaseSettings
from pydantic import BaseModel


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8080


class ApiPrefix(BaseModel):
    prefix: str = "/api"


class Settings(BaseSettings):
    run: RunConfig = RunConfig() #підтягує данні з клсу RunConfig
    api: ApiPrefix = ApiPrefix()


settings = Settings()
from fastapi import FastAPI
import uvicorn
from api import router as api_router #імполртуемо роутер з пакету api в основний додаток
from core.config import settings

app = FastAPI() # створення додатку
app.include_router( # підключення роутеру
    api_router,
    prefix=settings.api.prefix,
)

if __name__ == "__main__": #запускає додаток автоматично при зміні коду
    uvicorn.run(
        app = "main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
from fastapi import FastAPI
import uvicorn

app = FastAPI()


if __name__ == "__main__": #запускає додаток автоматично при зміні коду
    uvicorn.run(app = "main:app", reload=True)
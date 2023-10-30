from fastapi import FastAPI
import uvicorn 

from api import v1_router

app = FastAPI()


app.include_router(v1_router, prefix="/api")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
from typing import Union
from fastapi import FastAPI
from api.routes.routes import router as albums_router

app = FastAPI()
app.title = "Mac Miller API"


@app.get("/HelloWorld", tags=['Test'])
def read_root():
    return {"Hello": "World"}

# Montar el router de álbumes
app.include_router(albums_router, prefix="/albums", tags=["albums"])

# Ruta de inicio
@app.get("/")
def read_root():
    return {"message": "Welcome to the Mac Miller API!"}
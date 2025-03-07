from fastapi import FastAPI
from api.routes.routes import router as albums_router

app = FastAPI()
app.title = "Mac Miller API"


@app.get("/helloworld", tags=['Test'])
def read_root():
    return {"Hello": "World"}

# Montar el router de álbumes
app.include_router(albums_router, prefix="/albums", tags=["Albums"])

# Ruta de inicio
@app.get("/", tags=['Home'])    
def read_root():
    return {"message": "Welcome to the Mac Miller API!"}
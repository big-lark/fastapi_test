from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get("/compare")
def read_root():
    return {"Hello": "비교정보를!!"}

@app.get("/compare/home1")
def read_root():
    return {"Hello": "비교정보를!!home1"}

@app.get("/compare/home2")
def read_root():
    return {"Hello": "비교정보를!!home2"}

@app.get("/air")
def read_root():
    return {"Hello": "날씨정보를!"}

app.mount("/", StaticFiles(directory="public", html = True), name="static")



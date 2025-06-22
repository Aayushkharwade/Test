# main.py

from fastapi import FastAPI

app = FastAPI()

# Root route
@app.get("/")
def test():
    return {"message": "Welcome to FastAPI on Azure App Service!"}


@app.get("/new")
def new():
    return {"This is the new function"}


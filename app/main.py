from fastapi import FastAPI
from .routers import users

app = FastAPI()

app.include_router(users.router)

#hii there


@app.get("/")
def root():
    return {"message": "CRUD API is running 🚀"}


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


class UserCreate(BaseModel):
    user_id: str
    user_password: str


@app.post("/login/")
def login(login: UserCreate):
    user_id = login.user_id
    username = login.user_password
    return {
        "msg": "we got data succesfully",
        "user_id": user_id,
        "username": username,
    }

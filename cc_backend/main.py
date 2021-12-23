from fastapi import FastAPI
from cc_schemas.users import User
import logging

lg = logging.getLogger(__name__)

app = FastAPI()


@app.get("/")
def read_root():
    """Alive check"""
    return "alive"


@app.get("/user/{user_name}")
def read_user(user_name: str):
    """Return user information"""
    return {"item_name": user_name}


@app.post("/user")
def add_user(user: User):
    """Add a new user"""
    lg.info(user.json())
    return

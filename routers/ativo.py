
from typing import Union
from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter()

class user (BaseModel):
    name:str
    password:str

users = [
    user(name='Lucas',password='1234'),
    user(name='Guilherme',password ='4321')
]

@router.get('/')
def home():
    return ('Hello Word')

@router.get("/users/", tags=["users"])
def read_users():
    return users


@router.get("/users/{user.name}&{user.password}", tags=["users"])
def read_user_me():
    for user in users:
        user.name = {user.name},
        user.password = [user.password]



@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}
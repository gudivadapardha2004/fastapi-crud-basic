from pydantic import BaseModel

class Users(BaseModel):
    userID:str
    name:str
    age:int
    password:str

class UserCreate(BaseModel):
    name: str
    age: int
    password: str
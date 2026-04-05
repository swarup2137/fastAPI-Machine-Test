from pydantic import BaseModel
from typing import List

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class Login(BaseModel):
    email: str
    password: str

class ClientCreate(BaseModel):
    client_name: str

class ProjectCreate(BaseModel):
    project_name: str
    client_id: int
    users: List[int]
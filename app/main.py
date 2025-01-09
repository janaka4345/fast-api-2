from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None
    
class User(BaseModel):
    user_id:int
    name:str
    email:str

class DocumentEnum(str,Enum):
    policy="Policy"
    evidence="Evidence"
    
@app.get('/document/{document_type}')
async def document(document_type:DocumentEnum):
    if document_type==DocumentEnum.policy:
        return {"doc":DocumentEnum.policy}
    if document_type==DocumentEnum.evidence:
        return {"doc":DocumentEnum.evidence}
    return{"doc":'null'}
    

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None,h: Union[str, None] = None):
    return {"item_id": item_id, "q": q,"h":h}
  
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.get('/user/{user_id}')
async def get_user(user_id:int):
    user = {"user_id": user_id, "name": "John Doe", "email": "johndoe@example.com"}
    return user

@app.get('/list_users')
async def list_users():
    user = [
        {"user_id": 1, "name": "John Doe", "email": "johndoe@example.com"},
        {"user_id": 2, "name": "Jane Doe", "email": "janedoe@example.com"},
        {"user_id": 3, "name": "Alice Smith", "email": "alicesmith@example.com"}
    ]
    
    return user


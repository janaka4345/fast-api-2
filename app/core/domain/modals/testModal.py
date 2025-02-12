from pydantic import BaseModel
from typing import Union

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None
    
class User(BaseModel):
    user_id:int
    name:str
    email:str
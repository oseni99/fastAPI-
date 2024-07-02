from pydantic import BaseModel
from typing import List,Union



class Blog(BaseModel):
  title : str 
  body : str 
  class Config:
    from_attributes= True

class User(BaseModel):
  name:str
  email:str
  password:str

  class Config:
    from_attributes = True 

class ShowUser(BaseModel):
  name:str
  email:str
  blogs:List[Blog]

class ShowBlog(Blog):
  title:str
  body:str
  creator: ShowUser
  class Config:
    from_attributes= True

class Login(BaseModel):
  username:str
  password:str

  
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Union[str, None] = None
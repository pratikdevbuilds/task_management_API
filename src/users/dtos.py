from pydantic import BaseModel

class Userschema(BaseModel):
  name:str 
  username:str
  password:str
  email:str 
  mob:int


class Userschemareponse(BaseModel):
  id:int
  username:str
  email:str
  mob:int
  

class LoginSchema(BaseModel):
 
  username:str
  password:str
 
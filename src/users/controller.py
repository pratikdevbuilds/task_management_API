
from fastapi import HTTPException,status,Request
from src.users.dtos import Userschema,LoginSchema
from sqlalchemy .orm import session
from src.users.models import UserModel
from pwdlib import PasswordHash
from datetime import datetime,timedelta
from jwt import InvalidTokenError

from src.utils.setting import settings 

import jwt 

password_hash= PasswordHash.recommended()


def get_password_hash(password):
    return password_hash.hash(password)

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)


def register(body:Userschema,db:session):
  is_user = db.query(UserModel).filter(UserModel.username==body.username).first()
  
  if is_user:
    raise HTTPException(400,detail="Username already exist....")
  
  is_user = db.query(UserModel).filter(UserModel.email==body.email).first()
  
  if is_user:
      raise HTTPException(400,detail="email already exist....")
  
  is_user = db.query(UserModel).filter(UserModel.mob==body.mob).first()
  
  if is_user:
      raise HTTPException(400,detail="Mobile number already exist....")

  password_hash= get_password_hash(body.password)

  new_user= UserModel(
    name=body.name,
  username=body.username,
  hash_password = password_hash,
  email=body.email,
  mob=body.mob
  )

  db.add(new_user)
  db.commit()
  db.refresh(new_user)

  return new_user


def login_user(body:LoginSchema,db:session):
  user = db.query(UserModel).filter(UserModel.username==body.username).first()
  
  if not user:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Username not exist....")
  
  if not verify_password(body.password,user.hash_password):
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="password didn't  match....")
 
  exp_tm = datetime.now()+timedelta(minutes=settings.EXP_TIME)
  
  token =jwt.encode({"id":user.id,"exp":exp_tm.timestamp()},settings.SECRET_KEY,settings.ALGORITHM)
  
  print(token)
  return {"token":token}



def user_authorization(request:Request,db:session):
  try :  
      token  = request.headers.get("authorization")
      if  not token:
          raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="you anauthorized")
      
      token = token.split(" ")[-1]
      
      data = jwt.decode(token,settings.SECRET_KEY,settings.ALGORITHM)
      user_id = data.get("id")
      
      user = db.query(UserModel).filter(UserModel.id==user_id).first()
      if not user :
          raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="you an authorized ")
        
      return  user
  except InvalidTokenError:
          raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="you an authorized ")
     
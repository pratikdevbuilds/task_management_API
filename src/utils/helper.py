from fastapi import Request,HTTPException,status,Depends
import jwt
from jwt.exceptions import InvalidTokenError
from src.utils.setting import settings 
from src.users.models import UserModel 
from sqlalchemy.orm import session

from src.utils.db import get_db




def user_authorization(request:Request,db:session=Depends(get_db)):
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
     

 
     
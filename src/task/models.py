from sqlalchemy import Column,Integer,Boolean,Float,String
from src.utils.db import Base


class TaskModel(Base):
  __tablename__="User_Tasks"
  id = Column(Integer,primary_key="True")
  title = Column(String)
  description=Column(String)
  is_completed=Column(Boolean,default="False")
from src.task.dtos import TaskSchema
from sqlalchemy .orm import  session
from src.task.models import TaskModel
from fastapi import HTTPException
from src.users.models import UserModel

def create_task(body:TaskSchema,db:session,user:UserModel):
  data=body.model_dump()
  new_task=TaskModel(title = data["title"],
                     description=data["description"],
                       is_completed=data["is_completed"],
                       user_id = user.id)
  db.add(new_task)
  db.commit()
  db.refresh(new_task)
  return new_task 
  

def get_tasks(db:session,user:UserModel):
  tasks =db.query(TaskModel).filter(user.id == TaskModel.user_id).all()
  return{"status":"ALL Tasks","data":tasks} 


def get_taskby_ones(task_id:int,db:session,user:UserModel):
  ones_task= db.query(TaskModel).filter(TaskModel.id==user.id).get(task_id)
  if not ones_task:
    raise HTTPException(404,detail="Task id is not available" )
  return {"status":"the Task Fetched","data":ones_task}


def update_task(body:TaskSchema,task_id:int,db:session,user:UserModel):
  #  new_task= db.query(TaskModel).get(task_id)
   new_task:TaskModel=db.get(TaskModel, task_id)
 
   if not new_task:
    raise HTTPException(404,detail="Task id is not available" )
   
   if new_task.user_id != user.id:
    
    raise HTTPException(401,detail="you are not allow to chenges" )
     
     
     
    
  #  new_task.title = body.title
  #  new_task.description = body.description
  #  new_task.is_completed =  body.is_completed
   body = body.model_dump()
   for field,value in body.items():
      
     setattr(new_task,field,value)
   

   db.add(new_task)
   db.commit()
   db.refresh(new_task)
   return {"status":"the Task Fetched and updated ","data":new_task}

def del_task(task_id:int,db:session,user:UserModel):
  del_data = db.get(TaskModel,task_id)
  
  if del_data.user_id != user.id:
    
    raise HTTPException(401,detail="you are not allow to delete this task " )

  if not del_data:
    raise HTTPException(404,detail="Task id or data is not available" )
  
  db.delete(del_data)
  db.commit()
  # return {"status":"The Task Deleted Successfully" }
  return None





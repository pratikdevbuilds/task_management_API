from src.task.dtos import TaskSchema
from sqlalchemy .orm import  session
from src.task.models import TaskModel
from fastapi import HTTPException

def create_task(body:TaskSchema,db:session):
  data=body.model_dump()
  new_task=TaskModel(title = data["title"],
                     description=data["description"],
                       is_completed=data["is_completed"])
  db.add(new_task)
  db.commit()
  db.refresh(new_task)
  return new_task 
  

def get_tasks(db:session):
  tasks =db.query(TaskModel).all()
  return{"status":"ALL Tasks","data":tasks}


def get_taskby_ones(task_id:int,db:session):
  ones_task= db.query(TaskModel).get(task_id)
  if not ones_task:
    raise HTTPException(404,detail="Task id is not available" )
  return {"status":"the Task Fetched","data":ones_task}


def update_task(body:TaskSchema,task_id:int,db:session):
  #  new_task= db.query(TaskModel).get(task_id)
   new_task=db.get(TaskModel, task_id)
   if not new_task:
    raise HTTPException(404,detail="Task id is not available" )
    
  #  new_task.title = body.title
  #  new_task.description = body.description
  #  new_task.is_completed =  body.is_completed
   body = body.model_dump()
   for field,value in body.items():
     print(field)
     setattr(new_task,field,value)
   

   db.add(new_task)
   db.commit()
   db.refresh(new_task)
   return {"status":"the Task Fetched and updated ","data":new_task}

def del_task(task_id:int,db:session):
  del_data = db.get(TaskModel,task_id)
  if not del_data:
    raise HTTPException(404,detail="Task id or data is not available" )
  db.delete(del_data)
  db.commit()
  # return {"status":"The Task Deleted Successfully" }
  return None





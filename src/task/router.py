from fastapi import APIRouter,Depends,status
from src.task import controller
from src.task.dtos import TaskSchema,TaskresponseSchema
from src.utils.db import get_db
from src.utils.helper import user_authorization
from src.users.models import UserModel


task_routes = APIRouter(prefix="/tasks")
@task_routes.post("/create",response_model=TaskresponseSchema,status_code=status.HTTP_201_CREATED)
def create_task(body:TaskSchema,db=Depends(get_db),user:UserModel=Depends(user_authorization)):
  return controller.create_task(body,db,user)
 

@task_routes.get("/all_task",status_code=status.HTTP_200_OK)
def get_all_task(db=Depends(get_db),user:UserModel=Depends(user_authorization)): 
  return controller.get_tasks(db)



@task_routes.get("/by_ones/{task_id}",status_code=status.HTTP_200_OK)
def get_taskby_ones(task_id:int,db=Depends(get_db),user:UserModel=Depends(user_authorization)):
  return controller.get_taskby_ones(task_id,db)



@task_routes.put("/changes/{task_id}",status_code=status.HTTP_201_CREATED)
def update_task(body:TaskSchema,task_id:int,db=Depends(get_db)):
  return controller.update_task(body,task_id,db)



@task_routes.delete("/delet_data/{task_id}",status_code=status.HTTP_204_NO_CONTENT)
def del_task(task_id:int,db=Depends(get_db),user:UserModel=Depends(user_authorization)):
  return controller.del_task(task_id,db)
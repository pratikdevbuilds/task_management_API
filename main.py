from fastapi import FastAPI
from src.utils.db import Base,engine
# from src.task.models import TaskModel

 

from src.task.router import task_routes
from src.users.router import user_routes
 
Base.metadata.create_all(engine)

app = FastAPI(title="this is my task project")
app.include_router(task_routes)
app.include_router(user_routes)

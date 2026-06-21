from pydantic import BaseModel

class TaskSchema(BaseModel):
   title:str
   description:str
   is_completed :bool = False

class TaskresponseSchema(BaseModel):
   id :int
   title:str
   description:str
   is_completed :bool
   model_config = {
        "from_attributes": True
    } 
   user_id :int |None =0
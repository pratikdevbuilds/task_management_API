# file upload
from fastapi import File,UploadFile,File,HTTPException,APIRouter
from fastapi . staticfiles import StaticFiles
from src.utils.db import Base,engine
import os 
import shutil

files_rout = APIRouter(prefix="/file")
#  step 1 :if folder not exist so, i create as well as :
UPLOAD_DIR = "upload"
if not os.path.exists (UPLOAD_DIR):
  os.makedirs(UPLOAD_DIR)

# step2 :static file set-up:
files_rout.mount("/files",StaticFiles(directory=UPLOAD_DIR),name="files")
# step 3 upload file api
@files_rout.post("/upload")
def upload_file(file:UploadFile=File(...)):
  filename =file.filename
  file_path = os.path.join(UPLOAD_DIR,filename)


  if not filename:
    raise HTTPException(status_code=400,detail="file not selected")
  

  with open (file_path,"wb") as buffer:
     shutil.copyfileobj(file.file,buffer)

     return{
       "massage":"file uplaoded successfully ",
       "fileName":filename,
       "fileUrl":f"http://127.0.0.1:8000/files/{filename}"
     }
  
# step 4 Get file URL API

@files_rout.get("/files/{filename}")
def get_file(filename:str):
  file_path =os.path.join(UPLOAD_DIR,filename) 
  if not os.path.exists(file_path):
      raise HTTPException(status_code=404,detail="file not found") 
  return{
     "fileUrl" :f"http://127.0.0.1:8000/files/{filename}"
  }

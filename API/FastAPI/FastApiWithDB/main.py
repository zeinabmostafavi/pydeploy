from fastapi import FastAPI,File,Form,UploadFile,HTTPException
from fastapi.responses import StreamingResponse
import numpy as np
import io
from Database import Database

app=FastAPI()
tasks= Database()


@app.get("/")
def read_root():
    return{"Hello":"World"}

@app.get("/items")
def read_tasks():
    response=tasks.select()
    return response

@app.post("/items")
#id,title,desceription,time,status
def add_task(id:int = Form() , title:str=Form(),desceription:str=Form(),time:int=Form(), status:bool=Form()):
    response = tasks.insert(id,title,desceription,time,status)
    return response


@app.delete("/items/{id}")
def remove_task(id:str):
    response = tasks.delete(id)
    if response == True:
        return response,{"message": "Item deleted"}
    if response == False:
        raise HTTPException(status_code=400 , detail="this id does not exists ")

        


@app.put("/items/{id}")
def update_friend(id:int):
    response = tasks.edit(id)
    if response == True:
        return response,{"message": "Item updated"}
    if response == False:
        raise HTTPException(status_code=400 , detail="this id does not exists ")

    
    

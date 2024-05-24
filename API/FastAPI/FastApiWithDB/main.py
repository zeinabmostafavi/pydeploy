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
    
    
    return response,{"message": "Item deleted"}
    




@app.put("/items/{id}")
def update_friend(id:int , title:str=Form(),desceription:str=Form(),time:int=Form(), status:bool=Form()):
    # if id not in friends:
    #     raise HTTPException(status_code=404 , dtail="item not found")
    if title is not None:
        tasks.edit(title={title})
        print('edit')
    if desceription is not None:
        tasks.edit(desceription={desceription})
    if time is not None:
        tasks.edit(time={time})
    if status is not None:
        tasks.edit(status={status})

    response = tasks.edit(id,title,desceription,time,status)
    
    
    return response,{"message": "Item uptaded"}

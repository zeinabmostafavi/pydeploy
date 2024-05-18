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
def read_friends():
    response=tasks.select()
    return response

@app.post("/items")
#id,title,desceription,time,status
def add_friend(id:int = Form() , title:str=Form(),desceription:str=Form(),time:int=Form(), status:bool=Form()):
    response = tasks.insert(id,title,desceription,time,status)
    
    return response


# @app.delete("/items/{id}")
# def remove_friend(id:str):
#     if id not in friends:
#         raise HTTPException(status_code=404,detail="Item not found")                                                          
#     del friends[id]
#     return {"message": "Item deleted"}
    




# @app.put("/items/{id}")
# def update_friend(id:str,name:str=Form(None),age:float=Form(None)):
#     if id not in friends:
#         raise HTTPException(status_code=404 , dtail="item not found")
#     if name is not None:
#         friends[id]["name"]=name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
#     if age is not None:
#         friends[id]["age"]= age
    
#     return friends[id]
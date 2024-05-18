from fastapi import FastAPI,File,Form,UploadFile,HTTPException
from fastapi.responses import StreamingResponse
import numpy as np
import io

app=FastAPI()
friends={}

@app.get("/")
def read_root():
    return{"Hello":"World"}

@app.get("/items")
def read_friends():
    return friends

@app.post("/items")
def add_friend(id:str = Form() , name:str=Form(),age:float=Form()):
    friends[id]={"name": name, "age":age}
    return friends[id]


@app.delete("/items/{id}")
def remove_friend(id:str):
    if id not in friends:
        raise HTTPException(status_code=404,detail="Item not found")                                                          
    del friends[id]
    return {"message": "Item deleted"}
    




@app.put("/items/{id}")
def update_friend(id:str,name:str=Form(None),age:float=Form(None)):
    if id not in friends:
        raise HTTPException(status_code=404 , dtail="item not found")
    if name is not None:
        friends[id]["name"]=name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    if age is not None:
        friends[id]["age"]= age
    
    return friends[id]
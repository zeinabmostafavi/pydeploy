import cv2
from fastapi import FastAPI , HTTPException , status
from fastapi.responses import StreamingResponse , FileResponse
import io
import numpy 


# uvicorn main:app --reload
# seven_sin={
#  'سیب':{"descrip":" سیب نماد سلامتی، زندگی و زیبایی است","img":"assets\sib.jpeg"},
# "سماق" :{"descrip":" سماق نماد زیبایی و شادابی است"     ,"img":"assets\somagh.jpeg"},
#  "سیر" :{"descrip":" سیر نماد سلامتی و درمان بیماری‌هاست","img":"assets\sir.jpeg"},
#  "سکه" :{"descrip":" سکه نشان‌دهنده فراوانی، برکت، توفیق و ثروت است","img":"assets\seke.jpeg"},
# "سمنو" :{"descrip":" سمنو نماد عشق و محبت در سفره هفت سین است","img":"assets\samanoo.jpeg"},
# "سبزه" :{"descrip":" سبزه یکی از مهم‌ترین نمادهای سفره هفت سین است که بهار و زندگی را نشان می‌دهد","img":"assets\sabze.jpeg"},
# "سرکه" :{"descrip":" سرکه نماد زندگی و بردباری در برابر مشکلات محسوب می‌شود","img":"assets\serke.jpeg"}
#  }

app=FastAPI()

@app.get("/")
def read_root():
    return "Hi! Welcome to my API. The API provides information for Haft Sin (Haft Seen) is a traditional custom in the New Year holiday of Iranian known as Nowruz. Actually it is a table setting with 7 different items which its essential items letters start with."

@app.get("/sins")
def name():
    return ' سرکه'+ ' سبزه'+' سمنو'+ ' سکه'+' سیر'+ ' سماق'+' سیب'
   
@app.get("/sins/{sin_name}")
def information(sin_name:str):
     if sin_name == "sib" :
            return " سیب نماد سلامتی، زندگی و زیبایی است"
     if sin_name == "somagh" :
            return " سماق نماد زیبایی و شادابی است"
     if sin_name == "sir" :
            return "سیر نماد سلامتی و درمان بیماری‌هاست"
     if sin_name == "seke" :
            return " سکه نشان‌دهنده فراوانی، برکت، توفیق و ثروت است"
     if sin_name == "samanoo" :
            return "سمنو نماد عشق و محبت در سفره هفت سین است"
     if sin_name == "sabzeh" :
            return " سبزه یکی از مهم‌ترین نمادهای سفره هفت سین است که بهار و زندگی را نشان می‌دهد"
     if sin_name == "serke" :
            return "سرکه نماد زندگی و بردباری در برابر مشکلات محسوب می‌شود"
     else:
       raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="NOT FOUND ITEM")


@app.get("/sins/{sin_name}/image")
def image(sin_name:str):
     if sin_name == "sib"  :
            image = cv2.imread("assets\sib.jpeg")      
            _, encode_image = cv2.imencode(".png",image)
            return StreamingResponse(content=io.BytesIO(encode_image.tobytes()), media_type = "image/png")
     if sin_name == "somagh" :
            image = cv2.imread("assets\somagh.jpeg")      
            _, encode_image = cv2.imencode(".png",image)
            return StreamingResponse(content=io.BytesIO(encode_image.tobytes()), media_type = "image/png")     
     if sin_name == "sir" :
            image = cv2.imread("assets\sir.jpeg")      
            _, encode_image = cv2.imencode(".png",image)
            return StreamingResponse(content=io.BytesIO(encode_image.tobytes()), media_type = "image/png")     
     if sin_name == "seke" :
            image = cv2.imread("assets\seke.jpeg")      
            _, encode_image = cv2.imencode(".png",image)
            return StreamingResponse(content=io.BytesIO(encode_image.tobytes()), media_type = "image/png")     
     if sin_name == "samanoo" :
            image = cv2.imread("assets\samanoo.jpeg")      
            _, encode_image = cv2.imencode(".png",image)
            return StreamingResponse(content=io.BytesIO(encode_image.tobytes()), media_type = "image/png")     
     if sin_name == "sabzeh" :
            image = cv2.imread("assets\sabze.jpeg")      
            _, encode_image = cv2.imencode(".png",image)
            return StreamingResponse(content=io.BytesIO(encode_image.tobytes()), media_type = "image/png")     
     if sin_name == "serke" :
            image = cv2.imread("assets\serke.jpeg")      
            _, encode_image = cv2.imencode(".png",image)
            return StreamingResponse(content=io.BytesIO(encode_image.tobytes()), media_type = "image/png")     
     else:
       raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="NOT FOUND ITEM")



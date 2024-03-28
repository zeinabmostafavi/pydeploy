import cv2
from fastapi import FastAPI , HTTPException , status
from fastapi.responses import StreamingResponse , FileResponse
import io
import numpy 


# uvicorn main:app --reload
# seven_sin={
#  'سیب':{"descrip":" سیب نماد سلامتی، زندگی و زیبایی است","img":"images\sib.jpeg"},
# "سماق" :{"descrip":" سماق نماد زیبایی و شادابی است"     ,"img":"images\somagh.jpeg"},
#  "سیر" :{"descrip":" سیر نماد سلامتی و درمان بیماری‌هاست","img":"images\sir.jpeg"},
#  "سکه" :{"descrip":" سکه نشان‌دهنده فراوانی، برکت، توفیق و ثروت است","img":"images\seke.jpeg"},
# "سمنو" :{"descrip":" سمنو نماد عشق و محبت در سفره هفت سین است","img":"images\samanoo.jpeg"},
# "سبزه" :{"descrip":" سبزه یکی از مهم‌ترین نمادهای سفره هفت سین است که بهار و زندگی را نشان می‌دهد","img":"images\sabze.jpeg"},
# "سرکه" :{"descrip":" سرکه نماد زندگی و بردباری در برابر مشکلات محسوب می‌شود","img":"images\serke.jpeg"}
#  }

app=FastAPI()

@app.get("/")
def read_root():
    return "Hi! Welcome to my API. The API provides information for Haft Sin (Haft Seen) is a traditional custom in the New Year holiday of Iranian known as Nowruz. Actually it is a table setting with 7 different items which its essential items letters start with."

@app.get("/planets")

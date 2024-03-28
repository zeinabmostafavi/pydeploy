import cv2
from fastapi import FastAPI , HTTPException , status
from fastapi.responses import StreamingResponse , FileResponse
import io
import numpy 



@app.get("/")
def read_root():
    return "Hi! Welcome to my API.The Solar System API provides information for thousands of all solar system planets and their moons."

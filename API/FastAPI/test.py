from fastapi import FastAPI

app = FastAPI()


@app.get("/zeinab")
def read_root():
    return {"Hello": "World"}


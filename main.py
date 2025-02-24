from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/about")
def about():
    return {"info": "This is an API built with FastAPI"}

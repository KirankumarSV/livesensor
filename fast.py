from fastapi import FastAPI


app = FastAPI()


@app.get("/hello")
async def root():
    return "Hi. This is an hello endpoint"


@app.get("/")
async def root():
    return "Welcome to Kiran's test page"


@app.get("/items/{item_id}")
async def read_item(item_id : int):
    return {"item_id": item_id}
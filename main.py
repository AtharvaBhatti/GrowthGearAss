from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from helper import pseudo_SQL,explain,validator

app = FastAPI()

class topicModel(BaseModel):
    topic:str

@app.get("/")
async def read_root():
    return {"Hello": "World"}
    

@app.post("/query")

async def recieve_task(taskData: topicModel):
    try:
        task = taskData.topic
        query = pseudo_SQL(task)
        return {"query" : query}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@app.get("/explain")
async def explanation(taskData: topicModel):
    try:
        task = taskData.topic
        query = pseudo_SQL(task)
        expl = explain(task, query)
        return {"explanation" : expl}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@app.post("/validate")
async def validate_task(taskData: topicModel):
    try:
        task = taskData.topic
        query = pseudo_SQL(task)
        val = validator(query)
        return {"validation" : val}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
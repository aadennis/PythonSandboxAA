from fastapi import FastAPI, Body
from pydantic import BaseModel

# uvicorn --log-level debug whisky04:app --reload
# command line - OK
# echo '{"whisky": {"name": "Dewars", "age": 10}, "quality": 1}' | http POST http://localhost:8000/whisky4
# command line - bad...
# echo '{"whisky": {"name": "Dewars", "age": 10}, "quality": 5}' | http POST http://localhost:8000/whisky4

class Whisky(BaseModel):
    name: str
    age: int


app = FastAPI()


@app.post("/whisky4")
async def create_whisky(whisky: Whisky, quality: int = Body(..., ge=1, le=3)):
    return {"whisky": whisky, "quality": quality}


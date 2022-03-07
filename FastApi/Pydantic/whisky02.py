from fastapi import FastAPI
from pydantic import BaseModel

# uvicorn --log-level debug whisky02:app --reload
# echo '{"name": "Dewars", "age": 10}' | http POST http://localhost:8000/whisky2


class User(BaseModel):
    name: str
    age: int


app = FastAPI()


@app.post("/whisky2")
async def create_whisky(user: User):
    return user

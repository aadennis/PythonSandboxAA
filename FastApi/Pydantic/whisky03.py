from fastapi import FastAPI
from pydantic import BaseModel

# uvicorn --log-level debug whisky03:app --reload
# echo '{"user": {"name": "Old Blend", "age": 20}, "company": {"name": "MacCallan"}}' | http POST http://localhost:8000/whisky3

class User(BaseModel):
    name: str
    age: int


class Company(BaseModel):
    name: str


app = FastAPI()


@app.post("/whisky3")
async def create_whisky(user: User, company: Company):
    return {"user": user, "company": company}

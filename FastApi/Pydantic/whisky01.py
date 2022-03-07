from fastapi import FastAPI, Body

app = FastAPI()

# uvicorn --log-level debug whisky01:app --reload
# echo '{"name": "Dewars", "age": 10}' | http POST http://localhost:8000/whisky1

@app.post("/whisky1")
async def create_whisky(name: str = Body(...), age: int = Body(...)):
    return {"name": name, "age": age}

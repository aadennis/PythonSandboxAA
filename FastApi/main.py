"""
# https://fastapi.tiangolo.com/tutorial/first-steps/#first-steps
# https://mockaroo.com/
# PYTHONPATH=~/git/aadennis/PythonSandboxAA
# cd $PYTHONPATH/FastApi
# uvicorn main:app --reload
# http://127.0.0.1:8000
# https://eugeneyan.com/writing/how-to-set-up-html-app-with-fastapi-jinja-forms-templates/#now-lets-make-it-serve-html
# https://python-poetry.org/docs/#installation
"""

from fastapi import FastAPI, Request, APIRouter, Form
from fastapi.templating import Jinja2Templates
import model

app = FastAPI()
api_router = APIRouter()

templates = Jinja2Templates(directory="templates/")
data = model.load_people()

@app.get("/form")
def form_post(request: Request):
    """
    Render the chunk of fake json data within a Form.
    No BootStrap etc yet - just a quick POC.
    """
    # http://127.0.0.1:8000/form
    return templates.TemplateResponse('index.html', context={'request': request, 'result': data})




@app.post("/form")
async def form_post(request: Request, item_idx: str = Form(...), action: str = Form(...)): 

    a = {"id":item_idx,"first_name":"Didier","last_name":"Clique","email":"didier@radio.fr","ip_address":"56.123.149.96","trade":"Hock Taster"}

    data.append(a)
    if action == 'Save':
        model.save_people(data)

    return templates.TemplateResponse('index.html', context={'request': request, 'result': data})


@app.get('/')
def root(request: Request) -> dict:
    return templates.TemplateResponse(
        'index.html',
        {'request': request, 'result': data} 
    )

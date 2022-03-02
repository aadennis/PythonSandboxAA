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


from fastapi import FastAPI, Request, APIRouter
from fastapi.templating import Jinja2Templates
from model import data


app = FastAPI()
api_router = APIRouter()

templates = Jinja2Templates(directory="templates/")

# @app.get("/")
# async def root():
#     """
#     Render the chunk of fake json data
#     """
#     return data

@app.get("/form")
def form_post(request: Request):
    """
    Render the chunk of fake json data within a Form.
    No BootStrap etc yet - just a quick POC.
    """
    # http://127.0.0.1:8000/form
    return templates.TemplateResponse('index.html', context={'request': request, 'result': data})


@app.get('/')
def root(request: Request) -> dict:
    return templates.TemplateResponse(
        'index.html',
        {'request': request, 'result': data} 
    )

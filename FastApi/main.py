"""
# https://fastapi.tiangolo.com/tutorial/first-steps/#first-steps
# https://mockaroo.com/
# PYTHONPATH=~/git/PythonSandbox
# cd $PYTHONPATH/FastApi
# uvicorn main:app --reload
# http://127.0.0.1:8000
# https://eugeneyan.com/writing/how-to-set-up-html-app-with-fastapi-jinja-forms-templates/#now-lets-make-it-serve-html
# https://python-poetry.org/docs/#installation
"""


from fastapi import FastAPI, Request, APIRouter
from fastapi.templating import Jinja2Templates


app = FastAPI()
api_router = APIRouter()

templates = Jinja2Templates(directory="templates/")
data = [
    {"id":1,"first_name":"Layla","last_name":"Cohn","email":"lcohn0@g.co",
        "ip_address":"229.77.172.67","trade":"Equipment Operator"},
    {"id":2,"first_name":"Padget","last_name":"Bourbon","email":"pbourbon1@usatoday.com",
        "ip_address":"216.136.157.57","trade":"Millwright"},
    {"id":3,"first_name":"Jake","last_name":"Ecclestone","email":"jecclestone2@liveinternet.ru",
        "ip_address":"155.255.88.47","trade":"Plumber"},
    {"id":4,"first_name":"Adair","last_name":"Worgen","email":"aworgen3@ucoz.ru",
        "ip_address":"82.192.233.142","trade":"Carpenter"},
    {"id":5,"first_name":"Ellsworth","last_name":"McCarlich","email":"emccarlich4@mit.edu",
        "ip_address":"43.123.149.96","trade":"Plasterers"}]

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

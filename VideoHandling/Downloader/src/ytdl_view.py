# Windows (Powershell)
# cd d:\Sandbox\git\aadennis\
# .\virtualenvs\venv\Scripts\activate (Windows)
# source .\virtualenvs\venv\Scripts\activate (Git Bash on Windows)
# cd .\PythonSandboxAA\VideoHandling\Downloader
# uvicorn src.ytdl_view:app --reload
# http://127.0.0.1:8000/video
# Testing:
# My own Youtube video (6mb) is here: FFs4JIUbXJU
# https://github.com/tiangolo/fastapi/issues/854

from typing import Optional
from urllib import response
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse, Response
from fastapi.staticfiles import StaticFiles

from src.ytdl_model import save_video

app = FastAPI()
templates = Jinja2Templates(directory='src/templates/')

app.mount("/static", app = StaticFiles(directory="static"), name="static")

@app.get('/')
def read_form():
    return 'video download'

@app.get('/video')
def form_post(request: Request):
    results = ['Waiting for you to press [Download]...']
    return templates.TemplateResponse('ytdl.html', context={'request': request, 'result': results})

async def app2(scope, receive, send):
    assert scope['type'] == 'http'
    response = FileResponse('static/favicon.ico')
    await response(scope, receive, send)

@app.post('/video')
async def form_post(request: Request, action: str = Form(...), 
    video_code: Optional[str] = Form(None), sub_folder: Optional[str] = Form(None), single_or_list: str = Form(...)):
    if action == 'Download':
        results = save_video(video_code, single_or_list, sub_folder)
        return templates.TemplateResponse('ytdl.html', context={'request': request, 'result': results})
        


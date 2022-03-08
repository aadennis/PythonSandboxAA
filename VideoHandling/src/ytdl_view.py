# Windows (Powershell)
# cd .\Sandbox\git\aadennis\
# .\virtualenvs\venv\Scripts\activate (Windows)
# source .\virtualenvs\venv\Scripts\activate (Git Bash on Windows)
# cd .\PythonSandboxAA\TideTimes\
# uvicorn src.tidetimes:app --reload
# http://127.0.0.1:8000/tidetimes


from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse

from src.ytdl_model import save_video

app = FastAPI()
templates = Jinja2Templates(directory='src/templates/')


def save_to_text(content, filename):
    filepath = f'data/{filename}.txt'
    with open(filepath, 'w') as f:
        f.write(content)
    return filepath


@app.get('/')
def read_form():
    return 'video download'

@app.get('/video')
def form_post(request: Request):
    result = 'n/a'
    return templates.TemplateResponse('ytdl.html', context={'request': request, 'result': result})

@app.post('/video')
async def form_post(request: Request, action: str = Form(...)):
    if action == 'Save':
        file_path = save_video()
        result = 'button pressed'
        return templates.TemplateResponse('ytdl.html', context={'request': request, 'result': result})
        
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

from src.model import save_tide

app = FastAPI()
templates = Jinja2Templates(directory='templates/')


def save_to_text(content, filename):
    filepath = f'data/{filename}.txt'
    with open(filepath, 'w') as f:
        f.write(content)
    return filepath


@app.get('/')
def read_form():
    return 'tide times'

@app.get('/tidetimes')
def form_post(request: Request):
    result = 'n/a'
    return templates.TemplateResponse('tidetimes.html', context={'request': request, 'result': result})

@app.post('/tidetimes')
def form_post(request: Request, is_high_tide: bool = Form(False),
tide_1: int = Form(...), tide_2: int = Form(...), tide_3: int = Form(...), tide_4: int = Form(...),
tide_date: str = Form(...), tide_file: str = Form(...), action: str = Form(...)):
    if action == 'save':
        file_path = save_tide(tide_1, tide_2, tide_3, tide_4, tide_date, is_high_tide, tide_file)
        return FileResponse(file_path, media_type='application/octet-stream', filename=tide_file.format(tide_1))
        
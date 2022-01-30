from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse

from src.model import double_number

app = FastAPI()
templates = Jinja2Templates(directory='templates/')


def save_to_text(content, filename):
    filepath = 'data/{}.txt'.format(filename)
    with open(filepath, 'w') as f:
        f.write(content)
    return filepath


@app.get('/')
def read_form():
    return 'tide times'

@app.get('/form')
def form_post(request: Request):
    result = 'Type a number'
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})


@app.post('/form')
def form_post(request: Request, num: int = Form(...)):
    result = double_number(num)
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result, 'num': num})


@app.get('/checkbox')
def form_post(request: Request):
    result = 'Type a number'
    return templates.TemplateResponse('checkbox.html', context={'request': request, 'result': result})


@app.post('/checkbox')
def form_post(request: Request, num: int = Form(...), multiply_by_2: bool = Form(False)):
    result = double_number(num, multiply_by_2)
    return templates.TemplateResponse('checkbox.html', context={'request': request, 'result': result, 'num': num})


@app.get('/tidetimes')
def form_post(request: Request):
    result = 'Type a number'
    return templates.TemplateResponse('tidetimes.html', context={'request': request, 'result': result})


@app.post('/tidetimes')
def form_post(request: Request, is_high_tide: bool = Form(False),
tide_1: int = Form(...), tide_2: int = Form(...), tide_3: int = Form(...), tide_4: int = Form(...),
tide_date: str = Form(...), action: str = Form(...)):
    if action == 'convert':
        result = double_number(tide_1, tide_2, tide_3, tide_4, is_high_tide, tide_date)
        return templates.TemplateResponse('tidetimes.html', context={'request': request, 'result': result, 'tide_1': tide_1})
    elif action == 'save':
        print("Saved this I did")
        # Requires aiofiles
        result = double_number(tide_1, tide_2, tide_3, tide_4, is_high_tide, tide_date)
        filepath = save_to_text(result, tide_1)
        return FileResponse(filepath, media_type='application/octet-stream', filename='{}.txt'.format(tide_1))
        
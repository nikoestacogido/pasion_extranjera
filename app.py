from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI()

templates = Jinja2Templates(directory = "templates")

@app.get("/", response_class = HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

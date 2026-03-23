from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from database_func import getTeamFeature
from api_manager import getPlayers

app = FastAPI()

templates = Jinja2Templates(directory = "templates")

@app.get("/", response_class = HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

class teamData:
    def __init__(self):
        self.name = "None"
        self.badge = "None"
        self.players = []

class nextMatch:
    def __init__(self):
        self.home = "None"
        self.away = "None"
        self.time = "None"

@app.get("/team/{team_id}", response_class = HTMLResponse)
def team_page(request: Request, team_id: int):
    team_name = getTeamFeature("name", team_id)[0]
    opponent_name = getTeamFeature("nextmatch", team_id)[0]
    next_match = nextMatch()
    if getTeamFeature("condition", team_id)[0] == "Home":
        next_match.home = team_name
        next_match.away = opponent_name
    else:
        next_match.home = opponent_name
        next_match.away = team_name
    next_match.time = getTeamFeature("matchtime", team_id)[0]
    team_data = teamData()
    team_data.name = team_name
    team_data.players = getPlayers(team_id)

    return templates.TemplateResponse("team.html", {
        "request": request,
        "team": team_data,
        "nextMatch": next_match
    })
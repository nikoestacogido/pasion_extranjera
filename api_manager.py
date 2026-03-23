# API KEY 507e730cb209ad0f97228d13ee84d748
# Aca manejo todo lo que se comunica con la API, y de aca salen funciones corte getmatches()
import time
import requests
import os
from database_func import getTeamsFeature, getTeamFeature

API_KEY = os.environ["FOOTBALL_API_KEY"]
headers = { "X-Auth-Token": API_KEY }
params = {
    "status": "SCHEDULED",
    "limit": 1
}

def getMatches(ids): # All matches envolving the few teams
    matches = []
    for team in ids:
        match = []
        time.sleep(5)
        id = team
        url = f"https://api.football-data.org/v4/teams/{id}/matches"
        response = requests.get(url, headers = headers, params = params)
        data = response.json()
        home = True
        if data["matches"][0]["awayTeam"]["name"] == getTeamFeature("name", id)[0]: home = False
        match.append(id)
        match.append(data["matches"][0]["utcDate"])
        match.append(data["matches"][0]["homeTeam"]["name"])
        match.append(data["matches"][0]["awayTeam"]["name"])
        match.append(home)
        matches.append(match)
    return matches

def getIds():
    url = "https://api.football-data.org/v4/competitions/PL/teams"
    response = requests.get(url, headers = headers, params = params)
    data = response.json()
    for team in data["teams"]:
        print(team["name"])
        print(team["id"])

def getPlayers(teamId):
    url = f"https://api.football-data.org/v4/teams/{teamId}"
    response = requests.get(url, headers = headers, params = params)
    data = response.json()
    squad = []
    squad.append(data["coach"]["name"])
    for set in data["squad"]:
        squad.append(set["name"])
    return squad

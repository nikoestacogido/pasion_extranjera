# API KEY 507e730cb209ad0f97228d13ee84d748
# Aca manejo todo lo que se comunica con la API, y de aca salen funciones corte getmatches()
import time
import requests
import os

API_KEY = os.environ["FOOTBALL_API_KEY"]
headers = { "X-Auth-Token": API_KEY }
params = {
    "status": "SCHEDULED",
    "limit": 1
}

def getMatches(): # All matches envolving the few teams
    for team in [559, 86, 558]: #Sacarlo de un .CSV
        time.sleep(10)
        id = team
        url = f"https://api.football-data.org/v4/teams/{id}/matches"
        response = requests.get(url, headers = headers, params = params)
        data = response.json()
        print(f"{data["matches"][0]["homeTeam"]["name"]} vs {data["matches"][0]["awayTeam"]["name"]}")

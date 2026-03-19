#Unico script en tratar con la base de datos. He aqui todas las funciones que devuelven la info que posiblemente necesitarias
import sqlite3
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

def getTeamsFeature(column : str): #From all teams, X. Ej. "id"
    cursor.execute(f"SELECT {column} FROM teams")
    requested = []
    for data in cursor.fetchall(): requested.append(data[0])
    return requested

def getTeamFeature(column, id):
    cursor.execute(f"SELECT {column} FROM teams WHERE id = {id}")
    requested = []
    for data in cursor.fetchall(): requested.append(data[0])
    return requested

def writeMatches(matches):
    for match in matches:
        teamId = match[0]
        kickoffTime = match[1]
        home = match[2]
        away = match[3]
        against = ""
        condition = match[4]
        if condition:
            condition = "Home"
            against = away
        else:
            condition = "Away"
            against = home
        cursor.execute(
            f"UPDATE teams SET nextmatch = ? , matchtime = ? , condition = ? WHERE id = ?",
            (against, kickoffTime, condition, teamId)
        )
        conn.commit()

def writeSquad(squad : list, teamName : str):

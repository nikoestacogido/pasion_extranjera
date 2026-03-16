#Unico script en tratar con la base de datos. He aqui todas las funciones que devuelven la info que posiblemente necesitarias
import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

def getTeamsFeature(column : str): #From all teams, X. Ej. "id"
    cursor.execute(f"SELECT {column} FROM teams")
    requested = []
    for data in cursor.fetchall(): requested.append(data[0])
    return requested

"""API FastAPI + MongoDB

Esta API permite crear y leer usuarios en una base de datos MongoDB.
"""

from fastapi import FastAPI
from pymongo import MongoClient
import os


app = FastAPI(title="API FastAPI + MongoDB")

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017/")

client = MongoClient(MONGO_URL)
db = client.proyecto_db
coleccion = db.usuarios

@app.post("/usuarios/")
def crear_usuario(nombre: str, edad: int):
    """Crea un nuevo usuario en la base de datos."""
    resultado = coleccion.insert_one({"nombre": nombre, "edad": edad})
    return {"mensaje": "Usuario creado", "id": str(resultado.inserted_id)}

@app.get("/usuarios/")
def leer_usuarios():
    """Obtiene todos los usuarios de la base de datos."""
    usuarios = []
    for user in coleccion.find():
        usuarios.append({"id": str(user["_id"]), "nombre": user["nombre"], "edad": user["edad"]})
    return usuarios
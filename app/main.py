from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi import HTTPException

class Cifra(BaseModel):
    id: Optional[int] = None
    nome: str
    banda: str
    nivel: str  # iniciante, intermediária, avançada
    pestana: bool
    capotraste: bool
    tonalidade: str
    genero: str
    dedilhado: Optional[bool] = False
    levada: Optional[bool] = False


app = FastAPI()

@app.get("/")
def read_root():
    return {"Message" : "API CifraFacil online"}

cifras = []
next_id = 1

@app.post("/cifras/")
def criar_cifra(cifra: Cifra):
    if cifra.nivel == "iniciante" and cifra.pestana:
        raise HTTPException(status_code=400, detail="Cifra iniciante não pode ter pestana.")
    global next_id
    cifra.id = next_id
    next_id += 1
    cifras.append(cifra)
    return cifra

@app.get("/cifras/")
def listar_cifras():
    return cifras

from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from . import models
from .database import engine, SessionLocal
from .validators import validar_nivel

# Cria tabelas
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Pydantic schema
class Cifra(BaseModel):
    nome: str
    banda: str
    nivel: str
    pestana: bool
    capotraste: bool
    tonalidade: str
    genero: str
    dedilhado: bool
    levada: bool

    # Validação com função externa
    def __init__(self, **data):
        super().__init__(**data)
        validar_nivel(data["nivel"], data["pestana"])

# Dependência para sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Criar cifra
@app.post("/cifras/")
def criar_cifra(cifra: Cifra, db: Session = Depends(get_db)):
    db_cifra = models.Cifra(**cifra.dict())
    db.add(db_cifra)
    db.commit()
    db.refresh(db_cifra)
    return db_cifra

# Listar cifras
@app.get("/cifras/")
def listar_cifras(db: Session = Depends(get_db)):
    return db.query(models.Cifra).all()
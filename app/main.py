from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from . import models
from .database import engine, SessionLocal
from .validators import validar_nivel
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Cria tabelas
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # coloque o seu front local aqui
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.put("/cifras/{cifra_id}")
def update_cifra(cifra_id: int, cifra: Cifra, db: Session = Depends(get_db)):
    db_cifra = db.query(models.Cifra).filter(models.Cifra.id == cifra_id).first()
    if db_cifra is None:
        raise HTTPException(status_code=404, detail="Cifra não encontrada")
    
    db_cifra.nome = cifra.nome
    db_cifra.banda = cifra.banda
    db_cifra.nivel = cifra.nivel
    db_cifra.pestana = cifra.pestana
    db_cifra.capotraste = cifra.capotraste
    db_cifra.tonalidade = cifra.tonalidade
    db_cifra.genero = cifra.genero
    db_cifra.dedilhado = cifra.dedilhado
    db_cifra.levada = cifra.levada

    db.commit()
    db.refresh(db_cifra)
    return db_cifra


@app.delete("/cifras/{cifra_id}")
def delete_cifra(cifra_id: int, db: Session = Depends(get_db)):
    db_cifra = db.query(models.Cifra).filter(models.Cifra.id == cifra_id).first()
    if db_cifra is None:
        raise HTTPException(status_code=404, detail="Cifra não encontrada")

    db.delete(db_cifra)
    db.commit()
    return {"ok": True}



#uvicorn app.main:app
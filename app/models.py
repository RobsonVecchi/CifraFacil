from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class Cifra(Base):
    __tablename__ = "cifras"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    banda = Column(String)
    nivel = Column(String)
    pestana = Column(Boolean)
    capotraste = Column(Boolean)
    tonalidade = Column(String)
    genero = Column(String)
    dedilhado = Column(Boolean)
    levada = Column(Boolean)
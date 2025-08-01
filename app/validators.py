from fastapi import HTTPException

def validar_nivel(nivel: str, pestana: bool):
    """
    Regra: Se tiver pestana, não pode ser iniciante.
    """
    if nivel.lower() == "iniciante" and pestana:
        raise HTTPException(
            status_code=400,
            detail="Nível iniciante não pode ter pestana."
        )
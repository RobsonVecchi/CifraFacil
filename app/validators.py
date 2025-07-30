def validar_nivel(pestana: bool, nivel: str) -> bool:
    """
    Regra: Se tiver pestana, não pode ser iniciante.
    """
    if nivel.lower() == "iniciante" and pestana:
        return False
    return True
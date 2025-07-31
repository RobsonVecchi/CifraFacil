def validar_nivel(nivel: str, pestana: bool) -> bool:
    """
    Regra: Se tiver pestana, não pode ser iniciante.
    """
    if nivel.lower() == "iniciante" and pestana:
        return False
    return True
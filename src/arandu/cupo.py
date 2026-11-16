def hay_cupo(cupo: int, inscripciones: list[str]) -> bool:
    """Indica si una comisión puede recibir una inscripción más.

    Cada elemento de ``inscripciones`` es ``"activa"`` o ``"baja"``.
    Solo las inscripciones activas ocupan lugar; una baja no.
    """
    ocupados = sum(1 for estado in inscripciones if estado == "activa")
    return ocupados < cupo

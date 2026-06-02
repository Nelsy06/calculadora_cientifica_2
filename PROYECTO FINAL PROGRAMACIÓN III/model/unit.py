from dataclasses import dataclass, field
from typing import List


@dataclass(frozen=True)
class Unit:
    """Representa una unidad de medida. Inmutable."""
    nombre: str
    simbolo: str
    factor_a_base: float  # factor para convertir a la unidad base de la categoría


class UnitCategory:
    """Agrupa unidades de la misma magnitud."""

    def __init__(self, nombre: str, unidades: List[Unit]):
        self.nombre: str = nombre
        self.unidades: List[Unit] = unidades

    def get_unidad(self, nombre: str) -> Unit:
        for u in self.unidades:
            if u.nombre == nombre or u.simbolo == nombre:
                return u
        raise ValueError(f"Unidad '{nombre}' no encontrada en categoría '{self.nombre}'")

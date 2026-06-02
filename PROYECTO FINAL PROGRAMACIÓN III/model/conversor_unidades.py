from typing import List
from PySide6.QtCore import QObject, Signal

from model.unit import Unit, UnitCategory


def _build_categories() -> List[UnitCategory]:
    from model.unit import Unit, UnitCategory

    longitud = UnitCategory("Longitud", [
        Unit("Metro",      "m",  1.0),
        Unit("Kilómetro",  "km", 1000.0),
        Unit("Centímetro", "cm", 0.01),
        Unit("Milímetro",  "mm", 0.001),
        Unit("Pulgada",    "in", 0.0254),
        Unit("Pie",        "ft", 0.3048),
        Unit("Milla",      "mi", 1609.344),
    ])

    peso = UnitCategory("Peso/Masa", [
        Unit("Kilogramo",  "kg",  1.0),
        Unit("Gramo",      "g",   0.001),
        Unit("Miligramo",  "mg",  1e-6),
        Unit("Libra",      "lb",  0.453592),
        Unit("Onza",       "oz",  0.0283495),
        Unit("Tonelada",   "t",   1000.0),
    ])

    # Temperatura requiere fórmula especial, se maneja aparte
    temperatura = UnitCategory("Temperatura", [
        Unit("Celsius",    "°C", 1.0),
        Unit("Fahrenheit", "°F", 1.0),   # factor no aplica; lógica especial
        Unit("Kelvin",     "K",  1.0),
    ])

    return [longitud, peso, temperatura]


class ConversorUnidades(QObject):
    conversion_done = Signal(float)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.categorias: List[UnitCategory] = _build_categories()
        self.valor: float = 0.0

    def convertir(self, origen: Unit, destino: Unit, val: float) -> float:
        """Convierte val de origen a destino. Emite conversion_done."""
        # Caso especial: temperatura
        if origen.simbolo in ("°C", "°F", "K") or destino.simbolo in ("°C", "°F", "K"):
            resultado = self._convertir_temperatura(origen.simbolo, destino.simbolo, val)
        else:
            # Normalizar a base, luego a destino
            en_base = val * origen.factor_a_base
            resultado = en_base / destino.factor_a_base

        self.valor = resultado
        self.conversion_done.emit(resultado)
        return resultado

    def _convertir_temperatura(self, orig: str, dest: str, val: float) -> float:
        # Primero a Celsius
        if orig == "°C":
            celsius = val
        elif orig == "°F":
            celsius = (val - 32) * 5 / 9
        else:  # Kelvin
            celsius = val - 273.15

        # De Celsius a destino
        if dest == "°C":
            return celsius
        elif dest == "°F":
            return celsius * 9 / 5 + 32
        else:  # Kelvin
            return celsius + 273.15

    def get_categorias(self) -> List[UnitCategory]:
        return self.categorias

    def get_unidades(self, cat_nombre: str) -> List[Unit]:
        for c in self.categorias:
            if c.nombre == cat_nombre:
                return c.unidades
        return []

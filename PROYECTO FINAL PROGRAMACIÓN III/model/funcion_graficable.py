import math
from typing import List, Tuple
from PySide6.QtCore import QObject, Signal

from model.enums import TipoFuncion


class FuncionGraficable(QObject):
    puntos_listos = Signal(list)   
    def __init__(self, parent=None):
        super().__init__(parent)
        self.expresion: str = "sin(x)"
        self.tipo: TipoFuncion = TipoFuncion.SENO
        self.x_min: float = -10.0
        self.x_max: float = 10.0
        self.num_puntos: int = 500

    def evaluar(self, x: float) -> float:
        """Evalúa f(x) para el valor dado."""
        import numpy as np  
        env = {
            "x": x, "sin": math.sin, "cos": math.cos, "tan": math.tan,
            "sqrt": math.sqrt, "log": math.log10, "ln": math.log,
            "exp": math.exp, "abs": abs, "pi": math.pi, "e": math.e,
        }
        try:
            return float(eval(self.expresion, {"__builtins__": {}}, env))
        except Exception:
            return float("nan")

    def generar_puntos(self) -> List[Tuple[float, float]]:
        """Genera la lista de puntos y emite puntos_listos."""
        paso = (self.x_max - self.x_min) / max(self.num_puntos, 1)
        puntos: List[Tuple[float, float]] = []
        x = self.x_min
        while x <= self.x_max + 1e-9:
            y = self.evaluar(x)
            puntos.append((x, y))
            x += paso
        self.puntos_listos.emit(puntos)
        return puntos

    def set_rango(self, xmin: float, xmax: float) -> None:
        self.x_min = xmin
        self.x_max = xmax

    def get_expresion(self) -> str:
        return self.expresion

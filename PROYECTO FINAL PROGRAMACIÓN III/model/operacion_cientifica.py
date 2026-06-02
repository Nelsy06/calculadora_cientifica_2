import math
from model.enums import TipoOperacion, UnidadAngulo


class OperacionCientifica:
    def __init__(self):
        self.expresion: str = ""
        self.tipo: TipoOperacion = TipoOperacion.ARITMETICA
        self.unidad_angulo: UnidadAngulo = UnidadAngulo.DEG

    def _a_radianes(self, valor: float) -> float:
        if self.unidad_angulo == UnidadAngulo.DEG:
            return math.radians(valor)
        elif self.unidad_angulo == UnidadAngulo.GRAD:
            return valor * math.pi / 200
        return valor  # RAD

    def calcular_trigonometrica(self, nombre: str, valor: float) -> float:
        rad = self._a_radianes(valor)
        ops = {
            "sin": math.sin, "cos": math.cos, "tan": math.tan,
            "asin": lambda x: math.degrees(math.asin(x)),
            "acos": lambda x: math.degrees(math.acos(x)),
            "atan": lambda x: math.degrees(math.atan(x)),
        }
        if nombre not in ops:
            raise ValueError(f"Función trigonométrica desconocida: {nombre}")
        if nombre in ("asin", "acos", "atan"):
            return ops[nombre](valor)
        return ops[nombre](rad)

    def calcular_logaritmo(self, valor: float, base: float = 10) -> float:
        if valor <= 0:
            raise ValueError("El logaritmo requiere un valor positivo")
        if base == math.e:
            return math.log(valor)
        return math.log(valor, base)

    def calcular_potencia(self, base: float, exponente: float) -> float:
        if base < 0 and not exponente.is_integer():
            raise ValueError("Potencia de base negativa con exponente no entero")
        return math.pow(base, exponente)

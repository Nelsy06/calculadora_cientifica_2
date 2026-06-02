import math
from typing import List
from PySide6.QtCore import QObject, Signal

from model.enums import ModoCalculadora, UnidadAngulo
from model.operacion_cientifica import OperacionCientifica
from model.conversor_unidades import ConversorUnidades
from model.funcion_graficable import FuncionGraficable


class CalculadoraModelo(QObject):
    result_ready           = Signal(float)
    error_ocurrido         = Signal(str)
    historial_actualizado  = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._historial: List[str] = []
        self.max_historial: int = 100   
        self._expresion_actual: str = ""
        self.modo: ModoCalculadora = ModoCalculadora.BASICO
        self.unidad_angulo: UnidadAngulo = UnidadAngulo.DEG

        
        self._op_cient: OperacionCientifica = OperacionCientifica()
        self.conversor: ConversorUnidades = ConversorUnidades(self)

        
        self._funciones: List[FuncionGraficable] = []

    # ── @property ──────────────────────────────────────────────────────
    @property
    def expresion_actual(self) -> str:
        return self._expresion_actual

    @expresion_actual.setter
    def expresion_actual(self, val: str) -> None:
        self._expresion_actual = val

    # ── Métodos públicos ───────────────────────────────────────────────
    def evaluar_expresion(self, expr: str) -> float:
        """Evalúa expr matemáticamente. Emite result_ready o error_ocurrido."""
        self._op_cient.unidad_angulo = self.unidad_angulo
        env = {
            "sin":  lambda x: self._op_cient.calcular_trigonometrica("sin", x),
            "cos":  lambda x: self._op_cient.calcular_trigonometrica("cos", x),
            "tan":  lambda x: self._op_cient.calcular_trigonometrica("tan", x),
            "asin": lambda x: self._op_cient.calcular_trigonometrica("asin", x),
            "acos": lambda x: self._op_cient.calcular_trigonometrica("acos", x),
            "atan": lambda x: self._op_cient.calcular_trigonometrica("atan", x),
            "log":  lambda x: self._op_cient.calcular_logaritmo(x, 10),
            "ln":   lambda x: self._op_cient.calcular_logaritmo(x, math.e),
            "sqrt": math.sqrt,
            "exp":  math.exp,
            "abs":  abs,
            "pi":   math.pi,
            "e":    math.e,
            "pow":  self._op_cient.calcular_potencia,
        }
        try:
            resultado = float(eval(expr, {"__builtins__": {}}, env))
            if math.isnan(resultado) or math.isinf(resultado):
                raise ValueError("Resultado inválido (nan/inf)")
            self.agregar_historial(f"{expr} = {resultado}")
            self.result_ready.emit(resultado)
            return resultado
        except ZeroDivisionError:
            self.error_ocurrido.emit("Error: división por cero")
            raise
        except Exception as exc:
            self.error_ocurrido.emit(f"Error: {exc}")
            raise

    def agregar_historial(self, op: str) -> None:
        if len(self._historial) >= self.max_historial:
            self._historial.pop(0)
        self._historial.append(op)
        self.historial_actualizado.emit()

    def limpiar_historial(self) -> None:
        self._historial.clear()
        self.historial_actualizado.emit()

    def get_historial(self) -> List[str]:
        return list(self._historial)

    def set_modo(self, m: ModoCalculadora) -> None:
        self.modo = m


    def nueva_funcion(self) -> FuncionGraficable:
        fn = FuncionGraficable(self)
        self._funciones.append(fn)
        return fn

    def get_funciones(self) -> List[FuncionGraficable]:
        return list(self._funciones)

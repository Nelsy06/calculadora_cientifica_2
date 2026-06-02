import functools
from typing import Dict, List, Callable, Tuple
from PySide6.QtWidgets import QMessageBox, QWidget
from PySide6.QtCore import SignalInstance


class ManejadorErrores:
    def __init__(self, padre: QWidget = None):
        self._padre = padre
        self.tipo_error: str = ""

    
    def manejar_division_cero(self) -> None:
        QMessageBox.critical(self._padre, "Error", "División por cero")

    def manejar_expresion_invalida(self) -> None:
        QMessageBox.warning(self._padre, "Advertencia", "Expresión inválida")

    def mostrar_qmessage(self, tipo: str, msg: str) -> None:
        """Conectado a error_ocurrido Signal."""
        self.tipo_error = tipo
        if "cero" in msg.lower():
            QMessageBox.critical(self._padre, "Error de cálculo", msg)
        else:
            QMessageBox.warning(self._padre, "Advertencia", msg)


class ConectadorSeñales:
    """
    Centraliza el ciclo de vida de conexiones Qt.
    Propósito: poder llamar disconnect() limpio al cerrar subventanas MDI,
    evitando conexiones fantasma (señales ejecutadas múltiples veces).
    """

    def __init__(self):
        self.partial_map: Dict[object, Callable] = {}
        self.lambda_map:  Dict[str, Callable]    = {}
        self.connect_map: Dict[str, Tuple]       = {}

    def registrar(self, btn, accion: str) -> None:
        self.partial_map[btn] = accion

    def usar_partial(self, fn: Callable, val) -> Callable:
        """Retorna functools.partial(fn, val) y lo registra."""
        cb = functools.partial(fn, val)
        self.lambda_map[str(val)] = cb
        return cb

    def usar_lambda(self, fn: Callable, val) -> Callable:
        """Retorna lambda v=val: fn(v) y lo registra."""
        cb = lambda v=val: fn(v)
        self.lambda_map[f"lam_{val}"] = cb
        return cb

    def usar_connect(self, signal: SignalInstance, slot: Callable) -> None:
        """Conecta signal → slot y registra para posible disconnect."""
        key = f"{id(signal)}_{id(slot)}"
        self.connect_map[key] = (signal, slot)
        signal.connect(slot)

    def desconectar(self, btn) -> None:
        """Desconecta las señales del botón dado."""
        try:
            btn.clicked.disconnect()
        except RuntimeError:
            pass
        self.partial_map.pop(btn, None)

    def desconectar_todo(self) -> None:
        """Desconecta todas las señales registradas."""
        for key, (signal, slot) in list(self.connect_map.items()):
            try:
                signal.disconnect(slot)
            except RuntimeError:
                pass
        self.connect_map.clear()

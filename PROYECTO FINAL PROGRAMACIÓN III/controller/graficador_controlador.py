from PySide6.QtCore import QObject

from model.funcion_graficable import FuncionGraficable
from model.enums import TipoFuncion
from view.paneles import PanelGraficador
from view.subventanas import SubventanaGraficador


class GraficadorControlador(QObject):
    def __init__(
        self,
        modelo_funcion: FuncionGraficable,
        vista_panel: PanelGraficador,
        sub_ventana: SubventanaGraficador,
        parent=None
    ):
        super().__init__(parent)
        self.modelo_funcion: FuncionGraficable    = modelo_funcion
        self.vista_panel:    PanelGraficador      = vista_panel
        self.sub_ventana:    SubventanaGraficador = sub_ventana
        self.conectar_señales()

    def conectar_señales(self) -> None:
        """
        ✅ Pendiente #1 RESUELTO:
        puntos_listos → GraficadorWidget.set_puntos
        La flecha sale del Controlador, NO del Modelo.
        """
        self.modelo_funcion.puntos_listos.connect(
            self.vista_panel.graficador.set_puntos
        )
        self.vista_panel.graficar_pedido.connect(self._on_graficar)

    def _on_graficar(self, expr: str, xmin: float, xmax: float) -> None:
        """Slot: petición de graficar desde el panel."""
        self.on_graficar(expr, xmin, xmax)

    def on_graficar(self, expr: str, xmin: float = -10.0, xmax: float = 10.0) -> None:
        self.modelo_funcion.expresion = expr
        self.modelo_funcion.set_rango(xmin, xmax)
        puntos = self.modelo_funcion.generar_puntos()
        # puntos_listos ya emitido dentro de generar_puntos()

    def set_rango(self, xmin: float, xmax: float) -> None:
        self.modelo_funcion.set_rango(xmin, xmax)

    def on_tipo_funcion(self, t: TipoFuncion) -> None:
        self.modelo_funcion.tipo = t

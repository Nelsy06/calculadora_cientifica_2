from PySide6.QtWidgets import QMdiSubWindow, QWidget, QVBoxLayout
from PySide6.QtGui import QCloseEvent
from PySide6.QtCore import Signal

from view.display_led import DisplayLED
from view.paneles import PanelBasico, PanelCientifico, PanelConversor, PanelGraficador
from view.historial_widget import HistorialWidget


class SubventanaCalculadora(QMdiSubWindow):
    """
    Subventana de calculadora.
    - Modo BASICO:      muestra solo PanelBasico + DisplayLED
    - Modo CIENTIFICO:  muestra PanelBasico + PanelCientifico + DisplayLED
    """
    resultado_calculado = Signal(float)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.titulo = "Calculadora"
        self.setWindowTitle(self.titulo)

        # Widgets internos (conforme al UML)
        self.display       = DisplayLED()
        self.panel         = PanelBasico()
        self.panel_cient   = PanelCientifico()
        self._contenido: QWidget = None
        self._init_contenido()

    def _init_contenido(self) -> None:
        contenido = QWidget()
        vbox = QVBoxLayout(contenido)
        vbox.setContentsMargins(6, 6, 6, 6)
        vbox.setSpacing(4)
        vbox.addWidget(self.display)
        vbox.addWidget(self.panel)
        vbox.addWidget(self.panel_cient)
        # Panel científico oculto por defecto; visible solo en modo CIENTIFICO
        self.panel_cient.hide()
        self._contenido = contenido
        self.setWidget(contenido)
        self.resize(360, 520)

    def mostrar_panel_cientifico(self, visible: bool) -> None:
        """Muestra u oculta el panel científico según el modo."""
        self.panel_cient.setVisible(visible)
        # Ajustar tamaño al contenido
        if visible:
            self.resize(360, 780)
            self.setWindowTitle("Calculadora — Modo Científico")
        else:
            self.resize(360, 520)
            self.setWindowTitle("Calculadora — Modo Básico")

    def enviar_resultado(self, v: float) -> None:
        self.resultado_calculado.emit(v)

    def closeEvent(self, e: QCloseEvent) -> None:
        super().closeEvent(e)


# ══════════════════════════════════════════════════════════════════════
class SubventanaConversor(QMdiSubWindow):
    """Subventana exclusiva para el modo CONVERSOR."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.titulo = "Conversor de Unidades"
        self.setWindowTitle(self.titulo)
        self.panel_conv = PanelConversor()
        self._init_contenido()

    def _init_contenido(self) -> None:
        contenido = QWidget()
        vbox = QVBoxLayout(contenido)
        vbox.setContentsMargins(4, 4, 4, 4)
        vbox.addWidget(self.panel_conv)
        self.setWidget(contenido)
        self.resize(420, 360)

    def closeEvent(self, e: QCloseEvent) -> None:
        super().closeEvent(e)

# ══════════════════════════════════════════════════════════════════════
class SubventanaHistorial(QMdiSubWindow):
    """Subventana de historial de operaciones (siempre visible)."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.titulo = "Historial"
        self.setWindowTitle(self.titulo)
        self.historial_widget = HistorialWidget()
        self.vbox = QVBoxLayout()
        self._init_contenido()

    def _init_contenido(self) -> None:
        contenido = QWidget()
        vbox = QVBoxLayout(contenido)
        vbox.setContentsMargins(4, 4, 4, 4)
        vbox.addWidget(self.historial_widget)
        self.setWidget(contenido)
        self.resize(350, 380)

    def refrescar(self) -> None:
        pass

    def recibir_resultado(self, v: float) -> None:
        """Conectado a resultado_calculado Signal."""
        self.historial_widget.agregar_entrada(f"= {v}")

    def exportar(self) -> None:
        self.historial_widget.exportar_txt()

    def closeEvent(self, e: QCloseEvent) -> None:
        super().closeEvent(e)


# ══════════════════════════════════════════════════════════════════════
class SubventanaGraficador(QMdiSubWindow):
    """Subventana exclusiva para el modo GRAFICADOR."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.titulo = "Graficador de Funciones"
        self.setWindowTitle(self.titulo)
        self.panel_graf = PanelGraficador()
        self.vbox = QVBoxLayout()
        self._init_contenido()

    def _init_contenido(self) -> None:
        contenido = QWidget()
        vbox = QVBoxLayout(contenido)
        vbox.setContentsMargins(4, 4, 4, 4)
        vbox.addWidget(self.panel_graf)
        self.setWidget(contenido)
        self.resize(620, 520)

    def recibir_puntos(self, pts: list) -> None:
        """Conectado a puntos_listos vía GraficadorControlador."""
        self.panel_graf.actualizar_grafica(pts)

    def closeEvent(self, e: QCloseEvent) -> None:
        super().closeEvent(e)

from PySide6.QtWidgets import (
    QMainWindow, QMdiArea, QMenuBar, QToolBar,
    QStatusBar, QMessageBox, QLabel
)
from PySide6.QtCore import Signal
from PySide6.QtGui import QAction, QKeySequence

from model.enums import ModoCalculadora, TemaUI


class VentanaPrincipal(QMainWindow):
    modo_cambiado = Signal(ModoCalculadora)
    tema_cambiado = Signal(TemaUI)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Calculadora Cientifica Avanzada")
        self.resize(1200, 750)

        self.menu_bar:   QMenuBar    = self.menuBar()
        self.toolbar:    QToolBar    = QToolBar("Principal")
        self.status_bar: QStatusBar  = self.statusBar()
        self.mdi_area:   QMdiArea    = QMdiArea()

        self.modo_actual: ModoCalculadora = ModoCalculadora.BASICO
        self.tema_actual: TemaUI          = TemaUI.OSCURO
        self.acciones: dict               = {}

        self._init_ui()

    def _init_ui(self) -> None:
        self.setCentralWidget(self.mdi_area)
        self.mdi_area.setViewMode(QMdiArea.ViewMode.SubWindowView)
        self.addToolBar(self.toolbar)
        self._init_menus()
        self._init_toolbar()
        self.mostrar_status("Modo: BASICO  -  seleccione un modo del menu o la barra")

    def _init_menus(self) -> None:
        menu_calc = self.menu_bar.addMenu("&Calculadora")

        ac_basico = QAction("Modo Basico",     self)
        ac_cient  = QAction("Modo Cientifico", self)
        ac_conv   = QAction("Modo Conversor",  self)
        ac_graf   = QAction("Modo Graficador", self)

        ac_basico.setShortcut(QKeySequence("Ctrl+1"))
        ac_cient.setShortcut(QKeySequence("Ctrl+2"))
        ac_conv.setShortcut(QKeySequence("Ctrl+3"))
        ac_graf.setShortcut(QKeySequence("Ctrl+4"))

        ac_basico.setStatusTip("Calculadora basica aritmetica")
        ac_cient.setStatusTip("Calculadora con funciones cientificas")
        ac_conv.setStatusTip("Convertidor de unidades")
        ac_graf.setStatusTip("Graficador de funciones matematicas")

        ac_basico.triggered.connect(lambda: self.modo_cambiado.emit(ModoCalculadora.BASICO))
        ac_cient.triggered.connect(lambda:  self.modo_cambiado.emit(ModoCalculadora.CIENTIFICO))
        ac_conv.triggered.connect(lambda:   self.modo_cambiado.emit(ModoCalculadora.CONVERSOR))
        ac_graf.triggered.connect(lambda:   self.modo_cambiado.emit(ModoCalculadora.GRAFICADOR))

        menu_calc.addAction(ac_basico)
        menu_calc.addAction(ac_cient)
        menu_calc.addAction(ac_conv)
        menu_calc.addAction(ac_graf)
        menu_calc.addSeparator()

        ac_salir = QAction("Salir", self)
        ac_salir.setShortcut(QKeySequence("Ctrl+Q"))
        ac_salir.triggered.connect(self.close)
        menu_calc.addAction(ac_salir)

        self.acciones.update({
            "basico": ac_basico, "cientifico": ac_cient,
            "conversor": ac_conv, "graficador": ac_graf,
        })

        menu_vista = self.menu_bar.addMenu("&Vista")

        ac_oscuro = QAction("Tema Oscuro",    self)
        ac_claro  = QAction("Tema Claro",     self)
        ac_alto   = QAction("Alto Contraste", self)

        ac_oscuro.setShortcut(QKeySequence("Ctrl+Shift+D"))
        ac_claro.setShortcut(QKeySequence("Ctrl+Shift+L"))
        ac_alto.setShortcut(QKeySequence("Ctrl+Shift+A"))

        ac_oscuro.triggered.connect(lambda: self.tema_cambiado.emit(TemaUI.OSCURO))
        ac_claro.triggered.connect(lambda:  self.tema_cambiado.emit(TemaUI.CLARO))
        ac_alto.triggered.connect(lambda:   self.tema_cambiado.emit(TemaUI.ALTO_CONTRASTE))

        menu_vista.addAction(ac_oscuro)
        menu_vista.addAction(ac_claro)
        menu_vista.addAction(ac_alto)
        menu_vista.addSeparator()

        menu_ventanas = menu_vista.addMenu("&Ventanas MDI")
        ac_cascade = QAction("Cascada",      self)
        ac_tile    = QAction("Mosaico",      self)
        ac_cerrar  = QAction("Cerrar todas", self)
        ac_cascade.setShortcut("Ctrl+Shift+C")
        ac_tile.setShortcut("Ctrl+Shift+T")
        ac_cerrar.setShortcut("Ctrl+Shift+W")
        ac_cascade.triggered.connect(self.mdi_area.cascadeSubWindows)
        ac_tile.triggered.connect(self.mdi_area.tileSubWindows)
        ac_cerrar.triggered.connect(self.mdi_area.closeAllSubWindows)
        menu_ventanas.addAction(ac_cascade)
        menu_ventanas.addAction(ac_tile)
        menu_ventanas.addAction(ac_cerrar)

        self.acciones.update({
            "oscuro": ac_oscuro, "claro": ac_claro, "alto": ac_alto,
            "cascade": ac_cascade, "tile": ac_tile,
        })

        menu_hist = self.menu_bar.addMenu("&Historial")
        ac_borrar = QAction("Borrar historial", self)
        ac_borrar.setShortcut("Ctrl+H")
        self.acciones["borrar_historial"] = ac_borrar
        menu_hist.addAction(ac_borrar)

        menu_ayuda = self.menu_bar.addMenu("A&yuda")
        ac_acerca = QAction("Acerca de...", self)
        ac_acerca.setShortcut("F1")
        ac_acerca.triggered.connect(self._mostrar_acerca)
        menu_ayuda.addAction(ac_acerca)

    def _init_toolbar(self) -> None:
        self.toolbar.setMovable(True)

        for etiqueta, modo in [
            ("Basico",     ModoCalculadora.BASICO),
            ("Cientifico", ModoCalculadora.CIENTIFICO),
            ("Conversor",  ModoCalculadora.CONVERSOR),
            ("Graficador", ModoCalculadora.GRAFICADOR),
        ]:
            ac = QAction(etiqueta, self)
            ac.triggered.connect(lambda checked=False, m=modo: self.modo_cambiado.emit(m))
            self.toolbar.addAction(ac)

        self.toolbar.addSeparator()

        for etiqueta, tema in [
            ("Oscuro",    TemaUI.OSCURO),
            ("Claro",     TemaUI.CLARO),
            ("Contraste", TemaUI.ALTO_CONTRASTE),
        ]:
            ac = QAction(etiqueta, self)
            ac.triggered.connect(lambda checked=False, t=tema: self.tema_cambiado.emit(t))
            self.toolbar.addAction(ac)

        self.toolbar.addSeparator()

        for etiqueta, slot in [
            ("Mosaico", self.mdi_area.tileSubWindows),
            ("Cascada", self.mdi_area.cascadeSubWindows),
        ]:
            ac = QAction(etiqueta, self)
            ac.triggered.connect(slot)
            self.toolbar.addAction(ac)

    def aplicar_tema(self, t: TemaUI) -> None:
        self.tema_actual = t

    def mostrar_status(self, msg: str) -> None:
        self.status_bar.showMessage(msg, 5000)

    def mostrar_error(self, msg: str) -> None:
        QMessageBox.critical(self, "Error", msg)

    def _mostrar_acerca(self) -> None:
        QMessageBox.information(
            self, "Acerca de",
            "Calculadora Cientifica Avanzada\n"
            "Arquitectura MVC + MDI  PySide6\n\n"
            "Modos disponibles:\n"
            "  Basico       (Ctrl+1)\n"
            "  Cientifico   (Ctrl+2)\n"
            "  Conversor    (Ctrl+3)\n"
            "  Graficador   (Ctrl+4)\n\n"
            "Cada modo abre su subventana MDI al seleccionarse."
        )

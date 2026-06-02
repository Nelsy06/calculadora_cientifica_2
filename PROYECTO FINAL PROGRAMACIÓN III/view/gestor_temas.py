import os
from typing import Dict, List
from PySide6.QtWidgets import QApplication

from model.enums import TemaUI

_QSS: Dict[TemaUI, str] = {
    TemaUI.OSCURO: """
        QMainWindow, QWidget { background-color: #1a1018; color: #f0e0ec; }
        QPushButton {
            background-color: #2d1f2b; color: #f0e0ec;
            border: 1px solid #5a3a52; border-radius: 6px;
            padding: 8px 12px; font-size: 14px;
        }
        QPushButton:hover  { background-color: #3d2a3a; border-color: #e879b0; }
        QPushButton:pressed { background-color: #6b1a4a; }
        QPushButton#btnIgual { background-color: #8b1a5a; color: #ffe0f0; font-weight: bold; font-size: 16px; }
        QPushButton#btnLimpiar { background-color: #5a1a3a; color: #ffb0d0; }
        QPushButton#btnCientifico { background-color: #2a1a3a; color: #d4a0e8; }
        QLineEdit, QTextEdit {
            background-color: #0f080d; color: #ff79c6;
            border: 1px solid #4a2a40; border-radius: 4px; padding: 4px;
            font-family: 'Courier New'; font-size: 13px;
        }
        QComboBox {
            background-color: #2d1f2b; color: #f0e0ec;
            border: 1px solid #5a3a52; border-radius: 4px; padding: 4px;
        }
        QComboBox QAbstractItemView { background-color: #2d1f2b; color: #f0e0ec; }
        QSpinBox { background-color: #2d1f2b; color: #f0e0ec; border: 1px solid #5a3a52; border-radius: 4px; padding: 4px; }
        QLabel { color: #d4a0c0; }
        QMenuBar { background-color: #1f1020; color: #f0e0ec; }
        QMenuBar::item:selected { background-color: #3d2a3a; }
        QMenu { background-color: #1f1020; color: #f0e0ec; border: 1px solid #5a3a52; }
        QMenu::item:selected { background-color: #6b1a4a; }
        QToolBar { background-color: #1f1020; border: none; spacing: 4px; }
        QStatusBar { background-color: #140c12; color: #a07890; }
        QMdiArea { background-color: #110810; }
        QMdiSubWindow { background-color: #1a1018; border: 1px solid #5a3a52; }
        QMdiSubWindow::title { background-color: #1f1020; color: #f0e0ec; }
        QScrollBar:vertical { background: #1a1018; width: 10px; }
        QScrollBar::handle:vertical { background: #5a3a52; border-radius: 5px; }
        QCheckBox { color: #f0e0ec; }
        QCheckBox::indicator { width: 16px; height: 16px; }
        #historialTextEdit { font-family: 'Courier New'; font-size: 12px; }
    """,
    TemaUI.CLARO: """
        QMainWindow, QWidget { background-color: #fff5f9; color: #2a0a1a; }
        QPushButton {
            background-color: #f5d0e8; color: #2a0a1a;
            border: 1px solid #d090b8; border-radius: 6px;
            padding: 8px 12px; font-size: 14px;
        }
        QPushButton:hover  { background-color: #eebbda; border-color: #c0569a; }
        QPushButton:pressed { background-color: #d890c0; }
        QPushButton#btnIgual { background-color: #c0569a; color: #fff; font-weight: bold; }
        QPushButton#btnLimpiar { background-color: #e06090; color: #fff; }
        QLineEdit, QTextEdit {
            background-color: #ffffff; color: #2a0a1a;
            border: 1px solid #d090b8; border-radius: 4px; padding: 4px;
        }
        QComboBox { background-color: #ffffff; color: #2a0a1a; border: 1px solid #d090b8; }
        QLabel { color: #5a2a48; }
        QMenuBar { background-color: #f5d0e8; color: #2a0a1a; }
        QToolBar { background-color: #f5d0e8; }
        QStatusBar { background-color: #ffe0f0; color: #8a4a6a; }
        QMdiArea { background-color: #eec0d8; }
    """,
    TemaUI.ALTO_CONTRASTE: """
        QMainWindow, QWidget { background-color: #000000; color: #FFB8E0; }
        QPushButton {
            background-color: #000000; color: #FFB8E0;
            border: 2px solid #FFB8E0; border-radius: 4px;
            padding: 8px 12px; font-size: 15px; font-weight: bold;
        }
        QPushButton:hover  { background-color: #1a0010; }
        QPushButton#btnIgual { background-color: #FFB8E0; color: #000000; }
        QLineEdit, QTextEdit { background-color: #000000; color: #FFFFFF; border: 2px solid #FFB8E0; }
        QComboBox { background-color: #000000; color: #FFB8E0; border: 2px solid #FFB8E0; }
        QLabel { color: #FFB8E0; font-weight: bold; }
        QMenuBar { background-color: #000000; color: #FFB8E0; }
        QToolBar { background-color: #000000; }
        QStatusBar { background-color: #000000; color: #FFB8E0; }
        QMdiArea { background-color: #000000; }
    """,
}

class GestorTemas:
    def __init__(self):
        self.tema_activo: TemaUI = TemaUI.OSCURO
        self.temas: Dict[TemaUI, str] = _QSS
        self.ruta_qss: str = ""

    def aplicar_tema(self, t: TemaUI) -> None:
        self.tema_activo = t
        app = QApplication.instance()
        if app:
            qss = self.temas.get(t, "")
            if self.ruta_qss and os.path.isfile(self.ruta_qss):
                with open(self.ruta_qss, encoding="utf-8") as f:
                    qss = f.read()
            app.setStyleSheet(qss)

    def listar_temas(self) -> List[TemaUI]:
        return list(self.temas.keys())

    def cargar_qss(self, archivo: str) -> str:
        if os.path.isfile(archivo):
            with open(archivo, encoding="utf-8") as f:
                return f.read()
        return ""

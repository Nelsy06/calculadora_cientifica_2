from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton, QHBoxLayout, QFileDialog
from PySide6.QtCore import Qt


class HistorialWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.solo_lectura: bool = True
        self._build_ui()

    def _build_ui(self) -> None:
        vbox = QVBoxLayout(self)
        vbox.setContentsMargins(0, 0, 0, 0)

        self._text_edit = QTextEdit()
        self._text_edit.setReadOnly(True)
        self._text_edit.setObjectName("historialTextEdit")
        vbox.addWidget(self._text_edit)

        hbox = QHBoxLayout()
        btn_limpiar  = QPushButton("Limpiar")
        btn_exportar = QPushButton("Exportar .txt")
        btn_limpiar.setObjectName("btnLimpiar")
        btn_exportar.setObjectName("btnExportar")
        btn_limpiar.clicked.connect(self.limpiar)
        btn_exportar.clicked.connect(self.exportar_txt)
        hbox.addWidget(btn_limpiar)
        hbox.addWidget(btn_exportar)
        vbox.addLayout(hbox)

    
    def agregar_entrada(self, txt: str) -> None:
        """Recibe historial_actualizado — añade el texto al display."""
        self._text_edit.append(txt)

    def actualizar_desde_lista(self, historial: list) -> None:
        """Refresca completo desde la lista del modelo."""
        self._text_edit.clear()
        for entrada in historial:
            self._text_edit.append(entrada)

    def limpiar(self) -> None:
        self._text_edit.clear()

    def exportar_txt(self) -> None:
        ruta, _ = QFileDialog.getSaveFileName(
            self, "Exportar historial", "historial.txt",
            "Texto (*.txt);;CSV (*.csv)"
        )
        if ruta:
            with open(ruta, "w", encoding="utf-8") as f:
                f.write(self._text_edit.toPlainText())

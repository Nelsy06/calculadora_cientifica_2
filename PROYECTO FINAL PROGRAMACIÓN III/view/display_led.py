from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import (
    QPainter, QColor, QFont, QPaintEvent, QLinearGradient, QPen
)

class DisplayLED(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.texto: str = "0"
        self.color_encendido: QColor = QColor("#ff79c6")   # rosa LED
        self.color_apagado: QColor   = QColor("#330020")
        self.fuente_segmentada: QFont = QFont("Courier New", 28, QFont.Weight.Bold)
        self.num_digitos: int = 20
        self.alineacion = Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        self.setMinimumHeight(70)
        self.setMinimumWidth(300)

    def set_texto(self, t: str) -> None:
        self.texto = t
        self.update()

    def set_color(self, encendido: QColor, apagado: QColor) -> None:
        self.color_encendido = encendido
        self.color_apagado   = apagado
        self.update()

    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        rect = self.rect()

        grad = QLinearGradient(0, 0, 0, rect.height())
        grad.setColorAt(0.0, QColor("#0d0008"))
        grad.setColorAt(1.0, QColor("#1a0015"))
        painter.fillRect(rect, grad)

        pen = QPen(QColor("#4a1a3a"), 2)
        painter.setPen(pen)
        painter.drawRoundedRect(rect.adjusted(1, 1, -1, -1), 6, 6)

        inner_pen = QPen(QColor("#ff79c655"), 1)
        painter.setPen(inner_pen)
        painter.drawRoundedRect(rect.adjusted(3, 3, -3, -3), 4, 4)

        painter.setFont(self.fuente_segmentada)

        apagado_text = "8" * self.num_digitos
        painter.setPen(self.color_apagado)
        painter.drawText(rect.adjusted(10, 0, -10, 0), self.alineacion, apagado_text)

        painter.setPen(self.color_encendido)
        painter.drawText(rect.adjusted(10, 0, -10, 0), self.alineacion, self.texto)

        painter.end()

from typing import List, Tuple
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, QRect, QPoint
from PySide6.QtGui import (
    QPainter, QColor, QPen, QFont, QPaintEvent, QLinearGradient
)
import math

class GraficadorWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.puntos: List[Tuple[float, float]] = []
        self.color_curva: QColor  = QColor("#ff79c6")
        self.color_ejes: QColor   = QColor("#AAAAAA")
        self.color_grid: QColor   = QColor("#333333")
        self.x_min: float = -10.0
        self.x_max: float =  10.0
        self.y_min: float = -5.0
        self.y_max: float =  5.0
        self.titulo_grafica: str  = "f(x)"
        self.setMinimumSize(400, 300)
        self._margen = 40

    def set_puntos(self, pts: list) -> None:
        self.puntos = pts
        if pts:
            ys = [p[1] for p in pts if not math.isnan(p[1]) and not math.isinf(p[1])]
            if ys:
                self.y_min = min(ys)
                self.y_max = max(ys)
                if abs(self.y_max - self.y_min) < 1e-9:
                    self.y_min -= 1; self.y_max += 1
        self.update()

    def limpiar(self) -> None:
        self.puntos = []
        self.update()

    def exportar_imagen(self) -> None:
        from PySide6.QtWidgets import QFileDialog
        from PySide6.QtGui import QPixmap
        ruta, _ = QFileDialog.getSaveFileName(
            self, "Exportar imagen", "grafica.png",
            "PNG (*.png);;JPEG (*.jpg)"
        )
        if ruta:
            pixmap = self.grab()
            pixmap.save(ruta)


    def _mundo_a_pixel(self, x: float, y: float, w: int, h: int) -> QPoint:
        m = self._margen
        px = int(m + (x - self.x_min) / (self.x_max - self.x_min) * (w - 2 * m))
        py = int(h - m - (y - self.y_min) / (self.y_max - self.y_min) * (h - 2 * m))
        return QPoint(px, py)

    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        w, h = self.width(), self.height()
        m = self._margen

        # Fondo
        painter.fillRect(self.rect(), QColor("#111111"))

        # Grid
        painter.setPen(QPen(self.color_grid, 1, Qt.PenStyle.DotLine))
        for i in range(10):
            x_pos = m + i * (w - 2 * m) // 10
            painter.drawLine(x_pos, m, x_pos, h - m)
            y_pos = m + i * (h - 2 * m) // 10
            painter.drawLine(m, y_pos, w - m, y_pos)

        # Ejes
        pen_eje = QPen(self.color_ejes, 2)
        painter.setPen(pen_eje)
        # eje X
        x_axis_y = int(h - m - (0 - self.y_min) / (self.y_max - self.y_min) * (h - 2 * m))
        x_axis_y = max(m, min(h - m, x_axis_y))
        painter.drawLine(m, x_axis_y, w - m, x_axis_y)
        # eje Y
        y_axis_x = int(m + (0 - self.x_min) / (self.x_max - self.x_min) * (w - 2 * m))
        y_axis_x = max(m, min(w - m, y_axis_x))
        painter.drawLine(y_axis_x, m, y_axis_x, h - m)

        # Etiquetas de ejes
        font_lbl = QFont("Arial", 8)
        painter.setFont(font_lbl)
        painter.setPen(QColor("#888888"))
        for i in range(5):
            xv = self.x_min + i * (self.x_max - self.x_min) / 4
            pt = self._mundo_a_pixel(xv, self.y_min, w, h)
            painter.drawText(pt.x() - 15, h - m + 14, f"{xv:.1f}")
            yv = self.y_min + i * (self.y_max - self.y_min) / 4
            pt2 = self._mundo_a_pixel(self.x_min, yv, w, h)
            painter.drawText(2, pt2.y() + 4, f"{yv:.1f}")

        # Título
        painter.setPen(QColor("#CCCCCC"))
        painter.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        painter.drawText(m, m - 8, self.titulo_grafica)

        # Curva
        if len(self.puntos) >= 2:
            pen_curva = QPen(self.color_curva, 2)
            painter.setPen(pen_curva)
            prev = None
            for x, y in self.puntos:
                if math.isnan(y) or math.isinf(y):
                    prev = None
                    continue
                pt = self._mundo_a_pixel(x, y, w, h)
                if prev is not None:
                    painter.drawLine(prev, pt)
                prev = pt

        painter.end()

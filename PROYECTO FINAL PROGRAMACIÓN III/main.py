import sys
import os

# Añadir la raíz del proyecto al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PySide6.QtWidgets import QApplication

from model.calculadora_modelo import CalculadoraModelo
from view.ventana_principal import VentanaPrincipal
from view.subventanas import (
    SubventanaCalculadora,
    SubventanaConversor,
    SubventanaHistorial,
    SubventanaGraficador,
)
from controller.calculadora_controlador import CalculadoraControlador


def main() -> None:
    app = QApplication(sys.argv)
    app.setApplicationName("Calculadora Científica Avanzada")
    app.setApplicationVersion("2.0.0")

    # ── 1. Modelo ──────────────────────────────────────────────────────
    modelo = CalculadoraModelo()

    # ── 2. Vista principal ─────────────────────────────────────────────
    ventana = VentanaPrincipal()

    # ── 3. Subventanas MDI ─────────────────────────────────────────────
    # Se crean SIN parent; el QMdiArea las envuelve internamente
    # al llamar addSubWindow(), que crea el QMdiSubWindow contenedor.
    sub_calc = SubventanaCalculadora()
    sub_conv = SubventanaConversor()
    sub_hist = SubventanaHistorial()
    sub_graf = SubventanaGraficador()

    ventana.mdi_area.addSubWindow(sub_calc)
    ventana.mdi_area.addSubWindow(sub_conv)
    ventana.mdi_area.addSubWindow(sub_hist)
    ventana.mdi_area.addSubWindow(sub_graf)

    # El historial siempre visible
    sub_hist.show()

    # ── 4. Controlador ─────────────────────────────────────────────────
    # Al construirse activa el modo BASICO automáticamente
    controlador = CalculadoraControlador(
        modelo=modelo,
        vista=ventana,
        sub_calc=sub_calc,
        sub_conv=sub_conv,
        sub_hist=sub_hist,
        sub_graf=sub_graf,
    )

    # Conectar resultado de calculadora al historial
    sub_calc.resultado_calculado.connect(sub_hist.recibir_resultado)

    # ── 5. Mostrar ventana principal ───────────────────────────────────
    ventana.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

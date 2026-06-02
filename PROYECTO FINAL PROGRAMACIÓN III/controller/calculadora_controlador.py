import math
from PySide6.QtCore import QObject
from PySide6.QtWidgets import QMessageBox, QInputDialog, QFileDialog

from model.calculadora_modelo import CalculadoraModelo
from model.enums import ModoCalculadora, TemaUI
from view.ventana_principal import VentanaPrincipal
from view.subventanas import (
    SubventanaCalculadora,
    SubventanaConversor,
    SubventanaHistorial,
    SubventanaGraficador,
)
from view.gestor_temas import GestorTemas
from controller.manejador_errores import ManejadorErrores, ConectadorSeñales
from controller.graficador_controlador import GraficadorControlador


class CalculadoraControlador(QObject):
    def __init__(
        self,
        modelo:    CalculadoraModelo,
        vista:     VentanaPrincipal,
        sub_calc:  SubventanaCalculadora,
        sub_conv:  SubventanaConversor,
        sub_hist:  SubventanaHistorial,
        sub_graf:  SubventanaGraficador,
        parent=None,
    ):
        super().__init__(parent)
        self.modelo: CalculadoraModelo    = modelo
        self.vista:  VentanaPrincipal     = vista
        self.expresion_buffer: str        = ""
        self._precision: int              = 6


        self.conector:     ConectadorSeñales = ConectadorSeñales()
        self.manejador:    ManejadorErrores  = ManejadorErrores(vista)
        self.gestor_temas: GestorTemas       = GestorTemas()

        self._sub_calc = sub_calc
        self._sub_conv = sub_conv
        self._sub_hist = sub_hist
        self._sub_graf = sub_graf


        fn_modelo = modelo.nueva_funcion()
        self.graficador_ctrl = GraficadorControlador(
            fn_modelo,
            sub_graf.panel_graf,
            sub_graf,
        )

        self._conectar_señales()
        self.gestor_temas.aplicar_tema(TemaUI.OSCURO)


        self._activar_modo(ModoCalculadora.BASICO)


    def _conectar_señales(self) -> None:
        m    = self.modelo
        v    = self.vista
        calc = self._sub_calc

        # Modelo → Vista
        self.conector.usar_connect(m.result_ready,          self._on_resultado)
        self.conector.usar_connect(m.error_ocurrido,        self.manejador.mostrar_qmessage)
        self.conector.usar_connect(m.historial_actualizado, self._on_historial_actualizado)


        panel = calc.panel
        for btn in panel.botones:
            txt = btn.text()
            if txt not in ("=", "C"):
                btn.clicked.disconnect()
                cb = self.conector.usar_partial(self.on_boton_presionado, txt)
                btn.clicked.connect(cb)

        panel.igual_presionado.connect(self.on_igual)
        panel.limpiar_presionado.connect(self.on_limpiar)
        panel.chk_rad.stateChanged.connect(self._on_chk_rad)


        for btn in calc.panel_cient.btns:
            txt = btn.text()
            btn.clicked.disconnect()
            cb = self.conector.usar_partial(self._on_btn_cient, txt)
            btn.clicked.connect(cb)
        calc.panel_cient.spin_prec.valueChanged.connect(self._on_precision)


        v.modo_cambiado.connect(self.on_cambio_modo)
        v.tema_cambiado.connect(self.on_cambio_tema)

        accion_hist = v.acciones.get("borrar_historial")
        if accion_hist:
            accion_hist.triggered.connect(self._on_borrar_historial)


        self._conectar_conversor()

    def _conectar_conversor(self) -> None:
        """Inicializa el panel conversor con los datos del modelo."""
        panel_conv = self._sub_conv.panel_conv
        conversor  = self.modelo.conversor

        panel_conv.init_combos(conversor.get_categorias())


        panel_conv.combo_categoria.currentTextChanged.connect(
            self._on_categoria_conv_changed
        )


        panel_conv.convertir_pedido.connect(self._on_convertir)


        conversor.conversion_done.connect(panel_conv.mostrar_resultado)


    def on_boton_presionado(self, v: str) -> None:
        mapa = {"÷": "/", "×": "*", "−": "-"}
        if v == "←":
            self.expresion_buffer = self.expresion_buffer[:-1]
        elif v == "±":
            if self.expresion_buffer:
                if self.expresion_buffer[0] == "-":
                    self.expresion_buffer = self.expresion_buffer[1:]
                else:
                    self.expresion_buffer = "-" + self.expresion_buffer
        elif v == "%":
            try:
                val = float(self.expresion_buffer) / 100
                self.expresion_buffer = str(val)
            except ValueError:
                pass
        else:
            self.expresion_buffer += mapa.get(v, v)
        self._actualizar_display()

    def on_igual(self) -> None:
        if not self.expresion_buffer.strip():
            return
        try:
            resultado = self.modelo.evaluar_expresion(self.expresion_buffer)
            self.expresion_buffer = str(round(resultado, self._precision))
        except Exception:
            self.expresion_buffer = ""
        self._actualizar_display()

    def on_limpiar(self) -> None:
        self.expresion_buffer = ""
        self._actualizar_display()

    def on_cambio_modo(self, m: ModoCalculadora) -> None:
        """
        LÓGICA CENTRAL: ocultar subventanas de modo anterior,
        mostrar solo la del nuevo modo.
        """
        self._activar_modo(m)

    def on_cambio_tema(self, t: TemaUI) -> None:
        self.gestor_temas.aplicar_tema(t)
        self.vista.aplicar_tema(t)
        self.vista.mostrar_status(f"Tema: {t.value}")

    # ── Lógica de activación de modos ─────────────────────────────────
    def _activar_modo(self, m: ModoCalculadora) -> None:
        """
        Oculta todas las subventanas de modo y muestra únicamente
        la que corresponde al modo m. El historial siempre es visible.
        """
        self.modelo.set_modo(m)
        self.vista.modo_actual = m

        # --- Ocultar todas las subventanas de modo ---
        self._sub_calc.hide()
        self._sub_conv.hide()
        self._sub_graf.hide()

        # --- Mostrar la subventana del modo seleccionado ---
        if m == ModoCalculadora.BASICO:
            self._sub_calc.mostrar_panel_cientifico(False)
            self._sub_calc.show()
            self._sub_calc.raise_()
            self.vista.mdi_area.tileSubWindows()

        elif m == ModoCalculadora.CIENTIFICO:
            self._sub_calc.mostrar_panel_cientifico(True)
            self._sub_calc.show()
            self._sub_calc.raise_()
            self.vista.mdi_area.tileSubWindows()

        elif m == ModoCalculadora.CONVERSOR:
            self._sub_conv.show()
            self._sub_conv.raise_()
            self.vista.mdi_area.tileSubWindows()

        elif m == ModoCalculadora.GRAFICADOR:
            self._sub_graf.show()
            self._sub_graf.raise_()
            self.vista.mdi_area.tileSubWindows()

        self.vista.mostrar_status(f"Modo activo: {m.value}")


    def _on_resultado(self, v: float) -> None:
        self._sub_calc.enviar_resultado(v)
        self.vista.mostrar_status(f"Resultado: {v}")

    def _on_historial_actualizado(self) -> None:
        historial = self.modelo.get_historial()
        if historial:
            self._sub_hist.historial_widget.actualizar_desde_lista(historial)

    def _on_chk_rad(self, state: int) -> None:
        from model.enums import UnidadAngulo
        from PySide6.QtCore import Qt
        self.modelo.unidad_angulo = (
            UnidadAngulo.RAD if state == 2 else UnidadAngulo.DEG
        )

    def _on_btn_cient(self, txt: str) -> None:
        mapa_func = {
            "sin":  "sin(",  "cos":  "cos(",  "tan":  "tan(",
            "asin": "asin(", "acos": "acos(", "atan": "atan(",
            "log":  "log(",  "ln":   "ln(",   "√":    "sqrt(",
            "exp":  "exp(",  "abs":  "abs(",
        }
        mapa_const = {"π": str(math.pi), "e": str(math.e)}
        mapa_op    = {"x²": "**2", "xⁿ": "**", "1/x": "1/", "EE": "e"}

        if txt in mapa_func:
            self.expresion_buffer += mapa_func[txt]
        elif txt in mapa_const:
            self.expresion_buffer += mapa_const[txt]
        elif txt in mapa_op:
            self.expresion_buffer += mapa_op[txt]
        elif txt == "n!":
            try:
                n = int(float(self.expresion_buffer))
                self.expresion_buffer = str(math.factorial(n))
            except Exception:
                pass
        elif txt in ("(", ")"):
            self.expresion_buffer += txt
        else:
            self.expresion_buffer += txt
        self._actualizar_display()

    def _on_precision(self, n: int) -> None:
        self._precision = n

    def _on_borrar_historial(self) -> None:
        resp = QMessageBox.question(
            self.vista, "Historial",
            "¿Borrar todo el historial?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if resp == QMessageBox.StandardButton.Yes:
            self.modelo.limpiar_historial()
            self._sub_hist.historial_widget.limpiar()

    def _on_categoria_conv_changed(self, nombre: str) -> None:
        """Pobla los combos de unidades cuando cambia la categoría."""
        unidades = self.modelo.conversor.get_unidades(nombre)
        self._sub_conv.panel_conv.poblar_unidades(unidades)

    def _on_convertir(self, cat: str, origen_nombre: str,
                      destino_nombre: str, val: float) -> None:
        """Ejecuta la conversión de unidades a través del modelo."""
        conversor = self.modelo.conversor
        try:
            origen  = conversor.get_unidades(cat)
            destino = conversor.get_unidades(cat)
            u_orig  = next(u for u in origen  if u.nombre == origen_nombre)
            u_dest  = next(u for u in destino if u.nombre == destino_nombre)
            conversor.convertir(u_orig, u_dest, val)
        except Exception as exc:
            self._sub_conv.panel_conv.lbl_resultado.setText(f"Error: {exc}")

    def _actualizar_display(self) -> None:
        self._sub_calc.display.set_texto(self.expresion_buffer or "0")

from typing import List
from PySide6.QtWidgets import (
    QWidget, QGridLayout, QHBoxLayout, QVBoxLayout, QFormLayout,
    QPushButton, QLabel, QLineEdit, QComboBox, QSpinBox, QCheckBox,
    QSizePolicy
)
from PySide6.QtCore import Signal, Qt

from view.display_led import DisplayLED
from view.graficador_widget import GraficadorWidget
from model.enums import TipoFuncion


# ══════════════════════════════════════════════════════════════════════
class PanelBasico(QWidget):
    boton_presionado  = Signal(str)
    igual_presionado  = Signal()
    limpiar_presionado = Signal()

    _BOTONES = [
        ["C",  "±",  "%",  "÷"],
        ["7",  "8",  "9",  "×"],
        ["4",  "5",  "6",  "−"],
        ["1",  "2",  "3",  "+"],
        ["0",  ".",  "←",  "="],
    ]

    def __init__(self, parent=None):
        super().__init__(parent)
        self.botones: List[QPushButton] = []
        self.grid_layout = QGridLayout()
        self.vbox_main   = QVBoxLayout(self)
        self.chk_rad     = QCheckBox("RAD")
        self.lbl_display = QLabel()
        self._build_ui()

    def _build_ui(self) -> None:
        self.vbox_main.setContentsMargins(4, 4, 4, 4)
        self.vbox_main.setSpacing(4)

        hbox_top = QHBoxLayout()
        hbox_top.addWidget(self.chk_rad)
        hbox_top.addStretch()
        self.vbox_main.addLayout(hbox_top)

        for row, fila in enumerate(self._BOTONES):
            for col, txt in enumerate(fila):
                btn = QPushButton(txt)
                btn.setSizePolicy(QSizePolicy.Policy.Expanding,
                                  QSizePolicy.Policy.Expanding)
                btn.setMinimumSize(52, 48)
                if txt == "=":
                    btn.setObjectName("btnIgual")
                    btn.clicked.connect(self.igual_presionado)
                elif txt == "C":
                    btn.setObjectName("btnLimpiar")
                    btn.clicked.connect(self.limpiar_presionado)
                else:
                    val = txt
                    btn.clicked.connect(
                        lambda checked=False, v=val: self.boton_presionado.emit(v)
                    )
                self.botones.append(btn)
                self.grid_layout.addWidget(btn, row, col)

        self.grid_layout.setSpacing(4)
        self.vbox_main.addLayout(self.grid_layout)

    def get_layout(self):
        return self.vbox_main

    def agregar_boton(self, txt: str) -> None:
        btn = QPushButton(txt)
        btn.clicked.connect(lambda: self.boton_presionado.emit(txt))
        self.botones.append(btn)


# ══════════════════════════════════════════════════════════════════════
class PanelCientifico(QWidget):
    boton_presionado = Signal(str)

    _BTNS_CIENT = [
        ["sin",  "cos",  "tan",  "asin"],
        ["acos", "atan", "log",  "ln"  ],
        ["√",    "x²",   "xⁿ",  "exp" ],
        ["π",    "e",    "(",    ")"   ],
        ["1/x",  "n!",   "abs",  "EE"  ],
    ]

    def __init__(self, parent=None):
        super().__init__(parent)
        self.btns: List[QPushButton] = []
        self.hbox = QHBoxLayout()
        self.vbox = QVBoxLayout(self)
        self.spin_prec = QSpinBox()
        self.lbl_modo  = QLabel("Modo Científico")
        self._build_ui()

    def _build_ui(self) -> None:
        self.vbox.setContentsMargins(4, 4, 4, 4)
        self.vbox.setSpacing(4)

        hbox_top = QHBoxLayout()
        hbox_top.addWidget(self.lbl_modo)
        hbox_top.addStretch()
        hbox_top.addWidget(QLabel("Decimales:"))
        self.spin_prec.setRange(0, 15)
        self.spin_prec.setValue(6)
        self.spin_prec.setFixedWidth(55)
        hbox_top.addWidget(self.spin_prec)
        self.vbox.addLayout(hbox_top)

        grid = QGridLayout()
        grid.setSpacing(4)
        for row, fila in enumerate(self._BTNS_CIENT):
            for col, txt in enumerate(fila):
                btn = QPushButton(txt)
                btn.setObjectName("btnCientifico")
                btn.setSizePolicy(QSizePolicy.Policy.Expanding,
                                  QSizePolicy.Policy.Expanding)
                btn.setMinimumSize(52, 40)
                btn.clicked.connect(
                    lambda checked=False, v=txt: self.boton_presionado.emit(v)
                )
                self.btns.append(btn)
                grid.addWidget(btn, row, col)
        self.vbox.addLayout(grid)

    def crear_btns_cientificos(self) -> None:
        pass  # construidos en _build_ui

    def set_precision(self, n: int) -> None:
        self.spin_prec.setValue(n)


# ══════════════════════════════════════════════════════════════════════
class PanelConversor(QWidget):
    # Señal: categoria, origen, destino, valor
    convertir_pedido = Signal(str, str, str, float)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.combo_categoria = QComboBox()
        self.combo_origen    = QComboBox()
        self.combo_destino   = QComboBox()
        self.entrada         = QLineEdit("1.0")
        self.lbl_resultado   = QLabel("Resultado: —")
        self.form_layout     = QFormLayout()
        self.hbox_combos     = QHBoxLayout()
        self._build_ui()

    def _build_ui(self) -> None:
        vbox = QVBoxLayout(self)
        vbox.setContentsMargins(12, 12, 12, 12)
        vbox.setSpacing(10)

        # Título
        lbl_titulo = QLabel("Conversión de Unidades")
        lbl_titulo.setStyleSheet("font-size: 16px; font-weight: bold;")
        vbox.addWidget(lbl_titulo)

        self.form_layout.addRow("Categoría:", self.combo_categoria)
        self.form_layout.addRow("Valor:",     self.entrada)
        vbox.addLayout(self.form_layout)

        self.hbox_combos.addWidget(QLabel("De:"))
        self.hbox_combos.addWidget(self.combo_origen)
        self.hbox_combos.addWidget(QLabel("→"))
        self.hbox_combos.addWidget(QLabel("A:"))
        self.hbox_combos.addWidget(self.combo_destino)
        vbox.addLayout(self.hbox_combos)

        btn_conv = QPushButton("Convertir")
        btn_conv.setObjectName("btnIgual")
        btn_conv.clicked.connect(self._on_convertir)
        vbox.addWidget(btn_conv)

        self.lbl_resultado.setObjectName("lblResultadoConv")
        self.lbl_resultado.setStyleSheet("font-size: 14px; font-weight: bold;")
        vbox.addWidget(self.lbl_resultado)
        vbox.addStretch()

    def _on_convertir(self) -> None:
        cat     = self.combo_categoria.currentText()
        origen  = self.combo_origen.currentText()
        destino = self.combo_destino.currentText()
        try:
            val = float(self.entrada.text().replace(",", "."))
        except ValueError:
            self.lbl_resultado.setText("Entrada inválida")
            return
        self.convertir_pedido.emit(cat, origen, destino, val)

    def init_combos(self, categorias: list) -> None:
        self.combo_categoria.clear()
        for cat in categorias:
            self.combo_categoria.addItem(cat.nombre)
        self.combo_categoria.currentTextChanged.connect(self._on_categoria_changed)
        if categorias:
            self._poblar_unidades(categorias[0].unidades)

    def _on_categoria_changed(self, nombre: str) -> None:
        # El controlador conectará la lógica real a través de la señal
        pass

    def poblar_unidades(self, unidades: list) -> None:
        self.combo_origen.clear()
        self.combo_destino.clear()
        for u in unidades:
            self.combo_origen.addItem(u.nombre)
            self.combo_destino.addItem(u.nombre)
        if len(unidades) > 1:
            self.combo_destino.setCurrentIndex(1)

    def _poblar_unidades(self, unidades: list) -> None:
        self.poblar_unidades(unidades)

    def mostrar_resultado(self, v: float) -> None:
        """Slot conectado a ConversorUnidades.conversion_done."""
        origen  = self.combo_origen.currentText()
        destino = self.combo_destino.currentText()
        val_orig = self.entrada.text()
        self.lbl_resultado.setText(
            f"Resultado: {val_orig} {origen} = {v:,.10g} {destino}"
        )


# ══════════════════════════════════════════════════════════════════════
class PanelGraficador(QWidget):
    graficar_pedido = Signal(str, float, float)   # expresion, xmin, xmax

    _FUNCIONES_PREDEFINIDAS = [
        "sin(x)", "cos(x)", "tan(x)", "x**2", "x**3",
        "sqrt(abs(x))", "exp(x/5)", "log(abs(x)+1)", "personalizada"
    ]

    def __init__(self, parent=None):
        super().__init__(parent)
        self.graficador       = GraficadorWidget()
        self.combo_funcion    = QComboBox()
        self.entry_expresion  = QLineEdit("sin(x)")
        self.spin_xmin        = QSpinBox()
        self.spin_xmax        = QSpinBox()
        self.btn_graficar     = QPushButton("Graficar")
        self.vbox             = QVBoxLayout(self)
        self.hbox_controles   = QHBoxLayout()
        self._build_ui()

    def _build_ui(self) -> None:
        self.vbox.setContentsMargins(4, 4, 4, 4)
        self.vbox.setSpacing(6)
        self.vbox.addWidget(self.graficador, stretch=1)

        # Controles
        form = QFormLayout()
        self.combo_funcion.addItems(self._FUNCIONES_PREDEFINIDAS)
        self.combo_funcion.currentTextChanged.connect(self._on_funcion_seleccionada)
        form.addRow("Función predefinida:", self.combo_funcion)
        form.addRow("Expresión f(x):",      self.entry_expresion)

        self.spin_xmin.setRange(-1000, 0);   self.spin_xmin.setValue(-10)
        self.spin_xmax.setRange(0, 1000);    self.spin_xmax.setValue(10)
        self.hbox_controles.addWidget(QLabel("x min:"))
        self.hbox_controles.addWidget(self.spin_xmin)
        self.hbox_controles.addWidget(QLabel("x max:"))
        self.hbox_controles.addWidget(self.spin_xmax)
        self.hbox_controles.addStretch()
        self.btn_graficar.setObjectName("btnIgual")
        self.hbox_controles.addWidget(self.btn_graficar)
        self.btn_graficar.clicked.connect(self.on_graficar)

        self.vbox.addLayout(form)
        self.vbox.addLayout(self.hbox_controles)

    def _on_funcion_seleccionada(self, txt: str) -> None:
        if txt != "personalizada":
            self.entry_expresion.setText(txt)

    def on_graficar(self) -> None:
        expr = self.entry_expresion.text().strip()
        self.graficador.titulo_grafica = f"f(x) = {expr}"
        self.graficar_pedido.emit(
            expr,
            float(self.spin_xmin.value()),
            float(self.spin_xmax.value())
        )

    def init_controles(self) -> None:
        pass  # construidos en _build_ui

    def actualizar_grafica(self, pts: list) -> None:
        """Slot conectado a puntos_listos vía GraficadorControlador."""
        self.graficador.set_puntos(pts)

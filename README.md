Calculadora Científica Avanzada
Proyecto Integrador — Programación III (5850) | Universidad de Nariño — Semestre 2026

Docente: Ing. Carlos Alberto Fuel Tulcán

Descripción
Calculadora de escritorio con funciones básicas y científicas, historial de operaciones, conversión de
unidades y graficación de funciones matemáticas. Desarrollada en Python con PySide6 bajo el patrón de
arquitectura MVC (Modelo–Vista–Controlador) con una interfaz MDI (Multiple Document Interface).

Estructura del Proyecto

PROYECTO FINAL PROGRAMACIÓN III/
├── main.py # Punto de entrada de la aplicación
├── requirements.txt # Dependencias del proyecto
├── calculadora.spec # Configuración de PyInstaller
├── README.md # Este archivo
├── .gitignore # Archivos ignorados por Git
│
├── model/ # Capa de datos y lógica de negocio
│ ├── __init__.py
│ ├── calculadora_modelo.py # Modelo principal (QObject + Signals)
│ ├── operacion_cientifica.py # Lógica de operaciones científicas
│ ├── conversor_unidades.py # Lógica de conversión de unidades
│ ├── funcion_grafica.py # Modelo de función matemática graficable
│ ├── unit.py # Dataclass de unidades
│ └── enums.py # Enumeraciones del dominio
│
├── view/ # Capa de presentación (Componentes en Python
puro)
│ ├── __init__.py
│ ├── ventana_principal.py # Ventana contenedora principal MDI
│ ├── subventanas.py # Gestión de subventanas de la interfaz
│ ├── paneles.py # Componentes y distribución de los paneles
│ ├── display_led.py # Widget personalizado: display tipo LED
(QPainter)
│ ├── graficador_widget.py # Widget personalizado: renderizado gráfico
2D
│ ├── historial_widget.py # Widget encargado del registro de
operaciones
│ └── gestor_temas.py # Controlador de estilos QSS
│
├── controller/ # Capa de control (Coordinación M ↔ V)
│ ├── __init__.py
│ ├── calculadora_controlador.py # Controlador general de la aplicación
│ ├── graficador_controlador.py # Controlador específico de la lógica de
gráficos
│ └── manejador_errores.py # Captura y ruteo centralizado de excepciones

1

│
├── ui/ # Archivos de interfaz y diseño (Qt
Designer / Compilados)
│ ├── subventana_calculadora.py
│ ├── ui_subventana_calculadora.py
│ ├── ui_ventana_principal.py
│ └── ventana_principal.py
│
└── ven/ # Entorno virtual de desarrollo (Python
Virtual Env)
├── Include/
├── Lib/
└── pyvenv.cfg

Requisitos
Python 3.12+
PySide6 >= 6.6.0
numpy >= 1.26.0
Instalación del entorno virtual

Ejecución

Modos de la Calculadora

Modo Atajo Descripción
Básico Ctrl+1 Operaciones aritméticas elementales (+, -, ×, ÷, %, ±).
•
•
•

# Crear entorno virtual (si no se ha creado)
python -m venv ven
# Activar en Windows
ven\Scripts ctivate
# Activar en Linux/macOS
source ven/bin/activate
# Instalar dependencias
pip install -r requirements.txt

python main.py

2

Modo Atajo Descripción
Científico Ctrl+2 Funciones trigonométricas, logarítmicas, potencias y raíces.
Conversor Ctrl+3 Conversión matricial de unidades (longitud, peso y temperatura).
Graficador Ctrl+4 Renderizado de funciones f(x) con muestreo y límites dinámicos.

Temas Visuales

Tema Atajo
Oscuro Ctrl+Shift+D
Claro Ctrl+Shift+L
Alto Contraste Ctrl+Shift+A

Generación del Ejecutable (PyInstaller)

Unidades Técnicas Cubiertas

Unidad Tema Implementación en el Proyecto
U0 OOP & MVC Arquitectura desacoplada en model/ , view/ y
controller/ usando tipado estático y
encapsulamiento.

U1 Widgets & Señales Uso exhaustivo de QPushButton , QLabel ,
QLineEdit y mapeo de eventos mediante
connect() y functools.partial .

U2 Layouts
# Instalar herramienta de empaquetado
pip install pyinstaller
# Compilar usando la configuración del archivo .spec
pyinstaller calculadora.spec
# El binario se genera en la ruta: dist/CalculadoraCientifica

3

Unidad Tema Implementación en el Proyecto
Diseños complejos y responsivos usando
QVBoxLayout , QHBoxLayout y QGridLayout
aninados.

U3 Cuadros de Diálogo Gestión de alertas e interacciones contextuales con

QMessageBox y QInputDialog .
U4 QMainWindow Ventana principal dotada de barras de menús,
herramientas ( QToolBar ) y estados ( QStatusBar ).
U5 Sub-ventanas MDI Espacio de trabajo dinámico gestionado mediante

QMdiArea y QMdiSubWindow .

U6 Tematización QSS Hojas de estilo en cascada aplicadas de manera

dinámica en gestor_temas.py .

U7 Qt Designer Estructura visual armada en la carpeta dedicada ui/
vinculando componentes nativos y generados.
U8 Widgets Propios Creación de componentes a medida ( DisplayLED y

GraficadorWidget ) sobreescribiendo
paintEvent() con QPainter .

U9 Despliegue Configuración avanzada de compilación multiplataforma

compilada en calculadora.spec .

Integrantes:
• Maria de los Angeles Solis
• Nelsy Silena Padilla Boya
• Johan Mauricio Viafara Castañeda
Contacto Docente: Ing. Carlos Alberto Fuel Tulcán — cafuel@udenar.edu.co

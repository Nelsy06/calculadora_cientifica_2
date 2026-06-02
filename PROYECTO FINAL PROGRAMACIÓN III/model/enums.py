from enum import Enum


class ModoCalculadora(Enum):
    BASICO = "BASICO"
    CIENTIFICO = "CIENTIFICO"
    CONVERSOR = "CONVERSOR"
    GRAFICADOR = "GRAFICADOR"


class TemaUI(Enum):
    OSCURO = "OSCURO"
    CLARO = "CLARO"
    ALTO_CONTRASTE = "ALTO_CONTRASTE"


class UnidadAngulo(Enum):
    DEG = "DEG"
    RAD = "RAD"
    GRAD = "GRAD"


class TipoFuncion(Enum):
    SENO = "SENO"
    COSENO = "COSENO"
    TANGENTE = "TANGENTE"
    CUADRATICA = "CUADRATICA"
    PERSONALIZADA = "PERSONALIZADA"


class TipoOperacion(Enum):
    TRIGONOMETRICA = "TRIGONOMETRICA"
    LOGARITMO = "LOGARITMO"
    POTENCIA = "POTENCIA"
    ARITMETICA = "ARITMETICA"

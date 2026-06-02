# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'subventana_calculadora.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

from view.display_led import DisplayLED

class Ui_SubventanaCalculadora(object):
    def setupUi(self, SubventanaCalculadora):
        if not SubventanaCalculadora.objectName():
            SubventanaCalculadora.setObjectName(u"SubventanaCalculadora")
        SubventanaCalculadora.resize(513, 536)
        self.vbox_main = QVBoxLayout(SubventanaCalculadora)
        self.vbox_main.setSpacing(4)
        self.vbox_main.setObjectName(u"vbox_main")
        self.vbox_main.setContentsMargins(6, 6, 6, 6)
        self.display = DisplayLED(SubventanaCalculadora)
        self.display.setObjectName(u"display")
        self.display.setMinimumSize(QSize(300, 70))

        self.vbox_main.addWidget(self.display)

        self.vbox_panel_basico = QVBoxLayout()
        self.vbox_panel_basico.setSpacing(4)
        self.vbox_panel_basico.setObjectName(u"vbox_panel_basico")
        self.vbox_panel_basico.setContentsMargins(4, 4, 4, 4)
        self.hbox_top_basico = QHBoxLayout()
        self.hbox_top_basico.setObjectName(u"hbox_top_basico")
        self.chk_rad = QCheckBox(SubventanaCalculadora)
        self.chk_rad.setObjectName(u"chk_rad")

        self.hbox_top_basico.addWidget(self.chk_rad)

        self.spacer_rad = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hbox_top_basico.addItem(self.spacer_rad)


        self.vbox_panel_basico.addLayout(self.hbox_top_basico)

        self.grid_basico = QGridLayout()
        self.grid_basico.setSpacing(4)
        self.grid_basico.setObjectName(u"grid_basico")
        self.btnLimpiar = QPushButton(SubventanaCalculadora)
        self.btnLimpiar.setObjectName(u"btnLimpiar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnLimpiar.sizePolicy().hasHeightForWidth())
        self.btnLimpiar.setSizePolicy(sizePolicy)
        self.btnLimpiar.setMinimumSize(QSize(52, 48))

        self.grid_basico.addWidget(self.btnLimpiar, 0, 0, 1, 1)

        self.btn_signo = QPushButton(SubventanaCalculadora)
        self.btn_signo.setObjectName(u"btn_signo")
        sizePolicy.setHeightForWidth(self.btn_signo.sizePolicy().hasHeightForWidth())
        self.btn_signo.setSizePolicy(sizePolicy)
        self.btn_signo.setMinimumSize(QSize(52, 48))

        self.grid_basico.addWidget(self.btn_signo, 0, 1, 1, 1)

        self.btn_pct = QPushButton(SubventanaCalculadora)
        self.btn_pct.setObjectName(u"btn_pct")
        sizePolicy.setHeightForWidth(self.btn_pct.sizePolicy().hasHeightForWidth())
        self.btn_pct.setSizePolicy(sizePolicy)
        self.btn_pct.setMinimumSize(QSize(52, 48))

        self.grid_basico.addWidget(self.btn_pct, 0, 2, 1, 1)

        self.btn_div = QPushButton(SubventanaCalculadora)
        self.btn_div.setObjectName(u"btn_div")
        sizePolicy.setHeightForWidth(self.btn_div.sizePolicy().hasHeightForWidth())
        self.btn_div.setSizePolicy(sizePolicy)
        self.btn_div.setMinimumSize(QSize(52, 48))

        self.grid_basico.addWidget(self.btn_div, 0, 3, 1, 1)

        self.btn_7 = QPushButton(SubventanaCalculadora)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        self.btn_7.setMinimumSize(QSize(52, 48))

        self.grid_basico.addWidget(self.btn_7, 1, 0, 1, 1)

        self.btn_8 = QPushButton(SubventanaCalculadora)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)
        self.btn_8.setMinimumSize(QSize(52, 48))

        self.grid_basico.addWidget(self.btn_8, 1, 1, 1, 1)

        self.btn_9 = QPushButton(SubventanaCalculadora)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)
        self.btn_9.setMinimumSize(QSize(52, 48))

        self.grid_basico.addWidget(self.btn_9, 1, 2, 1, 1)

        self.btn_mul = QPushButton(SubventanaCalculadora)
        self.btn_mul.setObjectName(u"btn_mul")
        sizePolicy.setHeightForWidth(self.btn_mul.sizePolicy().hasHeightForWidth())
        self.btn_mul.setSizePolicy(sizePolicy)
        self.btn_mul.setMinimumSize(QSize(52, 48))

        self.grid_basico.addWidget(self.btn_mul, 1, 3, 1, 1)

        self.btn_4 = QPushButton(SubventanaCalculadora)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)
        self.btn_4.setMinimumSize(QSize(52, 48))

        self.grid_basico.addWidget(self.btn_4, 2, 0, 1, 1)

        self.btn_5 = QPushButton(SubventanaCalculadora)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        self.btn_5.setMinimumSize(QSize(52, 48))

        self.grid_basico.addWidget(self.btn_5, 2, 1, 1, 1)

        self.btn_6 = QPushButton(SubventanaCalculadora)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)
        self.btn_6.setMinimumSize(QSize(52, 48))

        self.grid_basico.addWidget(self.btn_6, 2, 2, 1, 1)

        self.btn_sub = QPushButton(SubventanaCalculadora)
        self.btn_sub.setObjectName(u"btn_sub")
        sizePolicy.setHeightForWidth(self.btn_sub.sizePolicy().hasHeightForWidth())
        self.btn_sub.setSizePolicy(sizePolicy)
        self.btn_sub.setMinimumSize(QSize(52, 48))

        self.grid_basico.addWidget(self.btn_sub, 2, 3, 1, 1)

        self.btn_1 = QPushButton(SubventanaCalculadora)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        self.btn_1.setMinimumSize(QSize(52, 48))

        self.grid_basico.addWidget(self.btn_1, 3, 0, 1, 1)

        self.btn_2 = QPushButton(SubventanaCalculadora)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        self.btn_2.setMinimumSize(QSize(52, 48))

        self.grid_basico.addWidget(self.btn_2, 3, 1, 1, 1)

        self.btn_3 = QPushButton(SubventanaCalculadora)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        self.btn_3.setMinimumSize(QSize(52, 48))

        self.grid_basico.addWidget(self.btn_3, 3, 2, 1, 1)

        self.btn_add = QPushButton(SubventanaCalculadora)
        self.btn_add.setObjectName(u"btn_add")
        sizePolicy.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy)
        self.btn_add.setMinimumSize(QSize(52, 48))

        self.grid_basico.addWidget(self.btn_add, 3, 3, 1, 1)

        self.btn_0 = QPushButton(SubventanaCalculadora)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy)
        self.btn_0.setMinimumSize(QSize(52, 48))

        self.grid_basico.addWidget(self.btn_0, 4, 0, 1, 1)

        self.btn_punto = QPushButton(SubventanaCalculadora)
        self.btn_punto.setObjectName(u"btn_punto")
        sizePolicy.setHeightForWidth(self.btn_punto.sizePolicy().hasHeightForWidth())
        self.btn_punto.setSizePolicy(sizePolicy)
        self.btn_punto.setMinimumSize(QSize(52, 48))

        self.grid_basico.addWidget(self.btn_punto, 4, 1, 1, 1)

        self.btn_back = QPushButton(SubventanaCalculadora)
        self.btn_back.setObjectName(u"btn_back")
        sizePolicy.setHeightForWidth(self.btn_back.sizePolicy().hasHeightForWidth())
        self.btn_back.setSizePolicy(sizePolicy)
        self.btn_back.setMinimumSize(QSize(52, 48))

        self.grid_basico.addWidget(self.btn_back, 4, 2, 1, 1)

        self.btnIgual = QPushButton(SubventanaCalculadora)
        self.btnIgual.setObjectName(u"btnIgual")
        sizePolicy.setHeightForWidth(self.btnIgual.sizePolicy().hasHeightForWidth())
        self.btnIgual.setSizePolicy(sizePolicy)
        self.btnIgual.setMinimumSize(QSize(52, 48))

        self.grid_basico.addWidget(self.btnIgual, 4, 3, 1, 1)


        self.vbox_panel_basico.addLayout(self.grid_basico)


        self.vbox_main.addLayout(self.vbox_panel_basico)

        self.vbox_cient = QVBoxLayout()
        self.vbox_cient.setSpacing(4)
        self.vbox_cient.setObjectName(u"vbox_cient")
        self.vbox_cient.setContentsMargins(4, 4, 4, 4)
        self.hbox_cient_top = QHBoxLayout()
        self.hbox_cient_top.setObjectName(u"hbox_cient_top")
        self.lbl_modo = QLabel(SubventanaCalculadora)
        self.lbl_modo.setObjectName(u"lbl_modo")

        self.hbox_cient_top.addWidget(self.lbl_modo)

        self.spacer_cient = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hbox_cient_top.addItem(self.spacer_cient)

        self.lbl_dec = QLabel(SubventanaCalculadora)
        self.lbl_dec.setObjectName(u"lbl_dec")

        self.hbox_cient_top.addWidget(self.lbl_dec)

        self.spin_prec = QSpinBox(SubventanaCalculadora)
        self.spin_prec.setObjectName(u"spin_prec")
        self.spin_prec.setMinimum(0)
        self.spin_prec.setMaximum(15)
        self.spin_prec.setValue(6)
        self.spin_prec.setProperty(u"fixedWidth", 55)

        self.hbox_cient_top.addWidget(self.spin_prec)


        self.vbox_cient.addLayout(self.hbox_cient_top)

        self.grid_cient = QGridLayout()
        self.grid_cient.setSpacing(4)
        self.grid_cient.setObjectName(u"grid_cient")
        self.btnCientifico = QPushButton(SubventanaCalculadora)
        self.btnCientifico.setObjectName(u"btnCientifico")
        sizePolicy.setHeightForWidth(self.btnCientifico.sizePolicy().hasHeightForWidth())
        self.btnCientifico.setSizePolicy(sizePolicy)
        self.btnCientifico.setMinimumSize(QSize(52, 40))

        self.grid_cient.addWidget(self.btnCientifico, 0, 0, 1, 1)

        self.btnCientifico1 = QPushButton(SubventanaCalculadora)
        self.btnCientifico1.setObjectName(u"btnCientifico1")
        sizePolicy.setHeightForWidth(self.btnCientifico1.sizePolicy().hasHeightForWidth())
        self.btnCientifico1.setSizePolicy(sizePolicy)
        self.btnCientifico1.setMinimumSize(QSize(52, 40))

        self.grid_cient.addWidget(self.btnCientifico1, 0, 1, 1, 1)

        self.btnCientifico2 = QPushButton(SubventanaCalculadora)
        self.btnCientifico2.setObjectName(u"btnCientifico2")
        sizePolicy.setHeightForWidth(self.btnCientifico2.sizePolicy().hasHeightForWidth())
        self.btnCientifico2.setSizePolicy(sizePolicy)
        self.btnCientifico2.setMinimumSize(QSize(52, 40))

        self.grid_cient.addWidget(self.btnCientifico2, 0, 2, 1, 1)

        self.btnCientifico3 = QPushButton(SubventanaCalculadora)
        self.btnCientifico3.setObjectName(u"btnCientifico3")
        sizePolicy.setHeightForWidth(self.btnCientifico3.sizePolicy().hasHeightForWidth())
        self.btnCientifico3.setSizePolicy(sizePolicy)
        self.btnCientifico3.setMinimumSize(QSize(52, 40))

        self.grid_cient.addWidget(self.btnCientifico3, 0, 3, 1, 1)

        self.btnCientifico4 = QPushButton(SubventanaCalculadora)
        self.btnCientifico4.setObjectName(u"btnCientifico4")
        sizePolicy.setHeightForWidth(self.btnCientifico4.sizePolicy().hasHeightForWidth())
        self.btnCientifico4.setSizePolicy(sizePolicy)
        self.btnCientifico4.setMinimumSize(QSize(52, 40))

        self.grid_cient.addWidget(self.btnCientifico4, 1, 0, 1, 1)

        self.btnCientifico5 = QPushButton(SubventanaCalculadora)
        self.btnCientifico5.setObjectName(u"btnCientifico5")
        sizePolicy.setHeightForWidth(self.btnCientifico5.sizePolicy().hasHeightForWidth())
        self.btnCientifico5.setSizePolicy(sizePolicy)
        self.btnCientifico5.setMinimumSize(QSize(52, 40))

        self.grid_cient.addWidget(self.btnCientifico5, 1, 1, 1, 1)

        self.btnCientifico6 = QPushButton(SubventanaCalculadora)
        self.btnCientifico6.setObjectName(u"btnCientifico6")
        sizePolicy.setHeightForWidth(self.btnCientifico6.sizePolicy().hasHeightForWidth())
        self.btnCientifico6.setSizePolicy(sizePolicy)
        self.btnCientifico6.setMinimumSize(QSize(52, 40))

        self.grid_cient.addWidget(self.btnCientifico6, 1, 2, 1, 1)

        self.btnCientifico7 = QPushButton(SubventanaCalculadora)
        self.btnCientifico7.setObjectName(u"btnCientifico7")
        sizePolicy.setHeightForWidth(self.btnCientifico7.sizePolicy().hasHeightForWidth())
        self.btnCientifico7.setSizePolicy(sizePolicy)
        self.btnCientifico7.setMinimumSize(QSize(52, 40))

        self.grid_cient.addWidget(self.btnCientifico7, 1, 3, 1, 1)

        self.btnCientifico8 = QPushButton(SubventanaCalculadora)
        self.btnCientifico8.setObjectName(u"btnCientifico8")
        sizePolicy.setHeightForWidth(self.btnCientifico8.sizePolicy().hasHeightForWidth())
        self.btnCientifico8.setSizePolicy(sizePolicy)
        self.btnCientifico8.setMinimumSize(QSize(52, 40))

        self.grid_cient.addWidget(self.btnCientifico8, 2, 0, 1, 1)

        self.btnCientifico9 = QPushButton(SubventanaCalculadora)
        self.btnCientifico9.setObjectName(u"btnCientifico9")
        sizePolicy.setHeightForWidth(self.btnCientifico9.sizePolicy().hasHeightForWidth())
        self.btnCientifico9.setSizePolicy(sizePolicy)
        self.btnCientifico9.setMinimumSize(QSize(52, 40))

        self.grid_cient.addWidget(self.btnCientifico9, 2, 1, 1, 1)

        self.btnCientifico10 = QPushButton(SubventanaCalculadora)
        self.btnCientifico10.setObjectName(u"btnCientifico10")
        sizePolicy.setHeightForWidth(self.btnCientifico10.sizePolicy().hasHeightForWidth())
        self.btnCientifico10.setSizePolicy(sizePolicy)
        self.btnCientifico10.setMinimumSize(QSize(52, 40))

        self.grid_cient.addWidget(self.btnCientifico10, 2, 2, 1, 1)

        self.btnCientifico11 = QPushButton(SubventanaCalculadora)
        self.btnCientifico11.setObjectName(u"btnCientifico11")
        sizePolicy.setHeightForWidth(self.btnCientifico11.sizePolicy().hasHeightForWidth())
        self.btnCientifico11.setSizePolicy(sizePolicy)
        self.btnCientifico11.setMinimumSize(QSize(52, 40))

        self.grid_cient.addWidget(self.btnCientifico11, 2, 3, 1, 1)

        self.btnCientifico12 = QPushButton(SubventanaCalculadora)
        self.btnCientifico12.setObjectName(u"btnCientifico12")
        sizePolicy.setHeightForWidth(self.btnCientifico12.sizePolicy().hasHeightForWidth())
        self.btnCientifico12.setSizePolicy(sizePolicy)
        self.btnCientifico12.setMinimumSize(QSize(52, 40))

        self.grid_cient.addWidget(self.btnCientifico12, 3, 0, 1, 1)

        self.btnCientifico13 = QPushButton(SubventanaCalculadora)
        self.btnCientifico13.setObjectName(u"btnCientifico13")
        sizePolicy.setHeightForWidth(self.btnCientifico13.sizePolicy().hasHeightForWidth())
        self.btnCientifico13.setSizePolicy(sizePolicy)
        self.btnCientifico13.setMinimumSize(QSize(52, 40))

        self.grid_cient.addWidget(self.btnCientifico13, 3, 1, 1, 1)

        self.btnCientifico14 = QPushButton(SubventanaCalculadora)
        self.btnCientifico14.setObjectName(u"btnCientifico14")
        sizePolicy.setHeightForWidth(self.btnCientifico14.sizePolicy().hasHeightForWidth())
        self.btnCientifico14.setSizePolicy(sizePolicy)
        self.btnCientifico14.setMinimumSize(QSize(52, 40))

        self.grid_cient.addWidget(self.btnCientifico14, 3, 2, 1, 1)

        self.btnCientifico15 = QPushButton(SubventanaCalculadora)
        self.btnCientifico15.setObjectName(u"btnCientifico15")
        sizePolicy.setHeightForWidth(self.btnCientifico15.sizePolicy().hasHeightForWidth())
        self.btnCientifico15.setSizePolicy(sizePolicy)
        self.btnCientifico15.setMinimumSize(QSize(52, 40))

        self.grid_cient.addWidget(self.btnCientifico15, 3, 3, 1, 1)

        self.btnCientifico16 = QPushButton(SubventanaCalculadora)
        self.btnCientifico16.setObjectName(u"btnCientifico16")
        sizePolicy.setHeightForWidth(self.btnCientifico16.sizePolicy().hasHeightForWidth())
        self.btnCientifico16.setSizePolicy(sizePolicy)
        self.btnCientifico16.setMinimumSize(QSize(52, 40))

        self.grid_cient.addWidget(self.btnCientifico16, 4, 0, 1, 1)

        self.btnCientifico17 = QPushButton(SubventanaCalculadora)
        self.btnCientifico17.setObjectName(u"btnCientifico17")
        sizePolicy.setHeightForWidth(self.btnCientifico17.sizePolicy().hasHeightForWidth())
        self.btnCientifico17.setSizePolicy(sizePolicy)
        self.btnCientifico17.setMinimumSize(QSize(52, 40))

        self.grid_cient.addWidget(self.btnCientifico17, 4, 1, 1, 1)

        self.btnCientifico18 = QPushButton(SubventanaCalculadora)
        self.btnCientifico18.setObjectName(u"btnCientifico18")
        sizePolicy.setHeightForWidth(self.btnCientifico18.sizePolicy().hasHeightForWidth())
        self.btnCientifico18.setSizePolicy(sizePolicy)
        self.btnCientifico18.setMinimumSize(QSize(52, 40))

        self.grid_cient.addWidget(self.btnCientifico18, 4, 2, 1, 1)

        self.btnCientifico19 = QPushButton(SubventanaCalculadora)
        self.btnCientifico19.setObjectName(u"btnCientifico19")
        sizePolicy.setHeightForWidth(self.btnCientifico19.sizePolicy().hasHeightForWidth())
        self.btnCientifico19.setSizePolicy(sizePolicy)
        self.btnCientifico19.setMinimumSize(QSize(52, 40))

        self.grid_cient.addWidget(self.btnCientifico19, 4, 3, 1, 1)


        self.vbox_cient.addLayout(self.grid_cient)


        self.vbox_main.addLayout(self.vbox_cient)


        self.retranslateUi(SubventanaCalculadora)

        QMetaObject.connectSlotsByName(SubventanaCalculadora)
    # setupUi

    def retranslateUi(self, SubventanaCalculadora):
        SubventanaCalculadora.setWindowTitle(QCoreApplication.translate("SubventanaCalculadora", u"Calculadora \u2014 Modo B\u00e1sico", None))
        self.chk_rad.setText(QCoreApplication.translate("SubventanaCalculadora", u"RAD", None))
        self.btnLimpiar.setText(QCoreApplication.translate("SubventanaCalculadora", u"C", None))
        self.btn_signo.setText(QCoreApplication.translate("SubventanaCalculadora", u"\u00b1", None))
        self.btn_pct.setText(QCoreApplication.translate("SubventanaCalculadora", u"%", None))
        self.btn_div.setText(QCoreApplication.translate("SubventanaCalculadora", u"\u00f7", None))
        self.btn_7.setText(QCoreApplication.translate("SubventanaCalculadora", u"7", None))
        self.btn_8.setText(QCoreApplication.translate("SubventanaCalculadora", u"8", None))
        self.btn_9.setText(QCoreApplication.translate("SubventanaCalculadora", u"9", None))
        self.btn_mul.setText(QCoreApplication.translate("SubventanaCalculadora", u"\u00d7", None))
        self.btn_4.setText(QCoreApplication.translate("SubventanaCalculadora", u"4", None))
        self.btn_5.setText(QCoreApplication.translate("SubventanaCalculadora", u"5", None))
        self.btn_6.setText(QCoreApplication.translate("SubventanaCalculadora", u"6", None))
        self.btn_sub.setText(QCoreApplication.translate("SubventanaCalculadora", u"\u2212", None))
        self.btn_1.setText(QCoreApplication.translate("SubventanaCalculadora", u"1", None))
        self.btn_2.setText(QCoreApplication.translate("SubventanaCalculadora", u"2", None))
        self.btn_3.setText(QCoreApplication.translate("SubventanaCalculadora", u"3", None))
        self.btn_add.setText(QCoreApplication.translate("SubventanaCalculadora", u"+", None))
        self.btn_0.setText(QCoreApplication.translate("SubventanaCalculadora", u"0", None))
        self.btn_punto.setText(QCoreApplication.translate("SubventanaCalculadora", u".", None))
        self.btn_back.setText(QCoreApplication.translate("SubventanaCalculadora", u"\u2190", None))
        self.btnIgual.setText(QCoreApplication.translate("SubventanaCalculadora", u"=", None))
        self.lbl_modo.setText(QCoreApplication.translate("SubventanaCalculadora", u"Modo Cient\u00edfico", None))
        self.lbl_dec.setText(QCoreApplication.translate("SubventanaCalculadora", u"Decimales:", None))
        self.btnCientifico.setText(QCoreApplication.translate("SubventanaCalculadora", u"sin", None))
        self.btnCientifico1.setText(QCoreApplication.translate("SubventanaCalculadora", u"cos", None))
        self.btnCientifico2.setText(QCoreApplication.translate("SubventanaCalculadora", u"tan", None))
        self.btnCientifico3.setText(QCoreApplication.translate("SubventanaCalculadora", u"asin", None))
        self.btnCientifico4.setText(QCoreApplication.translate("SubventanaCalculadora", u"acos", None))
        self.btnCientifico5.setText(QCoreApplication.translate("SubventanaCalculadora", u"atan", None))
        self.btnCientifico6.setText(QCoreApplication.translate("SubventanaCalculadora", u"log", None))
        self.btnCientifico7.setText(QCoreApplication.translate("SubventanaCalculadora", u"ln", None))
        self.btnCientifico8.setText(QCoreApplication.translate("SubventanaCalculadora", u"\u221a", None))
        self.btnCientifico9.setText(QCoreApplication.translate("SubventanaCalculadora", u"x\u00b2", None))
        self.btnCientifico10.setText(QCoreApplication.translate("SubventanaCalculadora", u"x\u207f", None))
        self.btnCientifico11.setText(QCoreApplication.translate("SubventanaCalculadora", u"exp", None))
        self.btnCientifico12.setText(QCoreApplication.translate("SubventanaCalculadora", u"\u03c0", None))
        self.btnCientifico13.setText(QCoreApplication.translate("SubventanaCalculadora", u"e", None))
        self.btnCientifico14.setText(QCoreApplication.translate("SubventanaCalculadora", u"(", None))
        self.btnCientifico15.setText(QCoreApplication.translate("SubventanaCalculadora", u")", None))
        self.btnCientifico16.setText(QCoreApplication.translate("SubventanaCalculadora", u"1/x", None))
        self.btnCientifico17.setText(QCoreApplication.translate("SubventanaCalculadora", u"n!", None))
        self.btnCientifico18.setText(QCoreApplication.translate("SubventanaCalculadora", u"abs", None))
        self.btnCientifico19.setText(QCoreApplication.translate("SubventanaCalculadora", u"EE", None))
    # retranslateUi


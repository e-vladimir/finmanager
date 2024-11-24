# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_rulevhFXGF.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QPlainTextEdit,
    QSizePolicy, QStatusBar, QWidget)

class Ui_frm_rule(object):
    def setupUi(self, frm_rule):
        if not frm_rule.objectName():
            frm_rule.setObjectName(u"frm_rule")
        frm_rule.resize(640, 320)
        self.centralwidget = QWidget(frm_rule)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.edit_input = QPlainTextEdit(self.centralwidget)
        self.edit_input.setObjectName(u"edit_input")
        self.edit_input.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)

        self.horizontalLayout.addWidget(self.edit_input)

        self.edit_output = QPlainTextEdit(self.centralwidget)
        self.edit_output.setObjectName(u"edit_output")
        self.edit_output.setBackgroundVisible(False)
        self.edit_output.setCenterOnScroll(False)

        self.horizontalLayout.addWidget(self.edit_output)

        frm_rule.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(frm_rule)
        self.statusbar.setObjectName(u"statusbar")
        frm_rule.setStatusBar(self.statusbar)

        self.retranslateUi(frm_rule)

        QMetaObject.connectSlotsByName(frm_rule)
    # setupUi

    def retranslateUi(self, frm_rule):
        frm_rule.setWindowTitle(QCoreApplication.translate("frm_rule", u"MainWindow", None))
        self.edit_input.setPlaceholderText(QCoreApplication.translate("frm_rule", u"\u0424\u0440\u0430\u0433\u043c\u0435\u043d\u0442\u044b \u043f\u043e\u0438\u0441\u043a\u0430", None))
        self.edit_output.setPlaceholderText(QCoreApplication.translate("frm_rule", u"\u0417\u0430\u043c\u0435\u043d\u0430 \u043d\u0430 \u0444\u0440\u0430\u0433\u043c\u0435\u043d\u0442", None))
    # retranslateUi


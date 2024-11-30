# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_control_autoreplaceyerthf.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHeaderView, QMainWindow,
    QSizePolicy, QStatusBar, QTableView, QVBoxLayout,
    QWidget)

class Ui_frm_control_autoreplace(object):
    def setupUi(self, frm_control_autoreplace):
        if not frm_control_autoreplace.objectName():
            frm_control_autoreplace.setObjectName(u"frm_control_autoreplace")
        frm_control_autoreplace.resize(800, 550)
        self.centralwidget = QWidget(frm_control_autoreplace)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.table_data = QTableView(self.centralwidget)
        self.table_data.setObjectName(u"table_data")
        self.table_data.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.table_data.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_data.setAlternatingRowColors(True)
        self.table_data.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table_data.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_data.horizontalHeader().setStretchLastSection(True)
        self.table_data.verticalHeader().setVisible(False)
        self.table_data.verticalHeader().setMinimumSectionSize(20)
        self.table_data.verticalHeader().setDefaultSectionSize(20)

        self.verticalLayout.addWidget(self.table_data)

        frm_control_autoreplace.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(frm_control_autoreplace)
        self.statusbar.setObjectName(u"statusbar")
        frm_control_autoreplace.setStatusBar(self.statusbar)

        self.retranslateUi(frm_control_autoreplace)

        QMetaObject.connectSlotsByName(frm_control_autoreplace)
    # setupUi

    def retranslateUi(self, frm_control_autoreplace):
        frm_control_autoreplace.setWindowTitle(QCoreApplication.translate("frm_control_autoreplace", u"MainWindow", None))
    # retranslateUi


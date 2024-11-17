# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formiLXKUf.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHeaderView, QMainWindow,
    QSizePolicy, QStatusBar, QTabWidget, QTableView,
    QVBoxLayout, QWidget)

class Ui_frm_import(object):
    def setupUi(self, frm_import):
        if not frm_import.objectName():
            frm_import.setObjectName(u"frm_import")
        frm_import.resize(800, 600)
        self.centralwidget = QWidget(frm_import)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.tabs_main = QTabWidget(self.centralwidget)
        self.tabs_main.setObjectName(u"tabs_main")
        self.tab_operations = QWidget()
        self.tab_operations.setObjectName(u"tab_operations")
        self.verticalLayout_2 = QVBoxLayout(self.tab_operations)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.table_operations_data = QTableView(self.tab_operations)
        self.table_operations_data.setObjectName(u"table_operations_data")
        self.table_operations_data.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.table_operations_data.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_operations_data.setAlternatingRowColors(True)
        self.table_operations_data.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table_operations_data.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_operations_data.verticalHeader().setMinimumSectionSize(20)
        self.table_operations_data.verticalHeader().setDefaultSectionSize(20)
        self.table_operations_data.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.table_operations_data)

        self.tabs_main.addTab(self.tab_operations, "")

        self.verticalLayout.addWidget(self.tabs_main)

        frm_import.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(frm_import)
        self.statusbar.setObjectName(u"statusbar")
        frm_import.setStatusBar(self.statusbar)

        self.retranslateUi(frm_import)

        self.tabs_main.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(frm_import)
    # setupUi

    def retranslateUi(self, frm_import):
        frm_import.setWindowTitle(QCoreApplication.translate("frm_import", u"MainWindow", None))
        self.tabs_main.setTabText(self.tabs_main.indexOf(self.tab_operations), QCoreApplication.translate("frm_import", u"\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u0438", None))
    # retranslateUi


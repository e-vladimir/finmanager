# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_finstatisticsslFAGS.ui'
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
    QSizePolicy, QStatusBar, QTableView, QVBoxLayout,
    QWidget)

class Ui_form_finstatistics(object):
    def setupUi(self, form_finstatistics):
        if not form_finstatistics.objectName():
            form_finstatistics.setObjectName(u"form_finstatistics")
        form_finstatistics.resize(800, 640)
        self.centralwidget = QWidget(form_finstatistics)
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
        self.table_data.setShowGrid(False)
        self.table_data.horizontalHeader().setMinimumSectionSize(20)
        self.table_data.verticalHeader().setVisible(False)
        self.table_data.verticalHeader().setMinimumSectionSize(20)
        self.table_data.verticalHeader().setDefaultSectionSize(20)

        self.verticalLayout.addWidget(self.table_data)

        form_finstatistics.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(form_finstatistics)
        self.statusbar.setObjectName(u"statusbar")
        form_finstatistics.setStatusBar(self.statusbar)

        self.retranslateUi(form_finstatistics)

        QMetaObject.connectSlotsByName(form_finstatistics)
    # setupUi

    def retranslateUi(self, form_finstatistics):
        form_finstatistics.setWindowTitle(QCoreApplication.translate("form_finstatistics", u"MainWindow", None))
    # retranslateUi


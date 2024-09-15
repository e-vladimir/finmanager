# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_exportiXJOJe.ui'
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

class Ui_form_export(object):
    def setupUi(self, form_export):
        if not form_export.objectName():
            form_export.setObjectName(u"form_export")
        form_export.resize(800, 480)
        self.centralwidget = QWidget(form_export)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabs_main = QTabWidget(self.centralwidget)
        self.tabs_main.setObjectName(u"tabs_main")
        self.tab_export_finactions = QWidget()
        self.tab_export_finactions.setObjectName(u"tab_export_finactions")
        self.verticalLayout_2 = QVBoxLayout(self.tab_export_finactions)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.table_finactions_data = QTableView(self.tab_export_finactions)
        self.table_finactions_data.setObjectName(u"table_finactions_data")
        self.table_finactions_data.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.table_finactions_data.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_finactions_data.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table_finactions_data.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_finactions_data.setShowGrid(False)
        self.table_finactions_data.setWordWrap(False)
        self.table_finactions_data.horizontalHeader().setVisible(False)
        self.table_finactions_data.horizontalHeader().setMinimumSectionSize(20)
        self.table_finactions_data.horizontalHeader().setStretchLastSection(True)
        self.table_finactions_data.verticalHeader().setVisible(False)
        self.table_finactions_data.verticalHeader().setMinimumSectionSize(20)
        self.table_finactions_data.verticalHeader().setDefaultSectionSize(20)
        self.table_finactions_data.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_2.addWidget(self.table_finactions_data)

        self.tabs_main.addTab(self.tab_export_finactions, "")

        self.verticalLayout.addWidget(self.tabs_main)

        form_export.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(form_export)
        self.statusbar.setObjectName(u"statusbar")
        form_export.setStatusBar(self.statusbar)

        self.retranslateUi(form_export)

        self.tabs_main.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(form_export)
    # setupUi

    def retranslateUi(self, form_export):
        form_export.setWindowTitle(QCoreApplication.translate("form_export", u"MainWindow", None))
        self.tabs_main.setTabText(self.tabs_main.indexOf(self.tab_export_finactions), QCoreApplication.translate("form_export", u"\u0424\u0438\u043d\u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f", None))
    # retranslateUi


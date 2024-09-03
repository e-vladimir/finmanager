# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_importGMsQaH.ui'
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

class Ui_form_import(object):
    def setupUi(self, form_import):
        if not form_import.objectName():
            form_import.setObjectName(u"form_import")
        form_import.resize(1000, 640)
        self.centralwidget = QWidget(form_import)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabs_main = QTabWidget(self.centralwidget)
        self.tabs_main.setObjectName(u"tabs_main")
        self.tab_import_finactions = QWidget()
        self.tab_import_finactions.setObjectName(u"tab_import_finactions")
        self.verticalLayout_2 = QVBoxLayout(self.tab_import_finactions)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.table_import_finactions_data = QTableView(self.tab_import_finactions)
        self.table_import_finactions_data.setObjectName(u"table_import_finactions_data")
        self.table_import_finactions_data.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.table_import_finactions_data.setStyleSheet(u"QTableView {\n"
"border: 1px solid #BBBBBB;\n"
"border-radius: 3px;\n"
"padding: 1px;\n"
"}")
        self.table_import_finactions_data.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_import_finactions_data.setAlternatingRowColors(True)
        self.table_import_finactions_data.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table_import_finactions_data.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectColumns)
        self.table_import_finactions_data.setShowGrid(False)
        self.table_import_finactions_data.horizontalHeader().setVisible(True)
        self.table_import_finactions_data.horizontalHeader().setMinimumSectionSize(20)
        self.table_import_finactions_data.horizontalHeader().setDefaultSectionSize(100)
        self.table_import_finactions_data.horizontalHeader().setStretchLastSection(True)
        self.table_import_finactions_data.verticalHeader().setVisible(False)
        self.table_import_finactions_data.verticalHeader().setMinimumSectionSize(20)
        self.table_import_finactions_data.verticalHeader().setDefaultSectionSize(20)
        self.table_import_finactions_data.verticalHeader().setHighlightSections(False)
        self.table_import_finactions_data.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_2.addWidget(self.table_import_finactions_data)

        self.tabs_main.addTab(self.tab_import_finactions, "")

        self.verticalLayout.addWidget(self.tabs_main)

        form_import.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(form_import)
        self.statusbar.setObjectName(u"statusbar")
        form_import.setStatusBar(self.statusbar)

        self.retranslateUi(form_import)

        self.tabs_main.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(form_import)
    # setupUi

    def retranslateUi(self, form_import):
        form_import.setWindowTitle(QCoreApplication.translate("form_import", u"MainWindow", None))
        self.tabs_main.setTabText(self.tabs_main.indexOf(self.tab_import_finactions), QCoreApplication.translate("form_import", u"\u0424\u0438\u043d\u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f", None))
    # retranslateUi


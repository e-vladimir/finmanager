# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_statisticUFGyoJ.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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

class Ui_frm_statistic(object):
    def setupUi(self, frm_statistic):
        if not frm_statistic.objectName():
            frm_statistic.setObjectName(u"frm_statistic")
        frm_statistic.resize(800, 800)
        self.centralwidget = QWidget(frm_statistic)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.tabs_main = QTabWidget(self.centralwidget)
        self.tabs_main.setObjectName(u"tabs_main")
        self.tab_statistic = QWidget()
        self.tab_statistic.setObjectName(u"tab_statistic")
        self.verticalLayout_2 = QVBoxLayout(self.tab_statistic)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.table_statistic = QTableView(self.tab_statistic)
        self.table_statistic.setObjectName(u"table_statistic")
        self.table_statistic.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.table_statistic.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_statistic.setAlternatingRowColors(True)
        self.table_statistic.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table_statistic.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_statistic.verticalHeader().setVisible(False)
        self.table_statistic.verticalHeader().setMinimumSectionSize(20)
        self.table_statistic.verticalHeader().setDefaultSectionSize(20)
        self.table_statistic.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.table_statistic)

        self.tabs_main.addTab(self.tab_statistic, "")

        self.verticalLayout.addWidget(self.tabs_main)

        frm_statistic.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(frm_statistic)
        self.statusbar.setObjectName(u"statusbar")
        frm_statistic.setStatusBar(self.statusbar)

        self.retranslateUi(frm_statistic)

        self.tabs_main.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(frm_statistic)
    # setupUi

    def retranslateUi(self, frm_statistic):
        frm_statistic.setWindowTitle(QCoreApplication.translate("frm_statistic", u"MainWindow", None))
        self.tabs_main.setTabText(self.tabs_main.indexOf(self.tab_statistic), QCoreApplication.translate("frm_statistic", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
    # retranslateUi


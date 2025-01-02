# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_statisticVyCWqW.ui'
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
    QSizePolicy, QStatusBar, QTabWidget, QTreeView,
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
        self.tab_statistic_struct = QWidget()
        self.tab_statistic_struct.setObjectName(u"tab_statistic_struct")
        self.verticalLayout_4 = QVBoxLayout(self.tab_statistic_struct)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tree_statistic_struct = QTreeView(self.tab_statistic_struct)
        self.tree_statistic_struct.setObjectName(u"tree_statistic_struct")
        self.tree_statistic_struct.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tree_statistic_struct.setAlternatingRowColors(True)
        self.tree_statistic_struct.setRootIsDecorated(False)
        self.tree_statistic_struct.setItemsExpandable(True)
        self.tree_statistic_struct.header().setVisible(True)
        self.tree_statistic_struct.header().setMinimumSectionSize(30)
        self.tree_statistic_struct.header().setStretchLastSection(False)

        self.verticalLayout_4.addWidget(self.tree_statistic_struct)

        self.tabs_main.addTab(self.tab_statistic_struct, "")

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
        self.tabs_main.setTabText(self.tabs_main.indexOf(self.tab_statistic_struct), QCoreApplication.translate("frm_statistic", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 (\u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u043d\u0430\u044f)", None))
    # retranslateUi


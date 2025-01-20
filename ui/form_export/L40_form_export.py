# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_exportkBbxhU.ui'
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
    QSizePolicy, QStatusBar, QTabWidget, QTreeView,
    QVBoxLayout, QWidget)

class Ui_frm_export(object):
    def setupUi(self, frm_export):
        if not frm_export.objectName():
            frm_export.setObjectName(u"frm_export")
        frm_export.resize(640, 480)
        self.centralwidget = QWidget(frm_export)
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
        self.tree_data_operations = QTreeView(self.tab_operations)
        self.tree_data_operations.setObjectName(u"tree_data_operations")
        self.tree_data_operations.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tree_data_operations.setStyleSheet(u"QTreeView::branch { \n"
"	border: none; \n"
"}")
        self.tree_data_operations.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tree_data_operations.setAlternatingRowColors(True)
        self.tree_data_operations.setRootIsDecorated(False)
        self.tree_data_operations.setItemsExpandable(False)
        self.tree_data_operations.setExpandsOnDoubleClick(False)
        self.tree_data_operations.header().setVisible(False)

        self.verticalLayout_2.addWidget(self.tree_data_operations)

        self.tabs_main.addTab(self.tab_operations, "")

        self.verticalLayout.addWidget(self.tabs_main)

        frm_export.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(frm_export)
        self.statusbar.setObjectName(u"statusbar")
        frm_export.setStatusBar(self.statusbar)

        self.retranslateUi(frm_export)

        self.tabs_main.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(frm_export)
    # setupUi

    def retranslateUi(self, frm_export):
        frm_export.setWindowTitle(QCoreApplication.translate("frm_export", u"MainWindow", None))
        self.tabs_main.setTabText(self.tabs_main.indexOf(self.tab_operations), QCoreApplication.translate("frm_export", u"\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u0438", None))
    # retranslateUi


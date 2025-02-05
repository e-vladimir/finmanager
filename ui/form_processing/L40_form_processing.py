# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_operationsjWNbUK.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QMainWindow, QSizePolicy, QStatusBar, QTabWidget,
    QTreeView, QVBoxLayout, QWidget)

class Ui_form_processing(object):
    def setupUi(self, form_processing):
        if not form_processing.objectName():
            form_processing.setObjectName(u"form_processing")
        form_processing.resize(800, 640)
        self.centralwidget = QWidget(form_processing)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabs_main = QTabWidget(self.centralwidget)
        self.tabs_main.setObjectName(u"tabs_main")
        self.tab_operations = QWidget()
        self.tab_operations.setObjectName(u"tab_operations")
        self.verticalLayout = QVBoxLayout(self.tab_operations)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tree_data_operations = QTreeView(self.tab_operations)
        self.tree_data_operations.setObjectName(u"tree_data_operations")
        self.tree_data_operations.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tree_data_operations.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tree_data_operations.setAlternatingRowColors(True)
        self.tree_data_operations.setRootIsDecorated(False)
        self.tree_data_operations.setItemsExpandable(False)
        self.tree_data_operations.setExpandsOnDoubleClick(False)
        self.tree_data_operations.header().setVisible(False)
        self.tree_data_operations.header().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.tree_data_operations)

        self.tabs_main.addTab(self.tab_operations, "")

        self.horizontalLayout.addWidget(self.tabs_main)

        form_processing.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(form_processing)
        self.statusbar.setObjectName(u"statusbar")
        form_processing.setStatusBar(self.statusbar)

        self.retranslateUi(form_processing)

        self.tabs_main.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(form_processing)
    # setupUi

    def retranslateUi(self, form_processing):
        form_processing.setWindowTitle(QCoreApplication.translate("form_processing", u"MainWindow", None))
        self.tabs_main.setTabText(self.tabs_main.indexOf(self.tab_operations), QCoreApplication.translate("form_processing", u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0439", None))
    # retranslateUi


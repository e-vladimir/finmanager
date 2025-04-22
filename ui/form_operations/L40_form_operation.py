# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_operationshbpacJ.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
    QMainWindow, QSizePolicy, QStatusBar, QTreeView,
    QWidget)

class Ui_form_operations(object):
    def setupUi(self, form_operations):
        if not form_operations.objectName():
            form_operations.setObjectName(u"form_operations")
        form_operations.resize(800, 600)
        self.centralwidget = QWidget(form_operations)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.TreeData = QTreeView(self.centralwidget)
        self.TreeData.setObjectName(u"TreeData")
        self.TreeData.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.TreeData.setStyleSheet(u"QTreeView {\n"
"background: white;\n"
"border: 1px solid lightgray;\n"
"border-radius: 5px;\n"
"padding: 3px;\n"
"}")
        self.TreeData.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.TreeData.setAlternatingRowColors(False)
        self.TreeData.setRootIsDecorated(False)
        self.TreeData.setItemsExpandable(False)
        self.TreeData.setExpandsOnDoubleClick(False)

        self.horizontalLayout.addWidget(self.TreeData)

        form_operations.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(form_operations)
        self.statusbar.setObjectName(u"statusbar")
        form_operations.setStatusBar(self.statusbar)

        self.retranslateUi(form_operations)

        QMetaObject.connectSlotsByName(form_operations)
    # setupUi

    def retranslateUi(self, form_operations):
        form_operations.setWindowTitle(QCoreApplication.translate("form_operations", u"MainWindow", None))
    # retranslateUi


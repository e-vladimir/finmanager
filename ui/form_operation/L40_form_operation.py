# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_operationgxhQaq.ui'
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
    QSizePolicy, QStatusBar, QTreeView, QVBoxLayout,
    QWidget)

class Ui_frm_operation(object):
    def setupUi(self, frm_operation):
        if not frm_operation.objectName():
            frm_operation.setObjectName(u"frm_operation")
        frm_operation.resize(640, 640)
        self.centralwidget = QWidget(frm_operation)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tree_data = QTreeView(self.centralwidget)
        self.tree_data.setObjectName(u"tree_data")
        self.tree_data.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tree_data.setStyleSheet(u"QTreeView::branch { \n"
"	border: none; \n"
"}")
        self.tree_data.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tree_data.setAlternatingRowColors(True)
        self.tree_data.setRootIsDecorated(False)
        self.tree_data.setItemsExpandable(False)
        self.tree_data.setExpandsOnDoubleClick(False)
        self.tree_data.header().setVisible(False)

        self.verticalLayout.addWidget(self.tree_data)

        frm_operation.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(frm_operation)
        self.statusbar.setObjectName(u"statusbar")
        frm_operation.setStatusBar(self.statusbar)

        self.retranslateUi(frm_operation)

        QMetaObject.connectSlotsByName(frm_operation)
    # setupUi

    def retranslateUi(self, frm_operation):
        frm_operation.setWindowTitle(QCoreApplication.translate("frm_operation", u"MainWindow", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_operationsNuhjBv.ui'
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

class Ui_frm_operations(object):
    def setupUi(self, frm_operations):
        if not frm_operations.objectName():
            frm_operations.setObjectName(u"frm_operations")
        frm_operations.resize(1024, 768)
        self.centralwidget = QWidget(frm_operations)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
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
        self.tree_data.header().setMinimumSectionSize(20)

        self.verticalLayout.addWidget(self.tree_data)

        frm_operations.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(frm_operations)
        self.statusbar.setObjectName(u"statusbar")
        frm_operations.setStatusBar(self.statusbar)

        self.retranslateUi(frm_operations)

        QMetaObject.connectSlotsByName(frm_operations)
    # setupUi

    def retranslateUi(self, frm_operations):
        frm_operations.setWindowTitle(QCoreApplication.translate("frm_operations", u"MainWindow", None))
    # retranslateUi


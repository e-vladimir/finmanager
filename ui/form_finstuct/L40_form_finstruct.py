# ФОРМА ФИНСТРУКТУРЫ: КАРКАС ДАННЫХ

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_finstructMgCjOD.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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

class Ui_form_finstruct(object):
    def setupUi(self, form_finstruct):
        if not form_finstruct.objectName():
            form_finstruct.setObjectName(u"form_finstruct")
        form_finstruct.resize(1000, 600)
        self.centralwidget = QWidget(form_finstruct)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.tree_data = QTreeView(self.centralwidget)
        self.tree_data.setObjectName(u"tree_data")
        self.tree_data.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tree_data.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tree_data.setAutoExpandDelay(1)
        self.tree_data.setRootIsDecorated(False)
        self.tree_data.setItemsExpandable(False)
        self.tree_data.setSortingEnabled(False)
        self.tree_data.setHeaderHidden(False)
        self.tree_data.setExpandsOnDoubleClick(False)
        self.tree_data.header().setVisible(True)
        self.tree_data.header().setMinimumSectionSize(10)
        self.tree_data.header().setStretchLastSection(False)

        self.horizontalLayout.addWidget(self.tree_data)

        self.horizontalLayout.setStretch(0, 1)
        form_finstruct.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(form_finstruct)
        self.statusbar.setObjectName(u"statusbar")
        form_finstruct.setStatusBar(self.statusbar)

        self.retranslateUi(form_finstruct)

        QMetaObject.connectSlotsByName(form_finstruct)
    # setupUi

    def retranslateUi(self, form_finstruct):
        form_finstruct.setWindowTitle(QCoreApplication.translate("form_finstruct", u"MainWindow", None))
    # retranslateUi

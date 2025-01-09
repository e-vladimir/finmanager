# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_analyticsTeRXZr.ui'
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
    QListView, QMainWindow, QSizePolicy, QStatusBar,
    QTreeView, QWidget)

class Ui_form_analytics(object):
    def setupUi(self, form_analytics):
        if not form_analytics.objectName():
            form_analytics.setObjectName(u"form_analytics")
        form_analytics.resize(800, 640)
        self.centralwidget = QWidget(form_analytics)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.list_items = QListView(self.centralwidget)
        self.list_items.setObjectName(u"list_items")
        self.list_items.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.list_items.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.list_items.setAlternatingRowColors(True)
        self.list_items.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.horizontalLayout.addWidget(self.list_items)

        self.tree_data = QTreeView(self.centralwidget)
        self.tree_data.setObjectName(u"tree_data")
        self.tree_data.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tree_data.setAlternatingRowColors(False)
        self.tree_data.setRootIsDecorated(False)
        self.tree_data.header().setVisible(False)
        self.tree_data.header().setMinimumSectionSize(20)
        self.tree_data.header().setStretchLastSection(False)

        self.horizontalLayout.addWidget(self.tree_data)

        self.horizontalLayout.setStretch(1, 1)
        form_analytics.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(form_analytics)
        self.statusbar.setObjectName(u"statusbar")
        form_analytics.setStatusBar(self.statusbar)

        self.retranslateUi(form_analytics)

        QMetaObject.connectSlotsByName(form_analytics)
    # setupUi

    def retranslateUi(self, form_analytics):
        form_analytics.setWindowTitle(QCoreApplication.translate("form_analytics", u"MainWindow", None))
    # retranslateUi


# ФОРМА ЗАПИСЬ ФИНДЕЙСТВИЙ: КАРКАС ДАННЫХ

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_record_finactionsWkzBiE.ui'
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
    QMainWindow, QSizePolicy, QSplitter, QStatusBar,
    QTableView, QTreeView, QWidget)

class Ui_frm_record_finactions(object):
    def setupUi(self, frm_record_finactions):
        if not frm_record_finactions.objectName():
            frm_record_finactions.setObjectName(u"frm_record_finactions")
        frm_record_finactions.resize(638, 515)
        self.centralwidget = QWidget(frm_record_finactions)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.tbl_data = QTableView(self.splitter)
        self.tbl_data.setObjectName(u"tbl_data")
        self.tbl_data.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tbl_data.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tbl_data.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tbl_data.setShowGrid(False)
        self.tbl_data.setWordWrap(False)
        self.splitter.addWidget(self.tbl_data)
        self.tbl_data.horizontalHeader().setVisible(False)
        self.tbl_data.horizontalHeader().setMinimumSectionSize(22)
        self.tbl_data.horizontalHeader().setStretchLastSection(True)
        self.tbl_data.verticalHeader().setVisible(False)
        self.tbl_data.verticalHeader().setMinimumSectionSize(22)
        self.tbl_data.verticalHeader().setDefaultSectionSize(22)
        self.tre_values = QTreeView(self.splitter)
        self.tre_values.setObjectName(u"tre_values")
        self.tre_values.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tre_values.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tre_values.setRootIsDecorated(False)
        self.tre_values.setItemsExpandable(False)
        self.tre_values.setHeaderHidden(True)
        self.tre_values.setExpandsOnDoubleClick(False)
        self.splitter.addWidget(self.tre_values)
        self.tre_values.header().setMinimumSectionSize(22)

        self.horizontalLayout.addWidget(self.splitter)

        frm_record_finactions.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(frm_record_finactions)
        self.statusbar.setObjectName(u"statusbar")
        frm_record_finactions.setStatusBar(self.statusbar)

        self.retranslateUi(frm_record_finactions)

        QMetaObject.connectSlotsByName(frm_record_finactions)
    # setupUi

    def retranslateUi(self, frm_record_finactions):
        frm_record_finactions.setWindowTitle(QCoreApplication.translate("frm_record_finactions", u"MainWindow", None))
    # retranslateUi

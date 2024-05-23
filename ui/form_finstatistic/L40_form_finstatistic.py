# ФОРМА ФИНСТАТИСТИКА: КАРКАС ДАННЫХ

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_finstatisticOsptof.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHeaderView, QMainWindow,
    QSizePolicy, QStatusBar, QTreeView, QVBoxLayout,
    QWidget)

class Ui_frm_finstatistic(object):
    def setupUi(self, frm_finstatistic):
        if not frm_finstatistic.objectName():
            frm_finstatistic.setObjectName(u"frm_finstatistic")
        frm_finstatistic.resize(716, 735)
        self.centralwidget = QWidget(frm_finstatistic)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.tree_finstatistic = QTreeView(self.centralwidget)
        self.tree_finstatistic.setObjectName(u"tree_finstatistic")
        self.tree_finstatistic.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tree_finstatistic.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tree_finstatistic.setAlternatingRowColors(True)
        self.tree_finstatistic.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tree_finstatistic.setRootIsDecorated(False)
        self.tree_finstatistic.setItemsExpandable(False)
        self.tree_finstatistic.setExpandsOnDoubleClick(False)
        self.tree_finstatistic.header().setMinimumSectionSize(20)
        self.tree_finstatistic.header().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.tree_finstatistic)

        frm_finstatistic.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(frm_finstatistic)
        self.statusbar.setObjectName(u"statusbar")
        frm_finstatistic.setStatusBar(self.statusbar)

        self.retranslateUi(frm_finstatistic)

        QMetaObject.connectSlotsByName(frm_finstatistic)
    # setupUi

    def retranslateUi(self, frm_finstatistic):
        frm_finstatistic.setWindowTitle(QCoreApplication.translate("frm_finstatistic", u"MainWindow", None))
    # retranslateUi

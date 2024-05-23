# ФОРМА ФИНСОСТАВА: КАРКАС ДАННЫХ

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_findescriptionnDLMlB.ui'
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
    QListWidget, QListWidgetItem, QMainWindow, QSizePolicy,
    QStatusBar, QTreeView, QWidget)

class Ui_frm_findescription(object):
    def setupUi(self, frm_findescription):
        if not frm_findescription.objectName():
            frm_findescription.setObjectName(u"frm_findescription")
        frm_findescription.resize(800, 600)
        self.centralwidget = QWidget(frm_findescription)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.lst_categories = QListWidget(self.centralwidget)
        self.lst_categories.setObjectName(u"lst_categories")
        self.lst_categories.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.lst_categories.setAlternatingRowColors(True)
        self.lst_categories.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)

        self.horizontalLayout.addWidget(self.lst_categories)

        self.tre_findescription = QTreeView(self.centralwidget)
        self.tre_findescription.setObjectName(u"tre_findescription")
        self.tre_findescription.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tre_findescription.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tre_findescription.setAutoExpandDelay(1)
        self.tre_findescription.setRootIsDecorated(False)
        self.tre_findescription.setItemsExpandable(False)
        self.tre_findescription.setSortingEnabled(False)
        self.tre_findescription.setExpandsOnDoubleClick(False)
        self.tre_findescription.header().setVisible(False)

        self.horizontalLayout.addWidget(self.tre_findescription)

        self.horizontalLayout.setStretch(1, 1)
        frm_findescription.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(frm_findescription)
        self.statusbar.setObjectName(u"statusbar")
        frm_findescription.setStatusBar(self.statusbar)

        self.retranslateUi(frm_findescription)

        QMetaObject.connectSlotsByName(frm_findescription)
    # setupUi

    def retranslateUi(self, frm_findescription):
        frm_findescription.setWindowTitle(QCoreApplication.translate("frm_findescription", u"MainWindow", None))
    # retranslateUi

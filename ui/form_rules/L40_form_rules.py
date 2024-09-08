# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_rulesMRtxMJ.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QListWidget, QListWidgetItem, QMainWindow, QSizePolicy,
    QStatusBar, QTableView, QWidget)

class Ui_form_rules(object):
    def setupUi(self, form_rules):
        if not form_rules.objectName():
            form_rules.setObjectName(u"form_rules")
        form_rules.resize(1024, 640)
        self.centralwidget = QWidget(form_rules)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.list_types = QListWidget(self.centralwidget)
        self.list_types.setObjectName(u"list_types")
        self.list_types.setMaximumSize(QSize(300, 16777215))
        self.list_types.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.list_types.setAlternatingRowColors(True)
        self.list_types.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.horizontalLayout.addWidget(self.list_types)

        self.table_data = QTableView(self.centralwidget)
        self.table_data.setObjectName(u"table_data")
        self.table_data.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.table_data.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_data.setAlternatingRowColors(True)
        self.table_data.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table_data.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_data.setShowGrid(False)
        self.table_data.horizontalHeader().setMinimumSectionSize(20)
        self.table_data.horizontalHeader().setStretchLastSection(True)
        self.table_data.verticalHeader().setVisible(False)
        self.table_data.verticalHeader().setMinimumSectionSize(20)
        self.table_data.verticalHeader().setDefaultSectionSize(20)

        self.horizontalLayout.addWidget(self.table_data)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        form_rules.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(form_rules)
        self.statusbar.setObjectName(u"statusbar")
        form_rules.setStatusBar(self.statusbar)

        self.retranslateUi(form_rules)

        QMetaObject.connectSlotsByName(form_rules)
    # setupUi

    def retranslateUi(self, form_rules):
        form_rules.setWindowTitle(QCoreApplication.translate("form_rules", u"MainWindow", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_rulesCsAJBy.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QHeaderView,
    QMainWindow, QSizePolicy, QStatusBar, QTableView,
    QVBoxLayout, QWidget)

class Ui_frm_rules(object):
    def setupUi(self, frm_rules):
        if not frm_rules.objectName():
            frm_rules.setObjectName(u"frm_rules")
        frm_rules.resize(800, 600)
        self.centralwidget = QWidget(frm_rules)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.cbbox_types = QComboBox(self.centralwidget)
        self.cbbox_types.setObjectName(u"cbbox_types")

        self.verticalLayout.addWidget(self.cbbox_types)

        self.table_data = QTableView(self.centralwidget)
        self.table_data.setObjectName(u"table_data")
        self.table_data.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.table_data.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_data.setAlternatingRowColors(True)
        self.table_data.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table_data.horizontalHeader().setStretchLastSection(True)
        self.table_data.verticalHeader().setVisible(False)
        self.table_data.verticalHeader().setMinimumSectionSize(20)
        self.table_data.verticalHeader().setDefaultSectionSize(20)

        self.verticalLayout.addWidget(self.table_data)

        frm_rules.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(frm_rules)
        self.statusbar.setObjectName(u"statusbar")
        frm_rules.setStatusBar(self.statusbar)

        self.retranslateUi(frm_rules)

        QMetaObject.connectSlotsByName(frm_rules)
    # setupUi

    def retranslateUi(self, frm_rules):
        frm_rules.setWindowTitle(QCoreApplication.translate("frm_rules", u"MainWindow", None))
    # retranslateUi


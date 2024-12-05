# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_control_descriptionDnbdhy.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
    QSizePolicy, QStatusBar, QTabWidget, QTableView,
    QVBoxLayout, QWidget)

class Ui_frm_control_description(object):
    def setupUi(self, frm_control_description):
        if not frm_control_description.objectName():
            frm_control_description.setObjectName(u"frm_control_description")
        frm_control_description.resize(800, 600)
        self.centralwidget = QWidget(frm_control_description)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.tabs_main = QTabWidget(self.centralwidget)
        self.tabs_main.setObjectName(u"tabs_main")
        self.tab_rules = QWidget()
        self.tab_rules.setObjectName(u"tab_rules")
        self.verticalLayout_2 = QVBoxLayout(self.tab_rules)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.table_rules = QTableView(self.tab_rules)
        self.table_rules.setObjectName(u"table_rules")
        self.table_rules.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.table_rules.setAlternatingRowColors(True)
        self.table_rules.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table_rules.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_rules.horizontalHeader().setMinimumSectionSize(100)
        self.table_rules.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.table_rules)

        self.tabs_main.addTab(self.tab_rules, "")
        self.tab_control = QWidget()
        self.tab_control.setObjectName(u"tab_control")
        self.verticalLayout_3 = QVBoxLayout(self.tab_control)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.table_control = QTableView(self.tab_control)
        self.table_control.setObjectName(u"table_control")
        self.table_control.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.table_control.setAlternatingRowColors(False)
        self.table_control.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table_control.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_control.horizontalHeader().setVisible(False)
        self.table_control.horizontalHeader().setMinimumSectionSize(100)
        self.table_control.horizontalHeader().setStretchLastSection(True)
        self.table_control.verticalHeader().setVisible(False)

        self.verticalLayout_3.addWidget(self.table_control)

        self.tabs_main.addTab(self.tab_control, "")

        self.verticalLayout.addWidget(self.tabs_main)

        frm_control_description.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(frm_control_description)
        self.statusbar.setObjectName(u"statusbar")
        frm_control_description.setStatusBar(self.statusbar)

        self.retranslateUi(frm_control_description)

        self.tabs_main.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(frm_control_description)
    # setupUi

    def retranslateUi(self, frm_control_description):
        frm_control_description.setWindowTitle(QCoreApplication.translate("frm_control_description", u"MainWindow", None))
        self.tabs_main.setTabText(self.tabs_main.indexOf(self.tab_rules), QCoreApplication.translate("frm_control_description", u"\u041f\u0440\u0430\u0432\u0438\u043b\u0430 \u0430\u0432\u0442\u043e\u0437\u0430\u043c\u0435\u043d\u044b \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u044f", None))
        self.tabs_main.setTabText(self.tabs_main.indexOf(self.tab_control), QCoreApplication.translate("frm_control_description", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435\u043c", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_processing_operationsKfpQVp.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHeaderView, QMainWindow,
    QSizePolicy, QStatusBar, QTabWidget, QTableView,
    QTreeView, QVBoxLayout, QWidget)

class Ui_frm_processing_operations(object):
    def setupUi(self, frm_processing_operations):
        if not frm_processing_operations.objectName():
            frm_processing_operations.setObjectName(u"frm_processing_operations")
        frm_processing_operations.resize(640, 800)
        self.centralwidget = QWidget(frm_processing_operations)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabs_main = QTabWidget(self.centralwidget)
        self.tabs_main.setObjectName(u"tabs_main")
        self.tab_rules = QWidget()
        self.tab_rules.setObjectName(u"tab_rules")
        self.verticalLayout = QVBoxLayout(self.tab_rules)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.table_rules = QTableView(self.tab_rules)
        self.table_rules.setObjectName(u"table_rules")
        self.table_rules.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.table_rules.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_rules.setAlternatingRowColors(True)
        self.table_rules.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table_rules.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_rules.horizontalHeader().setMinimumSectionSize(30)
        self.table_rules.horizontalHeader().setStretchLastSection(True)
        self.table_rules.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.table_rules)

        self.tabs_main.addTab(self.tab_rules, "")
        self.tab_tools = QWidget()
        self.tab_tools.setObjectName(u"tab_tools")
        self.verticalLayout_3 = QVBoxLayout(self.tab_tools)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tree_tools = QTreeView(self.tab_tools)
        self.tree_tools.setObjectName(u"tree_tools")
        self.tree_tools.setStyleSheet(u"QTreeView::branch { \n"
"	border: none; \n"
"}")
        self.tree_tools.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tree_tools.setAlternatingRowColors(True)
        self.tree_tools.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectColumns)
        self.tree_tools.setRootIsDecorated(False)
        self.tree_tools.setItemsExpandable(True)
        self.tree_tools.setExpandsOnDoubleClick(False)
        self.tree_tools.header().setVisible(False)

        self.verticalLayout_3.addWidget(self.tree_tools)

        self.tabs_main.addTab(self.tab_tools, "")

        self.verticalLayout_2.addWidget(self.tabs_main)

        frm_processing_operations.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(frm_processing_operations)
        self.statusbar.setObjectName(u"statusbar")
        frm_processing_operations.setStatusBar(self.statusbar)

        self.retranslateUi(frm_processing_operations)

        self.tabs_main.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(frm_processing_operations)
    # setupUi

    def retranslateUi(self, frm_processing_operations):
        frm_processing_operations.setWindowTitle(QCoreApplication.translate("frm_processing_operations", u"MainWindow", None))
        self.tabs_main.setTabText(self.tabs_main.indexOf(self.tab_rules), QCoreApplication.translate("frm_processing_operations", u"\u041f\u0440\u0430\u0432\u0438\u043b\u0430 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438", None))
        self.tabs_main.setTabText(self.tabs_main.indexOf(self.tab_tools), QCoreApplication.translate("frm_processing_operations", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439", None))
    # retranslateUi


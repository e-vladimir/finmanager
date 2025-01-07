# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_analyticsvjLDsk.ui'
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
    QListWidget, QListWidgetItem, QMainWindow, QSizePolicy,
    QStatusBar, QTabWidget, QTableView, QVBoxLayout,
    QWidget)

class Ui_form_analytics(object):
    def setupUi(self, form_analytics):
        if not form_analytics.objectName():
            form_analytics.setObjectName(u"form_analytics")
        form_analytics.resize(903, 600)
        self.centralwidget = QWidget(form_analytics)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.tabs_main = QTabWidget(self.centralwidget)
        self.tabs_main.setObjectName(u"tabs_main")
        self.tab_analytics_items = QWidget()
        self.tab_analytics_items.setObjectName(u"tab_analytics_items")
        self.horizontalLayout_2 = QHBoxLayout(self.tab_analytics_items)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.table_items = QTableView(self.tab_analytics_items)
        self.table_items.setObjectName(u"table_items")
        self.table_items.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.table_items.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_items.setAlternatingRowColors(True)
        self.table_items.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table_items.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_items.horizontalHeader().setVisible(False)
        self.table_items.verticalHeader().setVisible(False)

        self.horizontalLayout_2.addWidget(self.table_items)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.list_item_include = QListWidget(self.tab_analytics_items)
        self.list_item_include.setObjectName(u"list_item_include")
        self.list_item_include.setMinimumSize(QSize(250, 0))
        self.list_item_include.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.list_item_include.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.list_item_include.setAlternatingRowColors(True)
        self.list_item_include.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.list_item_include.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.verticalLayout_2.addWidget(self.list_item_include)

        self.list_item_exclude = QListWidget(self.tab_analytics_items)
        self.list_item_exclude.setObjectName(u"list_item_exclude")
        self.list_item_exclude.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.list_item_exclude.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.list_item_exclude.setAlternatingRowColors(True)
        self.list_item_exclude.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)

        self.verticalLayout_2.addWidget(self.list_item_exclude)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalLayout_2.setStretch(0, 1)
        self.tabs_main.addTab(self.tab_analytics_items, "")

        self.verticalLayout.addWidget(self.tabs_main)

        form_analytics.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(form_analytics)
        self.statusbar.setObjectName(u"statusbar")
        form_analytics.setStatusBar(self.statusbar)

        self.retranslateUi(form_analytics)

        self.tabs_main.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(form_analytics)
    # setupUi

    def retranslateUi(self, form_analytics):
        form_analytics.setWindowTitle(QCoreApplication.translate("form_analytics", u"MainWindow", None))
        self.tabs_main.setTabText(self.tabs_main.indexOf(self.tab_analytics_items), QCoreApplication.translate("form_analytics", u"\u042d\u043b\u0435\u043c\u0435\u043d\u0442\u044b \u0430\u043d\u0430\u043b\u0438\u0442\u0438\u043a\u0438", None))
    # retranslateUi


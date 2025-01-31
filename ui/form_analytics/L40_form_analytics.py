# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_analyticsaxtjOU.ui'
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
    QTabWidget, QTreeView, QVBoxLayout, QWidget)

class Ui_frm_analytics(object):
    def setupUi(self, frm_analytics):
        if not frm_analytics.objectName():
            frm_analytics.setObjectName(u"frm_analytics")
        frm_analytics.resize(800, 600)
        self.centralwidget = QWidget(frm_analytics)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabs_main = QTabWidget(self.centralwidget)
        self.tabs_main.setObjectName(u"tabs_main")
        self.tab_items = QWidget()
        self.tab_items.setObjectName(u"tab_items")
        self.horizontalLayout = QHBoxLayout(self.tab_items)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.list_items = QListView(self.tab_items)
        self.list_items.setObjectName(u"list_items")
        self.list_items.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.list_items.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.list_items.setAlternatingRowColors(True)
        self.list_items.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.horizontalLayout.addWidget(self.list_items)

        self.tree_data_item = QTreeView(self.tab_items)
        self.tree_data_item.setObjectName(u"tree_data_item")
        self.tree_data_item.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tree_data_item.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tree_data_item.setRootIsDecorated(False)
        self.tree_data_item.setItemsExpandable(False)
        self.tree_data_item.setHeaderHidden(False)
        self.tree_data_item.setExpandsOnDoubleClick(False)
        self.tree_data_item.header().setVisible(True)

        self.horizontalLayout.addWidget(self.tree_data_item)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.tabs_main.addTab(self.tab_items, "")
        self.tab_dm = QWidget()
        self.tab_dm.setObjectName(u"tab_dm")
        self.horizontalLayout_2 = QHBoxLayout(self.tab_dm)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tree_data_dm = QTreeView(self.tab_dm)
        self.tree_data_dm.setObjectName(u"tree_data_dm")
        self.tree_data_dm.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tree_data_dm.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tree_data_dm.setAlternatingRowColors(True)
        self.tree_data_dm.setRootIsDecorated(False)
        self.tree_data_dm.setItemsExpandable(False)
        self.tree_data_dm.setExpandsOnDoubleClick(False)
        self.tree_data_dm.header().setStretchLastSection(False)

        self.horizontalLayout_2.addWidget(self.tree_data_dm)

        self.tabs_main.addTab(self.tab_dm, "")
        self.tab_dy = QWidget()
        self.tab_dy.setObjectName(u"tab_dy")
        self.horizontalLayout_3 = QHBoxLayout(self.tab_dy)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tree_data_dy = QTreeView(self.tab_dy)
        self.tree_data_dy.setObjectName(u"tree_data_dy")
        self.tree_data_dy.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tree_data_dy.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tree_data_dy.setRootIsDecorated(False)
        self.tree_data_dy.setItemsExpandable(False)
        self.tree_data_dy.setExpandsOnDoubleClick(False)
        self.tree_data_dy.header().setStretchLastSection(False)

        self.horizontalLayout_3.addWidget(self.tree_data_dy)

        self.tabs_main.addTab(self.tab_dy, "")
        self.tab_analytics = QWidget()
        self.tab_analytics.setObjectName(u"tab_analytics")
        self.tabs_main.addTab(self.tab_analytics, "")

        self.verticalLayout.addWidget(self.tabs_main)

        frm_analytics.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(frm_analytics)
        self.statusbar.setObjectName(u"statusbar")
        frm_analytics.setStatusBar(self.statusbar)

        self.retranslateUi(frm_analytics)

        self.tabs_main.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(frm_analytics)
    # setupUi

    def retranslateUi(self, frm_analytics):
        frm_analytics.setWindowTitle(QCoreApplication.translate("frm_analytics", u"MainWindow", None))
        self.tabs_main.setTabText(self.tabs_main.indexOf(self.tab_items), QCoreApplication.translate("frm_analytics", u"\u042d\u043b\u0435\u043c\u0435\u043d\u0442\u044b \u0430\u043d\u0430\u043b\u0438\u0442\u0438\u043a\u0438", None))
        self.tabs_main.setTabText(self.tabs_main.indexOf(self.tab_dm), QCoreApplication.translate("frm_analytics", u"\u0421\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u0430 \u043c\u0435\u0441\u044f\u0446\u0430", None))
        self.tabs_main.setTabText(self.tabs_main.indexOf(self.tab_dy), QCoreApplication.translate("frm_analytics", u"\u0414\u0438\u043d\u0430\u043c\u0438\u043a\u0430", None))
        self.tabs_main.setTabText(self.tabs_main.indexOf(self.tab_analytics), QCoreApplication.translate("frm_analytics", u"\u0410\u043d\u0430\u043b\u0438\u0442\u0438\u043a\u0430", None))
    # retranslateUi


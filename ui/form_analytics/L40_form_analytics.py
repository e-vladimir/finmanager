# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_analyticsOgTqbi.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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

class Ui_FormAnalytics(object):
    def setupUi(self, FormAnalytics):
        if not FormAnalytics.objectName():
            FormAnalytics.setObjectName(u"FormAnalytics")
        FormAnalytics.resize(800, 600)
        self.centralwidget = QWidget(FormAnalytics)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.TabsMain = QTabWidget(self.centralwidget)
        self.TabsMain.setObjectName(u"TabsMain")
        self.TabItems = QWidget()
        self.TabItems.setObjectName(u"TabItems")
        self.horizontalLayout = QHBoxLayout(self.TabItems)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ListDataItems = QListView(self.TabItems)
        self.ListDataItems.setObjectName(u"ListDataItems")
        self.ListDataItems.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.ListDataItems.setStyleSheet(u"QListView {\n"
"background: white;\n"
"border: 1px solid lightgray;\n"
"border-radius: 5px;\n"
"padding: 3px;\n"
"}")
        self.ListDataItems.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.ListDataItems.setAlternatingRowColors(True)
        self.ListDataItems.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.ListDataItems.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.horizontalLayout.addWidget(self.ListDataItems)

        self.TreeDataItem = QTreeView(self.TabItems)
        self.TreeDataItem.setObjectName(u"TreeDataItem")
        self.TreeDataItem.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.TreeDataItem.setStyleSheet(u"QTreeView {\n"
"background: white;\n"
"border: 1px solid lightgray;\n"
"border-radius: 5px;\n"
"padding: 3px;\n"
"}")
        self.TreeDataItem.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.TreeDataItem.setAlternatingRowColors(True)
        self.TreeDataItem.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.TreeDataItem.setRootIsDecorated(False)
        self.TreeDataItem.setItemsExpandable(False)
        self.TreeDataItem.setExpandsOnDoubleClick(False)
        self.TreeDataItem.header().setVisible(False)

        self.horizontalLayout.addWidget(self.TreeDataItem)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 3)
        self.TabsMain.addTab(self.TabItems, "")
        self.TabAnalytics = QWidget()
        self.TabAnalytics.setObjectName(u"TabAnalytics")
        self.verticalLayout_2 = QVBoxLayout(self.TabAnalytics)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.TreeViewAnalytics = QTreeView(self.TabAnalytics)
        self.TreeViewAnalytics.setObjectName(u"TreeViewAnalytics")
        self.TreeViewAnalytics.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.TreeViewAnalytics.setStyleSheet(u"QTreeView {\n"
"background: white;\n"
"border: 1px solid lightgray;\n"
"border-radius: 5px;\n"
"padding: 3px;\n"
"}")
        self.TreeViewAnalytics.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.TreeViewAnalytics.setAlternatingRowColors(True)
        self.TreeViewAnalytics.setRootIsDecorated(False)
        self.TreeViewAnalytics.setItemsExpandable(False)
        self.TreeViewAnalytics.setExpandsOnDoubleClick(False)
        self.TreeViewAnalytics.header().setVisible(False)

        self.verticalLayout_2.addWidget(self.TreeViewAnalytics)

        self.TabsMain.addTab(self.TabAnalytics, "")

        self.verticalLayout.addWidget(self.TabsMain)

        FormAnalytics.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(FormAnalytics)
        self.statusbar.setObjectName(u"statusbar")
        FormAnalytics.setStatusBar(self.statusbar)

        self.retranslateUi(FormAnalytics)

        self.TabsMain.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(FormAnalytics)
    # setupUi

    def retranslateUi(self, FormAnalytics):
        FormAnalytics.setWindowTitle(QCoreApplication.translate("FormAnalytics", u"MainWindow", None))
        self.TabsMain.setTabText(self.TabsMain.indexOf(self.TabItems), QCoreApplication.translate("FormAnalytics", u"\u042d\u043b\u0435\u043c\u0435\u043d\u0442\u044b \u0430\u043d\u0430\u043b\u0438\u0442\u0438\u043a\u0438", None))
        self.TabsMain.setTabText(self.TabsMain.indexOf(self.TabAnalytics), QCoreApplication.translate("FormAnalytics", u"\u0410\u043d\u0430\u043b\u0438\u0442\u0438\u043a\u0430", None))
    # retranslateUi


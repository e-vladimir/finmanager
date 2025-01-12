# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_analyticsUAAdnR.ui'
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
    QListView, QMainWindow, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QTreeView, QVBoxLayout,
    QWidget)

from L20_form_analytics import C20_DiaDynamic

class Ui_form_analytics(object):
    def setupUi(self, form_analytics):
        if not form_analytics.objectName():
            form_analytics.setObjectName(u"form_analytics")
        form_analytics.resize(1200, 800)
        self.centralwidget = QWidget(form_analytics)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.list_items = QListView(self.centralwidget)
        self.list_items.setObjectName(u"list_items")
        self.list_items.setMinimumSize(QSize(300, 0))
        self.list_items.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.list_items.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.list_items.setAlternatingRowColors(True)
        self.list_items.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.horizontalLayout.addWidget(self.list_items)

        self.tabs_data = QTabWidget(self.centralwidget)
        self.tabs_data.setObjectName(u"tabs_data")
        self.tab_data_options = QWidget()
        self.tab_data_options.setObjectName(u"tab_data_options")
        self.verticalLayout = QVBoxLayout(self.tab_data_options)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tree_data_options = QTreeView(self.tab_data_options)
        self.tree_data_options.setObjectName(u"tree_data_options")
        self.tree_data_options.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tree_data_options.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tree_data_options.setAlternatingRowColors(False)
        self.tree_data_options.setRootIsDecorated(False)
        self.tree_data_options.setItemsExpandable(False)
        self.tree_data_options.setHeaderHidden(True)
        self.tree_data_options.setExpandsOnDoubleClick(False)
        self.tree_data_options.header().setMinimumSectionSize(30)
        self.tree_data_options.header().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.tree_data_options)

        self.tabs_data.addTab(self.tab_data_options, "")
        self.tab_data_dynamic = QWidget()
        self.tab_data_dynamic.setObjectName(u"tab_data_dynamic")
        self.verticalLayout_2 = QVBoxLayout(self.tab_data_dynamic)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.dia_data_dynamic = C20_DiaDynamic(self.tab_data_dynamic)
        self.dia_data_dynamic.setObjectName(u"dia_data_dynamic")
        self.dia_data_dynamic.setMinimumSize(QSize(0, 300))

        self.verticalLayout_2.addWidget(self.dia_data_dynamic)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.tabs_data.addTab(self.tab_data_dynamic, "")
        self.tab_data_volume = QWidget()
        self.tab_data_volume.setObjectName(u"tab_data_volume")
        self.verticalLayout_3 = QVBoxLayout(self.tab_data_volume)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tree_data_volume = QTreeView(self.tab_data_volume)
        self.tree_data_volume.setObjectName(u"tree_data_volume")
        self.tree_data_volume.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tree_data_volume.setAlternatingRowColors(False)
        self.tree_data_volume.setRootIsDecorated(False)
        self.tree_data_volume.setItemsExpandable(False)
        self.tree_data_volume.setExpandsOnDoubleClick(False)
        self.tree_data_volume.header().setVisible(False)
        self.tree_data_volume.header().setStretchLastSection(False)

        self.verticalLayout_3.addWidget(self.tree_data_volume)

        self.tabs_data.addTab(self.tab_data_volume, "")

        self.horizontalLayout.addWidget(self.tabs_data)

        self.horizontalLayout.setStretch(1, 1)
        form_analytics.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(form_analytics)
        self.statusbar.setObjectName(u"statusbar")
        form_analytics.setStatusBar(self.statusbar)

        self.retranslateUi(form_analytics)

        self.tabs_data.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(form_analytics)
    # setupUi

    def retranslateUi(self, form_analytics):
        form_analytics.setWindowTitle(QCoreApplication.translate("form_analytics", u"MainWindow", None))
        self.tabs_data.setTabText(self.tabs_data.indexOf(self.tab_data_options), QCoreApplication.translate("form_analytics", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.tabs_data.setTabText(self.tabs_data.indexOf(self.tab_data_dynamic), QCoreApplication.translate("form_analytics", u"\u0414\u0438\u043d\u0430\u043c\u0438\u043a\u0430", None))
        self.tabs_data.setTabText(self.tabs_data.indexOf(self.tab_data_volume), QCoreApplication.translate("form_analytics", u"\u041e\u0431\u044a\u0451\u043c\u043d\u0430\u044f \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c", None))
    # retranslateUi


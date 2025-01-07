# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_analyticsdZHdzq.ui'
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
    QSizePolicy, QStatusBar, QTabWidget, QTreeView,
    QVBoxLayout, QWidget)

class Ui_form_analytics(object):
    def setupUi(self, form_analytics):
        if not form_analytics.objectName():
            form_analytics.setObjectName(u"form_analytics")
        form_analytics.resize(1200, 800)
        self.centralwidget = QWidget(form_analytics)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.tabs_main = QTabWidget(self.centralwidget)
        self.tabs_main.setObjectName(u"tabs_main")
        self.tab_analytics_dm = QWidget()
        self.tab_analytics_dm.setObjectName(u"tab_analytics_dm")
        self.verticalLayout_4 = QVBoxLayout(self.tab_analytics_dm)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tree_data_dm = QTreeView(self.tab_analytics_dm)
        self.tree_data_dm.setObjectName(u"tree_data_dm")
        self.tree_data_dm.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tree_data_dm.setAlternatingRowColors(True)
        self.tree_data_dm.setRootIsDecorated(False)
        self.tree_data_dm.setItemsExpandable(True)
        self.tree_data_dm.header().setVisible(True)
        self.tree_data_dm.header().setMinimumSectionSize(30)
        self.tree_data_dm.header().setStretchLastSection(False)

        self.verticalLayout_4.addWidget(self.tree_data_dm)

        self.tabs_main.addTab(self.tab_analytics_dm, "")

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
        self.tabs_main.setTabText(self.tabs_main.indexOf(self.tab_analytics_dm), QCoreApplication.translate("form_analytics", u"\u0410\u043d\u0430\u043b\u0438\u0442\u0438\u043a\u0430 (\u0437\u0430 \u043c\u0435\u0441\u044f\u0446)", None))
    # retranslateUi


# ФОРМА ФИНАНАЛИЗ: КАРКАС ДАННЫХ

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_finanalyticsWyTCFX.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHeaderView, QMainWindow,
    QSizePolicy, QStatusBar, QTabWidget, QTableView,
    QVBoxLayout, QWidget)

class Ui_form_finanalytics(object):
    def setupUi(self, form_finanalytics):
        if not form_finanalytics.objectName():
            form_finanalytics.setObjectName(u"form_finanalytics")
        form_finanalytics.resize(1000, 640)
        self.centralwidget = QWidget(form_finanalytics)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.tabs_main = QTabWidget(self.centralwidget)
        self.tabs_main.setObjectName(u"tabs_main")
        self.tab_findescription_dynamic = QWidget()
        self.tab_findescription_dynamic.setObjectName(u"tab_findescription_dynamic")
        self.verticalLayout_2 = QVBoxLayout(self.tab_findescription_dynamic)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.table_findescription_dynamic = QTableView(self.tab_findescription_dynamic)
        self.table_findescription_dynamic.setObjectName(u"table_findescription_dynamic")
        self.table_findescription_dynamic.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.table_findescription_dynamic.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_findescription_dynamic.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.table_findescription_dynamic.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_findescription_dynamic.horizontalHeader().setVisible(False)
        self.table_findescription_dynamic.horizontalHeader().setMinimumSectionSize(20)
        self.table_findescription_dynamic.verticalHeader().setVisible(False)
        self.table_findescription_dynamic.verticalHeader().setMinimumSectionSize(20)
        self.table_findescription_dynamic.verticalHeader().setDefaultSectionSize(20)

        self.verticalLayout_2.addWidget(self.table_findescription_dynamic)

        self.tabs_main.addTab(self.tab_findescription_dynamic, "")

        self.verticalLayout.addWidget(self.tabs_main)

        form_finanalytics.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(form_finanalytics)
        self.statusbar.setObjectName(u"statusbar")
        form_finanalytics.setStatusBar(self.statusbar)

        self.retranslateUi(form_finanalytics)

        self.tabs_main.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(form_finanalytics)
    # setupUi

    def retranslateUi(self, form_finanalytics):
        form_finanalytics.setWindowTitle(QCoreApplication.translate("form_finanalytics", u"MainWindow", None))
        self.tabs_main.setTabText(self.tabs_main.indexOf(self.tab_findescription_dynamic), QCoreApplication.translate("form_finanalytics", u"\u0414\u0438\u043d\u0430\u043c\u0438\u043a\u0430 \u0444\u0438\u043d\u0441\u043e\u0441\u0442\u0430\u0432\u0430", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_finanaliticssNtVgk.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHeaderView, QMainWindow,
    QSizePolicy, QStatusBar, QTabWidget, QTableView,
    QTreeView, QVBoxLayout, QWidget)

class Ui_form_finanalitics(object):
    def setupUi(self, form_finanalitics):
        if not form_finanalitics.objectName():
            form_finanalitics.setObjectName(u"form_finanalitics")
        form_finanalitics.resize(1024, 768)
        self.centralwidget = QWidget(form_finanalitics)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.tabs_main = QTabWidget(self.centralwidget)
        self.tabs_main.setObjectName(u"tabs_main")
        self.tab_options = QWidget()
        self.tab_options.setObjectName(u"tab_options")
        self.verticalLayout_2 = QVBoxLayout(self.tab_options)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tree_options = QTreeView(self.tab_options)
        self.tree_options.setObjectName(u"tree_options")
        self.tree_options.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tree_options.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tree_options.setAlternatingRowColors(True)
        self.tree_options.setRootIsDecorated(False)
        self.tree_options.setHeaderHidden(True)

        self.verticalLayout_2.addWidget(self.tree_options)

        self.tabs_main.addTab(self.tab_options, "")
        self.tab_result_dm = QWidget()
        self.tab_result_dm.setObjectName(u"tab_result_dm")
        self.verticalLayout_3 = QVBoxLayout(self.tab_result_dm)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.table_data_dm = QTableView(self.tab_result_dm)
        self.table_data_dm.setObjectName(u"table_data_dm")
        self.table_data_dm.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.table_data_dm.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_data_dm.setAlternatingRowColors(True)
        self.table_data_dm.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table_data_dm.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_data_dm.setShowGrid(False)
        self.table_data_dm.horizontalHeader().setVisible(False)
        self.table_data_dm.horizontalHeader().setMinimumSectionSize(20)
        self.table_data_dm.verticalHeader().setVisible(False)
        self.table_data_dm.verticalHeader().setMinimumSectionSize(20)
        self.table_data_dm.verticalHeader().setDefaultSectionSize(20)

        self.verticalLayout_3.addWidget(self.table_data_dm)

        self.tabs_main.addTab(self.tab_result_dm, "")
        self.tab_result_12_dm = QWidget()
        self.tab_result_12_dm.setObjectName(u"tab_result_12_dm")
        self.tabs_main.addTab(self.tab_result_12_dm, "")
        self.tab_result_summary = QWidget()
        self.tab_result_summary.setObjectName(u"tab_result_summary")
        self.tabs_main.addTab(self.tab_result_summary, "")

        self.verticalLayout.addWidget(self.tabs_main)

        form_finanalitics.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(form_finanalitics)
        self.statusbar.setObjectName(u"statusbar")
        form_finanalitics.setStatusBar(self.statusbar)

        self.retranslateUi(form_finanalitics)

        self.tabs_main.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(form_finanalitics)
    # setupUi

    def retranslateUi(self, form_finanalitics):
        form_finanalitics.setWindowTitle(QCoreApplication.translate("form_finanalitics", u"MainWindow", None))
        self.tabs_main.setTabText(self.tabs_main.indexOf(self.tab_options), QCoreApplication.translate("form_finanalitics", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0430\u043d\u0430\u043b\u0438\u0437\u0430", None))
        self.tabs_main.setTabText(self.tabs_main.indexOf(self.tab_result_dm), QCoreApplication.translate("form_finanalitics", u"\u0410\u043d\u0430\u043b\u0438\u0437 \u043c\u0435\u0441\u044f\u0446\u0430", None))
        self.tabs_main.setTabText(self.tabs_main.indexOf(self.tab_result_12_dm), QCoreApplication.translate("form_finanalitics", u"\u0410\u043d\u0430\u043b\u0438\u0437 12 \u043c\u0435\u0441\u044f\u0446\u0435\u0432", None))
        self.tabs_main.setTabText(self.tabs_main.indexOf(self.tab_result_summary), QCoreApplication.translate("form_finanalitics", u"\u041e\u0431\u0449\u0438\u0439 \u0430\u043d\u0430\u043b\u0438\u0437", None))
    # retranslateUi


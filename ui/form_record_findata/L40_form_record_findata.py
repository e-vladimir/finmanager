# ФОРМА ЗАПИСИ ФИНДАННЫХ: КАРКАС ДАННЫХ

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_record_findataddIbgx.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QMainWindow, QSizePolicy, QSplitter, QStatusBar,
    QTableView, QWidget)

class Ui_form_record_findata(object):
    def setupUi(self, form_record_findata):
        if not form_record_findata.objectName():
            form_record_findata.setObjectName(u"form_record_findata")
        form_record_findata.resize(638, 515)
        self.centralwidget = QWidget(form_record_findata)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.table_data = QTableView(self.splitter)
        self.table_data.setObjectName(u"table_data")
        self.table_data.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_data.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_data.setShowGrid(False)
        self.table_data.setWordWrap(False)
        self.splitter.addWidget(self.table_data)
        self.table_data.horizontalHeader().setVisible(False)
        self.table_data.horizontalHeader().setMinimumSectionSize(22)
        self.table_data.horizontalHeader().setStretchLastSection(True)
        self.table_data.verticalHeader().setVisible(False)
        self.table_data.verticalHeader().setMinimumSectionSize(22)
        self.table_data.verticalHeader().setDefaultSectionSize(22)
        self.table_values = QTableView(self.splitter)
        self.table_values.setObjectName(u"table_values")
        self.table_values.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_values.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_values.setShowGrid(False)
        self.table_values.setWordWrap(False)
        self.splitter.addWidget(self.table_values)
        self.table_values.horizontalHeader().setVisible(False)
        self.table_values.horizontalHeader().setMinimumSectionSize(22)
        self.table_values.horizontalHeader().setStretchLastSection(True)
        self.table_values.verticalHeader().setVisible(False)
        self.table_values.verticalHeader().setMinimumSectionSize(22)
        self.table_values.verticalHeader().setDefaultSectionSize(22)

        self.horizontalLayout.addWidget(self.splitter)

        form_record_findata.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(form_record_findata)
        self.statusbar.setObjectName(u"statusbar")
        form_record_findata.setStatusBar(self.statusbar)

        self.retranslateUi(form_record_findata)

        QMetaObject.connectSlotsByName(form_record_findata)
    # setupUi

    def retranslateUi(self, form_record_findata):
        form_record_findata.setWindowTitle(QCoreApplication.translate("form_record_findata", u"MainWindow", None))
    # retranslateUi

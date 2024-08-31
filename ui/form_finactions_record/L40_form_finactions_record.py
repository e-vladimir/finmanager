# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_finactions_recordjibhVr.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QMainWindow, QSizePolicy, QStatusBar, QTableView,
    QWidget)

class Ui_frm_finactions_record(object):
    def setupUi(self, frm_finactions_record):
        if not frm_finactions_record.objectName():
            frm_finactions_record.setObjectName(u"frm_finactions_record")
        frm_finactions_record.resize(640, 640)
        self.centralwidget = QWidget(frm_finactions_record)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.table_data = QTableView(self.centralwidget)
        self.table_data.setObjectName(u"table_data")
        self.table_data.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.table_data.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_data.setAlternatingRowColors(False)
        self.table_data.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_data.setShowGrid(False)
        self.table_data.horizontalHeader().setVisible(False)
        self.table_data.horizontalHeader().setMinimumSectionSize(20)
        self.table_data.horizontalHeader().setDefaultSectionSize(20)
        self.table_data.horizontalHeader().setStretchLastSection(True)
        self.table_data.verticalHeader().setVisible(False)
        self.table_data.verticalHeader().setMinimumSectionSize(20)
        self.table_data.verticalHeader().setDefaultSectionSize(20)
        self.table_data.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout.addWidget(self.table_data)

        self.horizontalLayout.setStretch(0, 1)
        frm_finactions_record.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(frm_finactions_record)
        self.statusbar.setObjectName(u"statusbar")
        frm_finactions_record.setStatusBar(self.statusbar)

        self.retranslateUi(frm_finactions_record)

        QMetaObject.connectSlotsByName(frm_finactions_record)
    # setupUi

    def retranslateUi(self, frm_finactions_record):
        frm_finactions_record.setWindowTitle(QCoreApplication.translate("frm_finactions_record", u"MainWindow", None))
    # retranslateUi


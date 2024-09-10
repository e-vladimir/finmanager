# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_backupfcMhIQ.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QListView, QMainWindow,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_form_backup(object):
    def setupUi(self, form_backup):
        if not form_backup.objectName():
            form_backup.setObjectName(u"form_backup")
        form_backup.resize(480, 640)
        self.centralwidget = QWidget(form_backup)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.list_data = QListView(self.centralwidget)
        self.list_data.setObjectName(u"list_data")
        self.list_data.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.list_data.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.list_data.setAlternatingRowColors(True)
        self.list_data.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.verticalLayout.addWidget(self.list_data)

        form_backup.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(form_backup)
        self.statusbar.setObjectName(u"statusbar")
        form_backup.setStatusBar(self.statusbar)

        self.retranslateUi(form_backup)

        QMetaObject.connectSlotsByName(form_backup)
    # setupUi

    def retranslateUi(self, form_backup):
        form_backup.setWindowTitle(QCoreApplication.translate("form_backup", u"MainWindow", None))
    # retranslateUi


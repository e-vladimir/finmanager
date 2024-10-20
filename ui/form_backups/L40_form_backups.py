# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_backupsdCKWzG.ui'
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

class Ui_form_backups(object):
    def setupUi(self, form_backups):
        if not form_backups.objectName():
            form_backups.setObjectName(u"form_backups")
        form_backups.resize(480, 640)
        self.centralwidget = QWidget(form_backups)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.list_data = QListView(self.centralwidget)
        self.list_data.setObjectName(u"list_data")
        self.list_data.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.list_data.setStyleSheet(u"QListView {\n"
"border: 1px solid lightgray;\n"
"border-radius: 5px;\n"
"padding: 1px;\n"
"}")
        self.list_data.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.list_data.setAlternatingRowColors(True)
        self.list_data.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.verticalLayout.addWidget(self.list_data)

        form_backups.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(form_backups)
        self.statusbar.setObjectName(u"statusbar")
        form_backups.setStatusBar(self.statusbar)

        self.retranslateUi(form_backups)

        QMetaObject.connectSlotsByName(form_backups)
    # setupUi

    def retranslateUi(self, form_backups):
        form_backups.setWindowTitle(QCoreApplication.translate("form_backups", u"MainWindow", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_backupsOqjYZz.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QListView,
    QMainWindow, QSizePolicy, QStatusBar, QWidget)

class Ui_FormBackups(object):
    def setupUi(self, FormBackups):
        if not FormBackups.objectName():
            FormBackups.setObjectName(u"FormBackups")
        FormBackups.resize(480, 640)
        self.centralwidget = QWidget(FormBackups)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ListData = QListView(self.centralwidget)
        self.ListData.setObjectName(u"ListData")
        self.ListData.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.ListData.setStyleSheet(u"QListView {\n"
"background: white;\n"
"border: 1px solid lightgray;\n"
"border-radius: 5px;\n"
"padding: 3px;\n"
"}")
        self.ListData.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.ListData.setAlternatingRowColors(True)
        self.ListData.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.horizontalLayout.addWidget(self.ListData)

        FormBackups.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(FormBackups)
        self.statusbar.setObjectName(u"statusbar")
        FormBackups.setStatusBar(self.statusbar)

        self.retranslateUi(FormBackups)

        QMetaObject.connectSlotsByName(FormBackups)
    # setupUi

    def retranslateUi(self, FormBackups):
        FormBackups.setWindowTitle(QCoreApplication.translate("FormBackups", u"MainWindow", None))
    # retranslateUi


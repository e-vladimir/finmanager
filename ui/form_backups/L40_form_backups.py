# ФОРМА РЕЗЕРВНЫЕ КОПИИ: КАРКАС ДАННЫХ

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_backupsSpAMfu.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QListView, QMainWindow,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_frm_backups(object):
    def setupUi(self, frm_backups):
        if not frm_backups.objectName():
            frm_backups.setObjectName(u"frm_backups")
        frm_backups.resize(640, 480)
        self.centralwidget = QWidget(frm_backups)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.lst_backups = QListView(self.centralwidget)
        self.lst_backups.setObjectName(u"lst_backups")
        self.lst_backups.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.lst_backups.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.lst_backups.setAlternatingRowColors(True)
        self.lst_backups.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.verticalLayout.addWidget(self.lst_backups)

        frm_backups.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(frm_backups)
        self.statusbar.setObjectName(u"statusbar")
        frm_backups.setStatusBar(self.statusbar)

        self.retranslateUi(frm_backups)

        QMetaObject.connectSlotsByName(frm_backups)
    # setupUi

    def retranslateUi(self, frm_backups):
        frm_backups.setWindowTitle(QCoreApplication.translate("frm_backups", u"MainWindow", None))
    # retranslateUi

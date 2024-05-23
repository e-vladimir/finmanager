# ФОРМА ФИНДАННЫЕ: КАРКАС ДАННЫХ

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_findatammPdqm.ui'
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
    QSizePolicy, QStatusBar, QTreeView, QVBoxLayout,
    QWidget)

class Ui_form_findata(object):
    def setupUi(self, form_findata):
        if not form_findata.objectName():
            form_findata.setObjectName(u"form_findata")
        form_findata.resize(993, 610)
        self.centralwidget = QWidget(form_findata)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.tree_data = QTreeView(self.centralwidget)
        self.tree_data.setObjectName(u"tree_data")
        self.tree_data.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tree_data.setToolTipDuration(-1)
        self.tree_data.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tree_data.setRootIsDecorated(False)
        self.tree_data.setItemsExpandable(False)
        self.tree_data.setExpandsOnDoubleClick(False)
        self.tree_data.header().setMinimumSectionSize(10)

        self.verticalLayout.addWidget(self.tree_data)

        form_findata.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(form_findata)
        self.statusbar.setObjectName(u"statusbar")
        form_findata.setStatusBar(self.statusbar)

        self.retranslateUi(form_findata)

        QMetaObject.connectSlotsByName(form_findata)
    # setupUi

    def retranslateUi(self, form_findata):
        form_findata.setWindowTitle(QCoreApplication.translate("form_findata", u"MainWindow", None))
    # retranslateUi

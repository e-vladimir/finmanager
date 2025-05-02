# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_analyticsdaVzFj.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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

class Ui_FormAnalytics(object):
    def setupUi(self, FormAnalytics):
        if not FormAnalytics.objectName():
            FormAnalytics.setObjectName(u"FormAnalytics")
        FormAnalytics.resize(800, 600)
        self.centralwidget = QWidget(FormAnalytics)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 6, -1, -1)
        self.TreeData = QTreeView(self.centralwidget)
        self.TreeData.setObjectName(u"TreeData")
        self.TreeData.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.TreeData.setStyleSheet(u"QTreeView {\n"
"background: white;\n"
"border: 1px solid lightgray;\n"
"border-radius: 5px;\n"
"padding: 3px;\n"
"}")
        self.TreeData.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.TreeData.setAlternatingRowColors(False)
        self.TreeData.setRootIsDecorated(False)
        self.TreeData.setItemsExpandable(False)
        self.TreeData.setExpandsOnDoubleClick(False)
        self.TreeData.header().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.TreeData)

        FormAnalytics.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(FormAnalytics)
        self.statusbar.setObjectName(u"statusbar")
        FormAnalytics.setStatusBar(self.statusbar)

        self.retranslateUi(FormAnalytics)

        QMetaObject.connectSlotsByName(FormAnalytics)
    # setupUi

    def retranslateUi(self, FormAnalytics):
        FormAnalytics.setWindowTitle(QCoreApplication.translate("FormAnalytics", u"MainWindow", None))
    # retranslateUi


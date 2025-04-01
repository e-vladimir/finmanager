# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_exportEZtIJz.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHeaderView, QMainWindow,
    QSizePolicy, QStatusBar, QTreeView, QVBoxLayout,
    QWidget)

class Ui_FormExport(object):
    def setupUi(self, FormExport):
        if not FormExport.objectName():
            FormExport.setObjectName(u"FormExport")
        FormExport.resize(800, 600)
        self.centralwidget = QWidget(FormExport)
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
"}\n"
"\n"
"QTreeView::branch {\n"
"background: white;\n"
"border: none;\n"
"}")
        self.TreeData.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.TreeData.setAlternatingRowColors(True)
        self.TreeData.setRootIsDecorated(False)
        self.TreeData.setItemsExpandable(False)
        self.TreeData.setExpandsOnDoubleClick(False)
        self.TreeData.header().setVisible(False)

        self.verticalLayout.addWidget(self.TreeData)

        FormExport.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(FormExport)
        self.statusbar.setObjectName(u"statusbar")
        FormExport.setStatusBar(self.statusbar)

        self.retranslateUi(FormExport)

        QMetaObject.connectSlotsByName(FormExport)
    # setupUi

    def retranslateUi(self, FormExport):
        FormExport.setWindowTitle(QCoreApplication.translate("FormExport", u"MainWindow", None))
    # retranslateUi


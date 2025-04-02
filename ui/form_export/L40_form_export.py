# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_exportDIbvZX.ui'
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
    QSizePolicy, QStatusBar, QTabWidget, QTreeView,
    QVBoxLayout, QWidget)

class Ui_FormExport(object):
    def setupUi(self, FormExport):
        if not FormExport.objectName():
            FormExport.setObjectName(u"FormExport")
        FormExport.resize(800, 600)
        self.centralwidget = QWidget(FormExport)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.TabsMain = QTabWidget(self.centralwidget)
        self.TabsMain.setObjectName(u"TabsMain")
        self.TabOperations = QWidget()
        self.TabOperations.setObjectName(u"TabOperations")
        self.verticalLayout_2 = QVBoxLayout(self.TabOperations)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.TreeDataOperations = QTreeView(self.TabOperations)
        self.TreeDataOperations.setObjectName(u"TreeDataOperations")
        self.TreeDataOperations.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.TreeDataOperations.setStyleSheet(u"QTreeView {\n"
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
        self.TreeDataOperations.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.TreeDataOperations.setAlternatingRowColors(True)
        self.TreeDataOperations.setRootIsDecorated(False)
        self.TreeDataOperations.setItemsExpandable(False)
        self.TreeDataOperations.setExpandsOnDoubleClick(False)
        self.TreeDataOperations.header().setVisible(False)

        self.verticalLayout_2.addWidget(self.TreeDataOperations)

        self.TabsMain.addTab(self.TabOperations, "")

        self.verticalLayout.addWidget(self.TabsMain)

        FormExport.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(FormExport)
        self.statusbar.setObjectName(u"statusbar")
        FormExport.setStatusBar(self.statusbar)

        self.retranslateUi(FormExport)

        self.TabsMain.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(FormExport)
    # setupUi

    def retranslateUi(self, FormExport):
        FormExport.setWindowTitle(QCoreApplication.translate("FormExport", u"MainWindow", None))
        self.TabsMain.setTabText(self.TabsMain.indexOf(self.TabOperations), QCoreApplication.translate("FormExport", u"\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u0438", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_processinglbnwPI.ui'
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
    QSizePolicy, QStatusBar, QTabWidget, QTableView,
    QTreeView, QVBoxLayout, QWidget)

class Ui_FormProcessing(object):
    def setupUi(self, FormProcessing):
        if not FormProcessing.objectName():
            FormProcessing.setObjectName(u"FormProcessing")
        FormProcessing.resize(800, 600)
        self.centralwidget = QWidget(FormProcessing)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 6, -1, -1)
        self.TabsMain = QTabWidget(self.centralwidget)
        self.TabsMain.setObjectName(u"TabsMain")
        self.TabManual = QWidget()
        self.TabManual.setObjectName(u"TabManual")
        self.verticalLayout_2 = QVBoxLayout(self.TabManual)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.TreeDataManual = QTreeView(self.TabManual)
        self.TreeDataManual.setObjectName(u"TreeDataManual")
        self.TreeDataManual.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.TreeDataManual.setStyleSheet(u"QTreeView {\n"
"background: white;\n"
"border: 1px solid lightgray;\n"
"border-radius: 5px;\n"
"padding: 3px;\n"
"}")
        self.TreeDataManual.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.TreeDataManual.setAlternatingRowColors(True)
        self.TreeDataManual.setRootIsDecorated(False)

        self.verticalLayout_2.addWidget(self.TreeDataManual)

        self.TabsMain.addTab(self.TabManual, "")
        self.TabAuto = QWidget()
        self.TabAuto.setObjectName(u"TabAuto")
        self.verticalLayout_3 = QVBoxLayout(self.TabAuto)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.TableDataAuto = QTableView(self.TabAuto)
        self.TableDataAuto.setObjectName(u"TableDataAuto")
        self.TableDataAuto.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.TableDataAuto.setStyleSheet(u"QTableView {\n"
"background: white;\n"
"border: 1px solid lightgray;\n"
"border-radius: 5px;\n"
"padding: 3px;\n"
"}")
        self.TableDataAuto.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.TableDataAuto.setAlternatingRowColors(True)
        self.TableDataAuto.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.TableDataAuto.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.TableDataAuto.verticalHeader().setVisible(False)
        self.TableDataAuto.verticalHeader().setMinimumSectionSize(22)
        self.TableDataAuto.verticalHeader().setDefaultSectionSize(22)

        self.verticalLayout_3.addWidget(self.TableDataAuto)

        self.TabsMain.addTab(self.TabAuto, "")

        self.verticalLayout.addWidget(self.TabsMain)

        FormProcessing.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(FormProcessing)
        self.statusbar.setObjectName(u"statusbar")
        FormProcessing.setStatusBar(self.statusbar)

        self.retranslateUi(FormProcessing)

        self.TabsMain.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(FormProcessing)
    # setupUi

    def retranslateUi(self, FormProcessing):
        FormProcessing.setWindowTitle(QCoreApplication.translate("FormProcessing", u"MainWindow", None))
        self.TabsMain.setTabText(self.TabsMain.indexOf(self.TabManual), QCoreApplication.translate("FormProcessing", u"\u0420\u0443\u0447\u043d\u0430\u044f \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430", None))
        self.TabsMain.setTabText(self.TabsMain.indexOf(self.TabAuto), QCoreApplication.translate("FormProcessing", u"\u0410\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430", None))
    # retranslateUi


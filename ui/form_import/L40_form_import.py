# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_importBVfNne.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QSizePolicy, QStatusBar,
    QTabWidget, QTableView, QVBoxLayout, QWidget)

class Ui_form_import(object):
    def setupUi(self, form_import):
        if not form_import.objectName():
            form_import.setObjectName(u"form_import")
        form_import.resize(800, 600)
        self.centralwidget = QWidget(form_import)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.TabsMain = QTabWidget(self.centralwidget)
        self.TabsMain.setObjectName(u"TabsMain")
        self.TabOperations = QWidget()
        self.TabOperations.setObjectName(u"TabOperations")
        self.verticalLayout = QVBoxLayout(self.TabOperations)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.TableDataOperations = QTableView(self.TabOperations)
        self.TableDataOperations.setObjectName(u"TableDataOperations")
        self.TableDataOperations.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.TableDataOperations.setStyleSheet(u"QTableView {\n"
"background: white;\n"
"border: 1px solid lightgray;\n"
"border-radius: 5px;\n"
"padding: 3px;\n"
"}")
        self.TableDataOperations.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.TableDataOperations.setAlternatingRowColors(True)
        self.TableDataOperations.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.TableDataOperations.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.TableDataOperations.horizontalHeader().setMinimumSectionSize(20)
        self.TableDataOperations.horizontalHeader().setStretchLastSection(True)
        self.TableDataOperations.verticalHeader().setVisible(False)
        self.TableDataOperations.verticalHeader().setMinimumSectionSize(22)
        self.TableDataOperations.verticalHeader().setDefaultSectionSize(22)

        self.verticalLayout.addWidget(self.TableDataOperations)

        self.LabelOperationsFilepath = QLabel(self.TabOperations)
        self.LabelOperationsFilepath.setObjectName(u"LabelOperationsFilepath")

        self.verticalLayout.addWidget(self.LabelOperationsFilepath)

        self.TabsMain.addTab(self.TabOperations, "")

        self.horizontalLayout.addWidget(self.TabsMain)

        form_import.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(form_import)
        self.statusbar.setObjectName(u"statusbar")
        form_import.setStatusBar(self.statusbar)

        self.retranslateUi(form_import)

        self.TabsMain.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(form_import)
    # setupUi

    def retranslateUi(self, form_import):
        form_import.setWindowTitle(QCoreApplication.translate("form_import", u"MainWindow", None))
        self.LabelOperationsFilepath.setText(QCoreApplication.translate("form_import", u"TextLabel", None))
        self.TabsMain.setTabText(self.TabsMain.indexOf(self.TabOperations), QCoreApplication.translate("form_import", u"\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u0438", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_processing_operationseakusL.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QHeaderView,
    QLabel, QMainWindow, QSizePolicy, QStatusBar,
    QTableView, QVBoxLayout, QWidget)

class Ui_frm_processing_operations(object):
    def setupUi(self, frm_processing_operations):
        if not frm_processing_operations.objectName():
            frm_processing_operations.setObjectName(u"frm_processing_operations")
        frm_processing_operations.resize(800, 600)
        self.centralwidget = QWidget(frm_processing_operations)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.cbbox_subject = QComboBox(self.centralwidget)
        self.cbbox_subject.setObjectName(u"cbbox_subject")

        self.verticalLayout.addWidget(self.cbbox_subject)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.table_rules = QTableView(self.centralwidget)
        self.table_rules.setObjectName(u"table_rules")
        self.table_rules.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.table_rules.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_rules.setAlternatingRowColors(True)
        self.table_rules.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table_rules.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_rules.horizontalHeader().setMinimumSectionSize(30)
        self.table_rules.horizontalHeader().setStretchLastSection(True)
        self.table_rules.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.table_rules)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.table_tools = QTableView(self.centralwidget)
        self.table_tools.setObjectName(u"table_tools")
        self.table_tools.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.table_tools.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_tools.setAlternatingRowColors(True)
        self.table_tools.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table_tools.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_tools.horizontalHeader().setVisible(False)
        self.table_tools.horizontalHeader().setMinimumSectionSize(30)
        self.table_tools.horizontalHeader().setStretchLastSection(True)
        self.table_tools.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.table_tools)

        self.verticalLayout.setStretch(3, 1)
        frm_processing_operations.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(frm_processing_operations)
        self.statusbar.setObjectName(u"statusbar")
        frm_processing_operations.setStatusBar(self.statusbar)

        self.retranslateUi(frm_processing_operations)

        QMetaObject.connectSlotsByName(frm_processing_operations)
    # setupUi

    def retranslateUi(self, frm_processing_operations):
        frm_processing_operations.setWindowTitle(QCoreApplication.translate("frm_processing_operations", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("frm_processing_operations", u"\u0421\u0443\u0431\u044a\u0435\u043a\u0442 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438", None))
        self.label_2.setText(QCoreApplication.translate("frm_processing_operations", u"\u041f\u0440\u0430\u0432\u0438\u043b\u0430 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438", None))
        self.label_3.setText(QCoreApplication.translate("frm_processing_operations", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u044b \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438", None))
    # retranslateUi


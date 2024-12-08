# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_processing_rulexuaFvg.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPlainTextEdit, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_frm_processing_rule(object):
    def setupUi(self, frm_processing_rule):
        if not frm_processing_rule.objectName():
            frm_processing_rule.setObjectName(u"frm_processing_rule")
        frm_processing_rule.resize(800, 480)
        self.centralwidget = QWidget(frm_processing_rule)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_input = QLabel(self.centralwidget)
        self.label_input.setObjectName(u"label_input")
        self.label_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_input)

        self.edit_input_single = QLineEdit(self.centralwidget)
        self.edit_input_single.setObjectName(u"edit_input_single")

        self.verticalLayout.addWidget(self.edit_input_single)

        self.edit_input_multiple = QPlainTextEdit(self.centralwidget)
        self.edit_input_multiple.setObjectName(u"edit_input_multiple")
        self.edit_input_multiple.setTabChangesFocus(True)
        self.edit_input_multiple.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)

        self.verticalLayout.addWidget(self.edit_input_multiple)

        self.list_input_items = QListWidget(self.centralwidget)
        self.list_input_items.setObjectName(u"list_input_items")
        self.list_input_items.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.list_input_items.setAlternatingRowColors(True)
        self.list_input_items.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.verticalLayout.addWidget(self.list_input_items)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_output = QLabel(self.centralwidget)
        self.label_output.setObjectName(u"label_output")
        self.label_output.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_output)

        self.edit_output_single = QLineEdit(self.centralwidget)
        self.edit_output_single.setObjectName(u"edit_output_single")

        self.verticalLayout_2.addWidget(self.edit_output_single)

        self.edit_output_multiple = QPlainTextEdit(self.centralwidget)
        self.edit_output_multiple.setObjectName(u"edit_output_multiple")
        self.edit_output_multiple.setTabChangesFocus(True)
        self.edit_output_multiple.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)

        self.verticalLayout_2.addWidget(self.edit_output_multiple)

        self.list_output_items = QListWidget(self.centralwidget)
        self.list_output_items.setObjectName(u"list_output_items")
        self.list_output_items.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.list_output_items.setAlternatingRowColors(True)
        self.list_output_items.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.verticalLayout_2.addWidget(self.list_output_items)

        self.verticalSpacer_2 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        frm_processing_rule.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(frm_processing_rule)
        self.statusbar.setObjectName(u"statusbar")
        frm_processing_rule.setStatusBar(self.statusbar)

        self.retranslateUi(frm_processing_rule)

        QMetaObject.connectSlotsByName(frm_processing_rule)
    # setupUi

    def retranslateUi(self, frm_processing_rule):
        frm_processing_rule.setWindowTitle(QCoreApplication.translate("frm_processing_rule", u"MainWindow", None))
        self.label_input.setText(QCoreApplication.translate("frm_processing_rule", u"TextLabel", None))
        self.label_output.setText(QCoreApplication.translate("frm_processing_rule", u"TextLabel", None))
    # retranslateUi


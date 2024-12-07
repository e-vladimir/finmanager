# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_control_descriptionebwIjA.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QTableView, QVBoxLayout,
    QWidget)

class Ui_frm_control_description(object):
    def setupUi(self, frm_control_description):
        if not frm_control_description.objectName():
            frm_control_description.setObjectName(u"frm_control_description")
        frm_control_description.resize(800, 600)
        self.centralwidget = QWidget(frm_control_description)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.tabs_main = QTabWidget(self.centralwidget)
        self.tabs_main.setObjectName(u"tabs_main")
        self.tab_rules = QWidget()
        self.tab_rules.setObjectName(u"tab_rules")
        self.verticalLayout_2 = QVBoxLayout(self.tab_rules)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.table_rules = QTableView(self.tab_rules)
        self.table_rules.setObjectName(u"table_rules")
        self.table_rules.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.table_rules.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_rules.setAlternatingRowColors(True)
        self.table_rules.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table_rules.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_rules.horizontalHeader().setMinimumSectionSize(100)
        self.table_rules.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.table_rules)

        self.tabs_main.addTab(self.tab_rules, "")
        self.tab_control_replace = QWidget()
        self.tab_control_replace.setObjectName(u"tab_control_replace")
        self.horizontalLayout = QHBoxLayout(self.tab_control_replace)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.tab_control_replace)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)

        self.list_control_replace_available = QListWidget(self.tab_control_replace)
        self.list_control_replace_available.setObjectName(u"list_control_replace_available")
        self.list_control_replace_available.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.list_control_replace_available.setAlternatingRowColors(True)

        self.verticalLayout_4.addWidget(self.list_control_replace_available)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.tab_control_replace)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.edit_control_replace_input = QPlainTextEdit(self.tab_control_replace)
        self.edit_control_replace_input.setObjectName(u"edit_control_replace_input")
        self.edit_control_replace_input.setTabChangesFocus(True)
        self.edit_control_replace_input.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)

        self.verticalLayout_3.addWidget(self.edit_control_replace_input)

        self.label_2 = QLabel(self.tab_control_replace)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.edit_control_replace_output = QLineEdit(self.tab_control_replace)
        self.edit_control_replace_output.setObjectName(u"edit_control_replace_output")

        self.verticalLayout_3.addWidget(self.edit_control_replace_output)

        self.btn_control_replace = QPushButton(self.tab_control_replace)
        self.btn_control_replace.setObjectName(u"btn_control_replace")

        self.verticalLayout_3.addWidget(self.btn_control_replace)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.tabs_main.addTab(self.tab_control_replace, "")

        self.verticalLayout.addWidget(self.tabs_main)

        frm_control_description.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(frm_control_description)
        self.statusbar.setObjectName(u"statusbar")
        frm_control_description.setStatusBar(self.statusbar)

        self.retranslateUi(frm_control_description)

        self.tabs_main.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(frm_control_description)
    # setupUi

    def retranslateUi(self, frm_control_description):
        frm_control_description.setWindowTitle(QCoreApplication.translate("frm_control_description", u"MainWindow", None))
        self.tabs_main.setTabText(self.tabs_main.indexOf(self.tab_rules), QCoreApplication.translate("frm_control_description", u"\u041f\u0440\u0430\u0432\u0438\u043b\u0430 \u0430\u0432\u0442\u043e\u0437\u0430\u043c\u0435\u043d\u044b \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u044f", None))
        self.label_3.setText(QCoreApplication.translate("frm_control_description", u"\u0414\u043e\u0441\u0442\u0443\u043f\u043d\u044b\u0435 \u0444\u0440\u0430\u0433\u043c\u0435\u043d\u0442\u044b", None))
        self.label.setText(QCoreApplication.translate("frm_control_description", u"\u0424\u0440\u0430\u0433\u043c\u0435\u043d\u0442\u044b \u043f\u043e\u0438\u0441\u043a\u0430", None))
        self.label_2.setText(QCoreApplication.translate("frm_control_description", u"\u0424\u0440\u0430\u0433\u043c\u0435\u043d\u0442 \u0437\u0430\u043c\u0435\u043d\u044b", None))
        self.btn_control_replace.setText(QCoreApplication.translate("frm_control_description", u"\u041d\u0430\u0439\u0442\u0438 \u0438 \u0437\u0430\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.tabs_main.setTabText(self.tabs_main.indexOf(self.tab_control_replace), QCoreApplication.translate("frm_control_description", u"\u041f\u043e\u0438\u0441\u043a \u0438 \u0437\u0430\u043c\u0435\u043d\u0430", None))
    # retranslateUi


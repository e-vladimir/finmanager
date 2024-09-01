# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_finactions_recordkFXUlH.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QSizePolicy, QSpacerItem,
    QSpinBox, QStatusBar, QTreeView, QVBoxLayout,
    QWidget)

class Ui_form_finactions_record(object):
    def setupUi(self, form_finactions_record):
        if not form_finactions_record.objectName():
            form_finactions_record.setObjectName(u"form_finactions_record")
        form_finactions_record.resize(640, 640)
        self.centralwidget = QWidget(form_finactions_record)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 6, 6, -1)
        self.group_main = QGroupBox(self.centralwidget)
        self.group_main.setObjectName(u"group_main")
        self.verticalLayout_3 = QVBoxLayout(self.group_main)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.edit_dd = QSpinBox(self.group_main)
        self.edit_dd.setObjectName(u"edit_dd")
        self.edit_dd.setMinimumSize(QSize(75, 0))
        self.edit_dd.setMaximumSize(QSize(75, 16777215))
        self.edit_dd.setMinimum(1)
        self.edit_dd.setMaximum(31)

        self.horizontalLayout.addWidget(self.edit_dd)

        self.cbbox_dm = QComboBox(self.group_main)
        self.cbbox_dm.setObjectName(u"cbbox_dm")
        self.cbbox_dm.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout.addWidget(self.cbbox_dm)

        self.cbbox_dy = QComboBox(self.group_main)
        self.cbbox_dy.setObjectName(u"cbbox_dy")
        self.cbbox_dy.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout.addWidget(self.cbbox_dy)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.edit_amount = QSpinBox(self.group_main)
        self.edit_amount.setObjectName(u"edit_amount")
        self.edit_amount.setMinimumSize(QSize(100, 0))
        self.edit_amount.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.edit_amount.setProperty("showGroupSeparator", True)
        self.edit_amount.setMinimum(-99999999)
        self.edit_amount.setMaximum(99999999)
        self.edit_amount.setValue(0)
        self.edit_amount.setDisplayIntegerBase(10)

        self.horizontalLayout.addWidget(self.edit_amount)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addWidget(self.group_main)

        self.group_src = QGroupBox(self.centralwidget)
        self.group_src.setObjectName(u"group_src")
        self.group_src.setFlat(False)
        self.horizontalLayout_2 = QHBoxLayout(self.group_src)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.label_src_note = QLabel(self.group_src)
        self.label_src_note.setObjectName(u"label_src_note")
        self.label_src_note.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.label_src_note)

        self.label_src_amount = QLabel(self.group_src)
        self.label_src_amount.setObjectName(u"label_src_amount")

        self.horizontalLayout_2.addWidget(self.label_src_amount)

        self.horizontalLayout_2.setStretch(0, 1)

        self.verticalLayout_4.addWidget(self.group_src)

        self.group_record = QGroupBox(self.centralwidget)
        self.group_record.setObjectName(u"group_record")
        self.group_record.setFlat(False)
        self.verticalLayout = QVBoxLayout(self.group_record)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.edit_note = QLineEdit(self.group_record)
        self.edit_note.setObjectName(u"edit_note")

        self.verticalLayout.addWidget(self.edit_note)

        self.tree_finstruct = QTreeView(self.group_record)
        self.tree_finstruct.setObjectName(u"tree_finstruct")
        self.tree_finstruct.setAutoFillBackground(False)
        self.tree_finstruct.setStyleSheet(u" QTreeView {\n"
"	border: 1px solid #CCCCCC;\n"
"	border-radius: 3px;\n"
"	padding: 1px;\n"
"}")
        self.tree_finstruct.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tree_finstruct.setRootIsDecorated(False)
        self.tree_finstruct.setItemsExpandable(False)
        self.tree_finstruct.setExpandsOnDoubleClick(False)
        self.tree_finstruct.header().setVisible(False)

        self.verticalLayout.addWidget(self.tree_finstruct)

        self.edit_labels = QPlainTextEdit(self.group_record)
        self.edit_labels.setObjectName(u"edit_labels")
        self.edit_labels.setStyleSheet(u"QPlainTextEdit {\n"
"	border: 1px solid #CCCCCC;\n"
"	border-radius: 3px;\n"
"	padding: 1px;\n"
"}")
        self.edit_labels.setOverwriteMode(False)
        self.edit_labels.setBackgroundVisible(False)

        self.verticalLayout.addWidget(self.edit_labels)

        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 1)

        self.verticalLayout_4.addWidget(self.group_record)

        form_finactions_record.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(form_finactions_record)
        self.statusbar.setObjectName(u"statusbar")
        form_finactions_record.setStatusBar(self.statusbar)

        self.retranslateUi(form_finactions_record)

        QMetaObject.connectSlotsByName(form_finactions_record)
    # setupUi

    def retranslateUi(self, form_finactions_record):
        form_finactions_record.setWindowTitle(QCoreApplication.translate("form_finactions_record", u"MainWindow", None))
        self.group_main.setTitle(QCoreApplication.translate("form_finactions_record", u"\u041e\u0421\u041d\u041e\u0412\u041d\u042b\u0415 \u0414\u0410\u041d\u041d\u042b\u0415", None))
        self.cbbox_dm.setPlaceholderText(QCoreApplication.translate("form_finactions_record", u"\u043c\u0435\u0441", None))
        self.cbbox_dy.setCurrentText("")
        self.cbbox_dy.setPlaceholderText(QCoreApplication.translate("form_finactions_record", u"2024", None))
        self.edit_amount.setSpecialValueText("")
        self.group_src.setTitle(QCoreApplication.translate("form_finactions_record", u"\u0418\u0421\u0425\u041e\u0414\u041d\u042b\u0415 \u0414\u0410\u041d\u041d\u042b\u0415", None))
        self.label_src_note.setText(QCoreApplication.translate("form_finactions_record", u"\u041d\u0435\u0442 \u043f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u044f", None))
        self.label_src_amount.setText(QCoreApplication.translate("form_finactions_record", u"+3927", None))
        self.group_record.setTitle(QCoreApplication.translate("form_finactions_record", u"\u0420\u0410\u0411\u041e\u0427\u0418\u0415 \u0414\u0410\u041d\u041d\u042b\u0415", None))
        self.edit_note.setPlaceholderText(QCoreApplication.translate("form_finactions_record", u"\u0417\u0430\u043c\u0435\u0442\u043a\u0430", None))
        self.edit_labels.setPlaceholderText(QCoreApplication.translate("form_finactions_record", u"\u041c\u0435\u0442\u043a\u0438", None))
    # retranslateUi


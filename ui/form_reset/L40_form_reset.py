# ФОРМА СБРОС ДАННЫХ: КАРКАС ДАННЫХ

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_cleanerawcUnh.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QHeaderView,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTreeView, QVBoxLayout, QWidget)

class Ui_frm_reset(object):
    def setupUi(self, frm_reset):
        if not frm_reset.objectName():
            frm_reset.setObjectName(u"frm_reset")
        frm_reset.resize(640, 480)
        self.centralwidget = QWidget(frm_reset)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.tre_objects = QTreeView(self.centralwidget)
        self.tre_objects.setObjectName(u"tre_objects")
        self.tre_objects.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tre_objects.setRootIsDecorated(False)
        self.tre_objects.setItemsExpandable(False)
        self.tre_objects.setExpandsOnDoubleClick(False)
        self.tre_objects.header().setVisible(False)
        self.tre_objects.header().setMinimumSectionSize(22)

        self.verticalLayout.addWidget(self.tre_objects)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.chb_all_periods = QCheckBox(self.centralwidget)
        self.chb_all_periods.setObjectName(u"chb_all_periods")

        self.verticalLayout.addWidget(self.chb_all_periods)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.btn_exec_delete = QPushButton(self.centralwidget)
        self.btn_exec_delete.setObjectName(u"btn_exec_delete")

        self.verticalLayout.addWidget(self.btn_exec_delete)

        frm_reset.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(frm_reset)
        self.statusbar.setObjectName(u"statusbar")
        frm_reset.setStatusBar(self.statusbar)

        self.retranslateUi(frm_reset)

        QMetaObject.connectSlotsByName(frm_reset)
    # setupUi

    def retranslateUi(self, frm_reset):
        frm_reset.setWindowTitle(QCoreApplication.translate("frm_reset", u"MainWindow", None))
        self.chb_all_periods.setText(QCoreApplication.translate("frm_reset", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430 \u0432\u0441\u0435 \u043f\u0435\u0440\u0438\u043e\u0434\u044b", None))
        self.btn_exec_delete.setText(QCoreApplication.translate("frm_reset", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
    # retranslateUi

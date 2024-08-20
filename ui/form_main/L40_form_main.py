# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_mainIolnEE.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_form_main(object):
    def setupUi(self, form_main):
        if not form_main.objectName():
            form_main.setObjectName(u"form_main")
        form_main.resize(800, 480)
        self.centralwidget = QWidget(form_main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cbbox_dm = QComboBox(self.centralwidget)
        self.cbbox_dm.setObjectName(u"cbbox_dm")

        self.horizontalLayout.addWidget(self.cbbox_dm)

        self.cbbox_dy = QComboBox(self.centralwidget)
        self.cbbox_dy.setObjectName(u"cbbox_dy")

        self.horizontalLayout.addWidget(self.cbbox_dy)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_dm_prev = QPushButton(self.centralwidget)
        self.btn_dm_prev.setObjectName(u"btn_dm_prev")

        self.horizontalLayout.addWidget(self.btn_dm_prev)

        self.btn_dm_next = QPushButton(self.centralwidget)
        self.btn_dm_next.setObjectName(u"btn_dm_next")

        self.horizontalLayout.addWidget(self.btn_dm_next)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_fincomposition = QPushButton(self.centralwidget)
        self.btn_fincomposition.setObjectName(u"btn_fincomposition")

        self.gridLayout.addWidget(self.btn_fincomposition, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        form_main.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(form_main)
        self.statusbar.setObjectName(u"statusbar")
        form_main.setStatusBar(self.statusbar)

        self.retranslateUi(form_main)

        QMetaObject.connectSlotsByName(form_main)
    # setupUi

    def retranslateUi(self, form_main):
        form_main.setWindowTitle(QCoreApplication.translate("form_main", u"MainWindow", None))
        self.btn_dm_prev.setText("")
        self.btn_dm_next.setText("")
        self.btn_fincomposition.setText(QCoreApplication.translate("form_main", u"\u0424\u0438\u043d\u0441\u043e\u0441\u0442\u0430\u0432", None))
    # retranslateUi


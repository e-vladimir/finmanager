# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_mainNazNAq.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_form_main(object):
    def setupUi(self, form_main):
        if not form_main.objectName():
            form_main.setObjectName(u"form_main")
        form_main.resize(800, 639)
        self.centralwidget = QWidget(form_main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_dmdy = QPushButton(self.centralwidget)
        self.btn_dmdy.setObjectName(u"btn_dmdy")
        self.btn_dmdy.setMinimumSize(QSize(120, 0))

        self.horizontalLayout.addWidget(self.btn_dmdy)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_dm_prev = QPushButton(self.centralwidget)
        self.btn_dm_prev.setObjectName(u"btn_dm_prev")
        self.btn_dm_prev.setMinimumSize(QSize(32, 0))
        self.btn_dm_prev.setMaximumSize(QSize(48, 16777215))

        self.horizontalLayout.addWidget(self.btn_dm_prev)

        self.btn_dm_next = QPushButton(self.centralwidget)
        self.btn_dm_next.setObjectName(u"btn_dm_next")
        self.btn_dm_next.setMinimumSize(QSize(32, 0))
        self.btn_dm_next.setMaximumSize(QSize(48, 16777215))

        self.horizontalLayout.addWidget(self.btn_dm_next)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setBold(True)
        self.label_4.setFont(font)

        self.horizontalLayout_9.addWidget(self.label_4)

        self.line_6 = QFrame(self.centralwidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_9.addWidget(self.line_6)

        self.horizontalLayout_9.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btn_accounts = QPushButton(self.centralwidget)
        self.btn_accounts.setObjectName(u"btn_accounts")
        self.btn_accounts.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_8.addWidget(self.btn_accounts)

        self.btn_operations = QPushButton(self.centralwidget)
        self.btn_operations.setObjectName(u"btn_operations")
        self.btn_operations.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_8.addWidget(self.btn_operations)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_9)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_3)

        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_6.addWidget(self.line_5)

        self.horizontalLayout_6.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btn_archives = QPushButton(self.centralwidget)
        self.btn_archives.setObjectName(u"btn_archives")
        self.btn_archives.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_7.addWidget(self.btn_archives)

        self.btn_rules = QPushButton(self.centralwidget)
        self.btn_rules.setObjectName(u"btn_rules")
        self.btn_rules.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_7.addWidget(self.btn_rules)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_5 = QSpacerItem(17, 120, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        form_main.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(form_main)
        self.statusbar.setObjectName(u"statusbar")
        form_main.setStatusBar(self.statusbar)

        self.retranslateUi(form_main)

        QMetaObject.connectSlotsByName(form_main)
    # setupUi

    def retranslateUi(self, form_main):
        form_main.setWindowTitle(QCoreApplication.translate("form_main", u"MainWindow", None))
        self.btn_dmdy.setText(QCoreApplication.translate("form_main", u"\u043c\u0435\u0441 \u0413\u0413\u0413\u0413", None))
        self.btn_dm_prev.setText("")
        self.btn_dm_next.setText("")
        self.label_4.setText(QCoreApplication.translate("form_main", u"\u0414\u0410\u041d\u041d\u042b\u0415", None))
        self.btn_accounts.setText(QCoreApplication.translate("form_main", u"\u0421\u0447\u0435\u0442\u0430", None))
        self.btn_operations.setText(QCoreApplication.translate("form_main", u"\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u0438", None))
        self.label_3.setText(QCoreApplication.translate("form_main", u"\u0423\u0422\u0418\u041b\u0418\u0422\u042b", None))
        self.btn_archives.setText(QCoreApplication.translate("form_main", u"\u0410\u0440\u0445\u0438\u0432\u044b", None))
        self.btn_rules.setText(QCoreApplication.translate("form_main", u"\u041f\u0440\u0430\u0432\u0438\u043b\u0430", None))
    # retranslateUi


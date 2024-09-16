# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_mainDwGoiv.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_form_main(object):
    def setupUi(self, form_main):
        if not form_main.objectName():
            form_main.setObjectName(u"form_main")
        form_main.resize(800, 480)
        self.centralwidget = QWidget(form_main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
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

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_2)

        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_fincomposition = QPushButton(self.centralwidget)
        self.btn_fincomposition.setObjectName(u"btn_fincomposition")
        self.btn_fincomposition.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_4.addWidget(self.btn_fincomposition)

        self.btn_rules = QPushButton(self.centralwidget)
        self.btn_rules.setObjectName(u"btn_rules")
        self.btn_rules.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_4.addWidget(self.btn_rules)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line_4)

        self.horizontalLayout_3.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btn_finstruct = QPushButton(self.centralwidget)
        self.btn_finstruct.setObjectName(u"btn_finstruct")
        self.btn_finstruct.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_5.addWidget(self.btn_finstruct)

        self.btn_finactions = QPushButton(self.centralwidget)
        self.btn_finactions.setObjectName(u"btn_finactions")
        self.btn_finactions.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_5.addWidget(self.btn_finactions)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_4)

        self.line_6 = QFrame(self.centralwidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_8.addWidget(self.line_6)

        self.horizontalLayout_8.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btn_finstatistics = QPushButton(self.centralwidget)
        self.btn_finstatistics.setObjectName(u"btn_finstatistics")
        self.btn_finstatistics.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_9.addWidget(self.btn_finstatistics)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_7)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.verticalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_8)

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
        self.btn_backup = QPushButton(self.centralwidget)
        self.btn_backup.setObjectName(u"btn_backup")
        self.btn_backup.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_7.addWidget(self.btn_backup)

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
        self.btn_dm_prev.setText("")
        self.btn_dm_next.setText("")
        self.label.setText(QCoreApplication.translate("form_main", u"\u041a\u0410\u0422\u0410\u041b\u041e\u0413\u0418", None))
        self.btn_fincomposition.setText(QCoreApplication.translate("form_main", u"\u0424\u0438\u043d\u0441\u043e\u0441\u0442\u0430\u0432", None))
        self.btn_rules.setText(QCoreApplication.translate("form_main", u"\u041f\u0440\u0430\u0432\u0438\u043b\u0430", None))
        self.label_2.setText(QCoreApplication.translate("form_main", u"\u0414\u0410\u041d\u041d\u042b\u0415", None))
        self.btn_finstruct.setText(QCoreApplication.translate("form_main", u"\u0424\u0438\u043d\u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u0430", None))
        self.btn_finactions.setText(QCoreApplication.translate("form_main", u"\u0424\u0438\u043d\u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f", None))
        self.label_4.setText(QCoreApplication.translate("form_main", u"\u0410\u041d\u0410\u041b\u0418\u0422\u0418\u041a\u0410", None))
        self.btn_finstatistics.setText(QCoreApplication.translate("form_main", u"\u0424\u0438\u043d\u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
        self.label_3.setText(QCoreApplication.translate("form_main", u"\u0423\u0422\u0418\u041b\u0418\u0422\u042b", None))
        self.btn_backup.setText(QCoreApplication.translate("form_main", u"\u041a\u043e\u043f\u0438\u0438 \u0434\u0430\u043d\u043d\u044b\u0445", None))
    # retranslateUi


# ФОРМА ОСНОВНАЯ: КАРКАС ДАННЫХ

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_mainQgjKEl.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_form_main(object):
    def setupUi(self, form_main):
        if not form_main.objectName():
            form_main.setObjectName(u"form_main")
        form_main.resize(800, 509)
        self.centralwidget = QWidget(form_main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cbbox_dm = QComboBox(self.centralwidget)
        self.cbbox_dm.setObjectName(u"cbbox_dm")
        self.cbbox_dm.setMinimumSize(QSize(120, 0))

        self.horizontalLayout.addWidget(self.cbbox_dm)

        self.cbbox_dy = QComboBox(self.centralwidget)
        self.cbbox_dy.setObjectName(u"cbbox_dy")
        self.cbbox_dy.setMinimumSize(QSize(120, 0))

        self.horizontalLayout.addWidget(self.cbbox_dy)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_dm_prev = QPushButton(self.centralwidget)
        self.btn_dm_prev.setObjectName(u"btn_dm_prev")
        self.btn_dm_prev.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout.addWidget(self.btn_dm_prev)

        self.btn_dm_next = QPushButton(self.centralwidget)
        self.btn_dm_next.setObjectName(u"btn_dm_next")
        self.btn_dm_next.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout.addWidget(self.btn_dm_next)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_findescription = QPushButton(self.centralwidget)
        self.btn_findescription.setObjectName(u"btn_findescription")
        self.btn_findescription.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.btn_findescription, 1, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setIndent(2)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.btn_finanalytics = QPushButton(self.centralwidget)
        self.btn_finanalytics.setObjectName(u"btn_finanalytics")

        self.gridLayout.addWidget(self.btn_finanalytics, 10, 1, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout.addWidget(self.label_5, 15, 0, 1, 3)

        self.btn_finstruct = QPushButton(self.centralwidget)
        self.btn_finstruct.setObjectName(u"btn_finstruct")
        self.btn_finstruct.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.btn_finstruct, 4, 0, 1, 1)

        self.btn_finstatistic = QPushButton(self.centralwidget)
        self.btn_finstatistic.setObjectName(u"btn_finstatistic")

        self.gridLayout.addWidget(self.btn_finstatistic, 10, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_6, 14, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setIndent(2)

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 3)

        self.btn_findata = QPushButton(self.centralwidget)
        self.btn_findata.setObjectName(u"btn_findata")

        self.gridLayout.addWidget(self.btn_findata, 4, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 2, 0, 1, 1)

        self.btn_rules = QPushButton(self.centralwidget)
        self.btn_rules.setObjectName(u"btn_rules")

        self.gridLayout.addWidget(self.btn_rules, 1, 1, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 12, 0, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 9, 0, 1, 3)

        self.btn_cleaner = QPushButton(self.centralwidget)
        self.btn_cleaner.setObjectName(u"btn_cleaner")

        self.gridLayout.addWidget(self.btn_cleaner, 16, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)

        self.btn_backups = QPushButton(self.centralwidget)
        self.btn_backups.setObjectName(u"btn_backups")

        self.gridLayout.addWidget(self.btn_backups, 16, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_4, 5, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 17, 0, 1, 1)

        self.btn_report_summary = QPushButton(self.centralwidget)
        self.btn_report_summary.setObjectName(u"btn_report_summary")

        self.gridLayout.addWidget(self.btn_report_summary, 13, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_5, 11, 0, 1, 1)

        self.btn_report_finstate = QPushButton(self.centralwidget)
        self.btn_report_finstate.setObjectName(u"btn_report_finstate")

        self.gridLayout.addWidget(self.btn_report_finstate, 13, 1, 1, 1)

        self.gridLayout.setColumnMinimumWidth(0, 120)
        self.gridLayout.setColumnMinimumWidth(1, 120)

        self.verticalLayout.addLayout(self.gridLayout)

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
        self.btn_findescription.setText(QCoreApplication.translate("form_main", u"\u0424\u0438\u043d\u0441\u043e\u0441\u0442\u0430\u0432", None))
        self.label.setText(QCoreApplication.translate("form_main", u"\u041a\u0410\u0422\u0410\u041b\u041e\u0413\u0418", None))
        self.btn_finanalytics.setText(QCoreApplication.translate("form_main", u"\u0424\u0438\u043d\u0430\u043d\u0430\u043b\u0438\u0442\u0438\u043a\u0430", None))
        self.label_5.setText(QCoreApplication.translate("form_main", u"\u0423\u0422\u0418\u041b\u0418\u0422\u042b", None))
        self.btn_finstruct.setText(QCoreApplication.translate("form_main", u"\u0424\u0438\u043d\u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u0430", None))
        self.btn_finstatistic.setText(QCoreApplication.translate("form_main", u"\u0424\u0438\u043d\u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
        self.label_2.setText(QCoreApplication.translate("form_main", u"\u041e\u041f\u0415\u0420\u0410\u0422\u0418\u0412\u041d\u042b\u0415 \u0414\u0410\u041d\u041d\u042b\u0415", None))
        self.btn_findata.setText(QCoreApplication.translate("form_main", u"\u0424\u0438\u043d\u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.btn_rules.setText(QCoreApplication.translate("form_main", u"\u041f\u0440\u0430\u0432\u0438\u043b\u0430", None))
        self.label_3.setText(QCoreApplication.translate("form_main", u"\u041e\u0422\u0427\u0401\u0422\u041d\u041e\u0421\u0422\u042c", None))
        self.label_4.setText(QCoreApplication.translate("form_main", u"\u0410\u041d\u0410\u041b\u0418\u0422\u0418\u041a\u0410", None))
        self.btn_cleaner.setText(QCoreApplication.translate("form_main", u"\u0421\u0431\u0440\u043e\u0441 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.btn_backups.setText(QCoreApplication.translate("form_main", u"\u041a\u043e\u043f\u0438\u0438 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.btn_report_summary.setText(QCoreApplication.translate("form_main", u"\u0421\u0432\u043e\u0434\u043d\u044b\u0439 \u043e\u0442\u0447\u0451\u0442", None))
        self.btn_report_finstate.setText(QCoreApplication.translate("form_main", u"\u0424\u0438\u043d\u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435", None))
    # retranslateUi

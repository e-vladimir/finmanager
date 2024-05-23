# ФОРМА ЭКСПОРТА: КАРКАС ДАННЫХ

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_exportXsIrat.ui'
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
    QSpacerItem, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_frm_export(object):
    def setupUi(self, frm_export):
        if not frm_export.objectName():
            frm_export.setObjectName(u"frm_export")
        frm_export.resize(700, 480)
        self.centralwidget = QWidget(frm_export)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.tbs_input = QTabWidget(self.centralwidget)
        self.tbs_input.setObjectName(u"tbs_input")
        self.tbs_input.setMinimumSize(QSize(400, 0))
        self.tab_findata = QWidget()
        self.tab_findata.setObjectName(u"tab_findata")
        self.gridLayout_2 = QGridLayout(self.tab_findata)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setVerticalSpacing(3)
        self.gridLayout_2.setContentsMargins(3, 3, 3, 3)
        self.cbb_findata_dy = QComboBox(self.tab_findata)
        self.cbb_findata_dy.setObjectName(u"cbb_findata_dy")

        self.gridLayout_2.addWidget(self.cbb_findata_dy, 8, 1, 1, 1)

        self.lbl_findata_filename = QLabel(self.tab_findata)
        self.lbl_findata_filename.setObjectName(u"lbl_findata_filename")

        self.gridLayout_2.addWidget(self.lbl_findata_filename, 2, 1, 1, 1)

        self.label_9 = QLabel(self.tab_findata)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_9, 9, 0, 1, 1)

        self.label_5 = QLabel(self.tab_findata)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_5, 7, 0, 1, 1)

        self.label_12 = QLabel(self.tab_findata)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_12, 2, 0, 1, 1)

        self.cbb_findata_finstruct = QComboBox(self.tab_findata)
        self.cbb_findata_finstruct.setObjectName(u"cbb_findata_finstruct")

        self.gridLayout_2.addWidget(self.cbb_findata_finstruct, 5, 1, 1, 1)

        self.label_15 = QLabel(self.tab_findata)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_15, 0, 0, 1, 1)

        self.label_13 = QLabel(self.tab_findata)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_13, 4, 0, 1, 1)

        self.label_7 = QLabel(self.tab_findata)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_7, 8, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 10, 0, 1, 1)

        self.btn_findata_directory = QPushButton(self.tab_findata)
        self.btn_findata_directory.setObjectName(u"btn_findata_directory")

        self.gridLayout_2.addWidget(self.btn_findata_directory, 1, 1, 1, 1)

        self.cbb_findata_dm = QComboBox(self.tab_findata)
        self.cbb_findata_dm.setObjectName(u"cbb_findata_dm")

        self.gridLayout_2.addWidget(self.cbb_findata_dm, 9, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_6, 3, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_7, 6, 0, 1, 1)

        self.label_3 = QLabel(self.tab_findata)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_14 = QLabel(self.tab_findata)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_14, 5, 0, 1, 1)

        self.gridLayout_2.setColumnStretch(1, 1)
        self.tbs_input.addTab(self.tab_findata, "")

        self.horizontalLayout.addWidget(self.tbs_input)

        self.tbs_output = QTabWidget(self.centralwidget)
        self.tbs_output.setObjectName(u"tbs_output")
        self.tbs_output.setMinimumSize(QSize(250, 0))
        self.tab_statistic = QWidget()
        self.tab_statistic.setObjectName(u"tab_statistic")
        self.verticalLayout = QVBoxLayout(self.tab_statistic)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.tab_statistic)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)

        self.label_2 = QLabel(self.tab_statistic)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_6 = QLabel(self.tab_statistic)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.lbl_statistic_count_exported = QLabel(self.tab_statistic)
        self.lbl_statistic_count_exported.setObjectName(u"lbl_statistic_count_exported")
        self.lbl_statistic_count_exported.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_statistic_count_exported, 5, 1, 1, 1)

        self.label = QLabel(self.tab_statistic)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 9, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 4, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.label_11 = QLabel(self.tab_statistic)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_11, 8, 0, 1, 1)

        self.lbl_statistic_time_left = QLabel(self.tab_statistic)
        self.lbl_statistic_time_left.setObjectName(u"lbl_statistic_time_left")
        self.lbl_statistic_time_left.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_statistic_time_left, 8, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_4, 6, 0, 1, 1)

        self.lbl_statistic_time_processed = QLabel(self.tab_statistic)
        self.lbl_statistic_time_processed.setObjectName(u"lbl_statistic_time_processed")
        self.lbl_statistic_time_processed.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_statistic_time_processed, 7, 1, 1, 1)

        self.label_10 = QLabel(self.tab_statistic)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_10, 7, 0, 1, 1)

        self.lbl_statistic_count_left = QLabel(self.tab_statistic)
        self.lbl_statistic_count_left.setObjectName(u"lbl_statistic_count_left")
        self.lbl_statistic_count_left.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_statistic_count_left, 3, 1, 1, 1)

        self.lbl_statistic_count_processed = QLabel(self.tab_statistic)
        self.lbl_statistic_count_processed.setObjectName(u"lbl_statistic_count_processed")
        self.lbl_statistic_count_processed.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_statistic_count_processed, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.btn_exec_export = QPushButton(self.tab_statistic)
        self.btn_exec_export.setObjectName(u"btn_exec_export")

        self.verticalLayout.addWidget(self.btn_exec_export)

        self.verticalLayout.setStretch(0, 1)
        self.tbs_output.addTab(self.tab_statistic, "")

        self.horizontalLayout.addWidget(self.tbs_output)

        self.horizontalLayout.setStretch(0, 1)
        frm_export.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(frm_export)
        self.statusbar.setObjectName(u"statusbar")
        frm_export.setStatusBar(self.statusbar)

        self.retranslateUi(frm_export)

        self.tbs_input.setCurrentIndex(0)
        self.tbs_output.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(frm_export)
    # setupUi

    def retranslateUi(self, frm_export):
        frm_export.setWindowTitle(QCoreApplication.translate("frm_export", u"MainWindow", None))
        self.lbl_findata_filename.setText(QCoreApplication.translate("frm_export", u"...", None))
        self.label_9.setText(QCoreApplication.translate("frm_export", u"\u041c\u0435\u0441\u044f\u0446", None))
        self.label_5.setText(QCoreApplication.translate("frm_export", u"\u041f\u0415\u0420\u0418\u041e\u0414 \u042d\u041a\u0421\u041f\u041e\u0420\u0422\u0410", None))
        self.label_12.setText(QCoreApplication.translate("frm_export", u"\u0418\u043c\u044f \u0444\u0430\u0439\u043b\u0430", None))
        self.label_15.setText(QCoreApplication.translate("frm_export", u"\u041d\u0410\u0417\u041d\u0410\u0427\u0415\u041d\u0418\u0415", None))
        self.label_13.setText(QCoreApplication.translate("frm_export", u"\u041f\u0410\u0420\u0410\u041c\u0415\u0422\u0420\u042b", None))
        self.label_7.setText(QCoreApplication.translate("frm_export", u"\u0413\u043e\u0434", None))
        self.btn_findata_directory.setText(QCoreApplication.translate("frm_export", u"...", None))
        self.label_3.setText(QCoreApplication.translate("frm_export", u"\u0414\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0438\u044f \u044d\u043a\u0441\u043f\u043e\u0440\u0442\u0430", None))
        self.label_14.setText(QCoreApplication.translate("frm_export", u"\u0424\u0438\u043d\u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u0430", None))
        self.tbs_input.setTabText(self.tbs_input.indexOf(self.tab_findata), QCoreApplication.translate("frm_export", u"\u0424\u0438\u043d\u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.label_4.setText(QCoreApplication.translate("frm_export", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u043e", None))
        self.label_2.setText(QCoreApplication.translate("frm_export", u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u043d\u043e", None))
        self.label_6.setText(QCoreApplication.translate("frm_export", u"\u041e\u0441\u0442\u0430\u043b\u043e\u0441\u044c \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c", None))
        self.lbl_statistic_count_exported.setText(QCoreApplication.translate("frm_export", u"0", None))
        self.label.setText(QCoreApplication.translate("frm_export", u"\u0421\u0422\u0410\u0422\u0418\u0421\u0422\u0418\u041a\u0410", None))
        self.label_11.setText(QCoreApplication.translate("frm_export", u"\u0412\u0440\u0435\u043c\u044f \u043e\u0436\u0438\u0434\u0430\u043d\u0438\u044f", None))
        self.lbl_statistic_time_left.setText(QCoreApplication.translate("frm_export", u"00\u0447 00\u043c 00\u0441", None))
        self.lbl_statistic_time_processed.setText(QCoreApplication.translate("frm_export", u"00\u0447 00\u043c 00\u0441", None))
        self.label_10.setText(QCoreApplication.translate("frm_export", u"\u0412\u0440\u0435\u043c\u044f \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438", None))
        self.lbl_statistic_count_left.setText(QCoreApplication.translate("frm_export", u"0", None))
        self.lbl_statistic_count_processed.setText(QCoreApplication.translate("frm_export", u"0", None))
        self.btn_exec_export.setText(QCoreApplication.translate("frm_export", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c \u044d\u043a\u0441\u043f\u043e\u0440\u0442", None))
        self.tbs_output.setTabText(self.tbs_output.indexOf(self.tab_statistic), QCoreApplication.translate("frm_export", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442", None))
    # retranslateUi

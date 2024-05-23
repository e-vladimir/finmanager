# ФОРМА ИМПОРТА ДАННЫХ: КАРКАС ДАННЫХ

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_importDgWjJu.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_frm_import(object):
    def setupUi(self, frm_import):
        if not frm_import.objectName():
            frm_import.setObjectName(u"frm_import")
        frm_import.resize(771, 465)
        self.centralwidget = QWidget(frm_import)
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
        self.gridLayout_2.setContentsMargins(3, 3, 3, 3)
        self.lbl_findata_folder = QLabel(self.tab_findata)
        self.lbl_findata_folder.setObjectName(u"lbl_findata_folder")

        self.gridLayout_2.addWidget(self.lbl_findata_folder, 2, 1, 1, 1)

        self.btn_findata_file = QPushButton(self.tab_findata)
        self.btn_findata_file.setObjectName(u"btn_findata_file")
        self.btn_findata_file.setText(u"...")
        self.btn_findata_file.setAutoExclusive(False)
        self.btn_findata_file.setFlat(False)

        self.gridLayout_2.addWidget(self.btn_findata_file, 1, 1, 1, 1)

        self.label_19 = QLabel(self.tab_findata)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_19, 4, 0, 1, 1)

        self.label_20 = QLabel(self.tab_findata)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_20, 7, 0, 1, 1)

        self.label_15 = QLabel(self.tab_findata)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_15, 1, 0, 1, 1)

        self.cbb_findata_format = QComboBox(self.tab_findata)
        self.cbb_findata_format.setObjectName(u"cbb_findata_format")

        self.gridLayout_2.addWidget(self.cbb_findata_format, 4, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 8, 0, 1, 1)

        self.cbb_findata_finstruct = QComboBox(self.tab_findata)
        self.cbb_findata_finstruct.setObjectName(u"cbb_findata_finstruct")

        self.gridLayout_2.addWidget(self.cbb_findata_finstruct, 7, 1, 1, 1)

        self.label_16 = QLabel(self.tab_findata)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_16, 2, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(0, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_6, 5, 0, 1, 1)

        self.label_17 = QLabel(self.tab_findata)
        self.label_17.setObjectName(u"label_17")
        font = QFont()
        font.setBold(True)
        font.setItalic(False)
        self.label_17.setFont(font)
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_17, 6, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_7, 3, 0, 1, 1)

        self.label_14 = QLabel(self.tab_findata)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_14, 0, 0, 1, 1)

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
        self.label_6 = QLabel(self.tab_statistic)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.label_8 = QLabel(self.tab_statistic)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)

        self.lbl_statistic_time_processed = QLabel(self.tab_statistic)
        self.lbl_statistic_time_processed.setObjectName(u"lbl_statistic_time_processed")
        self.lbl_statistic_time_processed.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_statistic_time_processed, 8, 1, 1, 1)

        self.lbl_statistic_time_left = QLabel(self.tab_statistic)
        self.lbl_statistic_time_left.setObjectName(u"lbl_statistic_time_left")
        self.lbl_statistic_time_left.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_statistic_time_left, 9, 1, 1, 1)

        self.label_10 = QLabel(self.tab_statistic)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_10, 8, 0, 1, 1)

        self.label_2 = QLabel(self.tab_statistic)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 10, 0, 1, 1)

        self.lbl_statistic_count_left = QLabel(self.tab_statistic)
        self.lbl_statistic_count_left.setObjectName(u"lbl_statistic_count_left")
        self.lbl_statistic_count_left.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_statistic_count_left, 3, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 4, 0, 1, 1)

        self.lbl_statistic_count_skipped = QLabel(self.tab_statistic)
        self.lbl_statistic_count_skipped.setObjectName(u"lbl_statistic_count_skipped")
        self.lbl_statistic_count_skipped.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_statistic_count_skipped, 6, 1, 1, 1)

        self.lbl_statistic_count_imported = QLabel(self.tab_statistic)
        self.lbl_statistic_count_imported.setObjectName(u"lbl_statistic_count_imported")
        self.lbl_statistic_count_imported.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_statistic_count_imported, 5, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.lbl_statistic_count_processed = QLabel(self.tab_statistic)
        self.lbl_statistic_count_processed.setObjectName(u"lbl_statistic_count_processed")
        self.lbl_statistic_count_processed.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_statistic_count_processed, 2, 1, 1, 1)

        self.label_11 = QLabel(self.tab_statistic)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_11, 9, 0, 1, 1)

        self.label_4 = QLabel(self.tab_statistic)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_4, 7, 0, 1, 1)

        self.label = QLabel(self.tab_statistic)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.line_3 = QFrame(self.tab_statistic)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_3, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.btn_exec_import = QPushButton(self.tab_statistic)
        self.btn_exec_import.setObjectName(u"btn_exec_import")

        self.verticalLayout.addWidget(self.btn_exec_import)

        self.verticalLayout.setStretch(0, 1)
        self.tbs_output.addTab(self.tab_statistic, "")

        self.horizontalLayout.addWidget(self.tbs_output)

        self.horizontalLayout.setStretch(1, 1)
        frm_import.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(frm_import)
        self.statusbar.setObjectName(u"statusbar")
        frm_import.setStatusBar(self.statusbar)

        self.retranslateUi(frm_import)

        self.tbs_input.setCurrentIndex(0)
        self.tbs_output.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(frm_import)
    # setupUi

    def retranslateUi(self, frm_import):
        frm_import.setWindowTitle(QCoreApplication.translate("frm_import", u"MainWindow", None))
        self.lbl_findata_folder.setText(QCoreApplication.translate("frm_import", u"...", None))
        self.label_19.setText(QCoreApplication.translate("frm_import", u"\u0424\u043e\u0440\u043c\u0430\u0442", None))
        self.label_20.setText(QCoreApplication.translate("frm_import", u"\u0424\u0438\u043d\u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u0430", None))
        self.label_15.setText(QCoreApplication.translate("frm_import", u"CSV-\u0444\u0430\u0439\u043b", None))
        self.label_16.setText(QCoreApplication.translate("frm_import", u"\u0414\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0438\u044f", None))
        self.label_17.setText(QCoreApplication.translate("frm_import", u"\u041d\u0410\u0417\u041d\u0410\u0427\u0415\u041d\u0418\u0415", None))
        self.label_14.setText(QCoreApplication.translate("frm_import", u"\u0418\u0421\u0422\u041e\u0427\u041d\u0418\u041a \u0414\u0410\u041d\u041d\u042b\u0425", None))
        self.tbs_input.setTabText(self.tbs_input.indexOf(self.tab_findata), QCoreApplication.translate("frm_import", u"\u0424\u0438\u043d\u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.label_6.setText(QCoreApplication.translate("frm_import", u"\u041e\u0441\u0442\u0430\u043b\u043e\u0441\u044c \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c", None))
        self.label_8.setText(QCoreApplication.translate("frm_import", u"\u041f\u0440\u043e\u043f\u0443\u0449\u0435\u043d\u043e", None))
        self.lbl_statistic_time_processed.setText(QCoreApplication.translate("frm_import", u"00\u0447 00\u043c 00\u0441", None))
        self.lbl_statistic_time_left.setText(QCoreApplication.translate("frm_import", u"00\u0447 00\u043c 00\u0441", None))
        self.label_10.setText(QCoreApplication.translate("frm_import", u"\u0412\u0440\u0435\u043c\u044f \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438", None))
        self.label_2.setText(QCoreApplication.translate("frm_import", u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u043d\u043e", None))
        self.lbl_statistic_count_left.setText(QCoreApplication.translate("frm_import", u"0", None))
        self.lbl_statistic_count_skipped.setText(QCoreApplication.translate("frm_import", u"0", None))
        self.lbl_statistic_count_imported.setText(QCoreApplication.translate("frm_import", u"0", None))
        self.lbl_statistic_count_processed.setText(QCoreApplication.translate("frm_import", u"0", None))
        self.label_11.setText(QCoreApplication.translate("frm_import", u"\u0412\u0440\u0435\u043c\u044f \u043e\u0436\u0438\u0434\u0430\u043d\u0438\u044f", None))
        self.label_4.setText(QCoreApplication.translate("frm_import", u"\u0418\u043c\u043f\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u043e", None))
        self.label.setText(QCoreApplication.translate("frm_import", u"\u0421\u0422\u0410\u0422\u0418\u0421\u0422\u0418\u041a\u0410", None))
        self.btn_exec_import.setText(QCoreApplication.translate("frm_import", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c \u0438\u043c\u043f\u043e\u0440\u0442", None))
        self.tbs_output.setTabText(self.tbs_output.indexOf(self.tab_statistic), QCoreApplication.translate("frm_import", u"\u0418\u043c\u043f\u043e\u0440\u0442", None))
    # retranslateUi

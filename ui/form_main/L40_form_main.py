# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_mainBTZKKp.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QMainWindow, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

from L20_PySide6 import C20_ActiveLabel

class Ui_form_main(object):
    def setupUi(self, form_main):
        if not form_main.objectName():
            form_main.setObjectName(u"form_main")
        form_main.resize(1024, 768)
        self.centralwidget = QWidget(form_main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.gbox_dm_dy = QGroupBox(self.centralwidget)
        self.gbox_dm_dy.setObjectName(u"gbox_dm_dy")
        self.horizontalLayout = QHBoxLayout(self.gbox_dm_dy)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_dm_dy_prev = C20_ActiveLabel(self.gbox_dm_dy)
        self.label_dm_dy_prev.setObjectName(u"label_dm_dy_prev")
        self.label_dm_dy_prev.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_dm_dy_prev.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_dm_dy_prev)

        self.label_dm_dy = C20_ActiveLabel(self.gbox_dm_dy)
        self.label_dm_dy.setObjectName(u"label_dm_dy")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_dm_dy.setFont(font)
        self.label_dm_dy.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_dm_dy.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_dm_dy)

        self.label_dm_dy_next = C20_ActiveLabel(self.gbox_dm_dy)
        self.label_dm_dy_next.setObjectName(u"label_dm_dy_next")
        self.label_dm_dy_next.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_dm_dy_next.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_dm_dy_next)


        self.horizontalLayout_3.addWidget(self.gbox_dm_dy)

        self.gbox_accounts = QGroupBox(self.centralwidget)
        self.gbox_accounts.setObjectName(u"gbox_accounts")
        self.verticalLayout = QVBoxLayout(self.gbox_accounts)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_amout = C20_ActiveLabel(self.gbox_accounts)
        self.label_amout.setObjectName(u"label_amout")
        font1 = QFont()
        font1.setBold(True)
        self.label_amout.setFont(font1)
        self.label_amout.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_amout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_amout)

        self.label_5 = QLabel(self.gbox_accounts)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_5)


        self.horizontalLayout_3.addWidget(self.gbox_accounts)

        self.gbox_operations = QGroupBox(self.centralwidget)
        self.gbox_operations.setObjectName(u"gbox_operations")
        self.verticalLayout_3 = QVBoxLayout(self.gbox_operations)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_delta = C20_ActiveLabel(self.gbox_operations)
        self.label_delta.setObjectName(u"label_delta")
        self.label_delta.setFont(font1)
        self.label_delta.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_delta.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_delta)

        self.label__subdelta = QLabel(self.gbox_operations)
        self.label__subdelta.setObjectName(u"label__subdelta")
        self.label__subdelta.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label__subdelta)


        self.horizontalLayout_3.addWidget(self.gbox_operations)

        self.gbox_backup = QGroupBox(self.centralwidget)
        self.gbox_backup.setObjectName(u"gbox_backup")
        self.verticalLayout_4 = QVBoxLayout(self.gbox_backup)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_backup_dd_dm_dy = C20_ActiveLabel(self.gbox_backup)
        self.label_backup_dd_dm_dy.setObjectName(u"label_backup_dd_dm_dy")
        self.label_backup_dd_dm_dy.setFont(font1)
        self.label_backup_dd_dm_dy.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_backup_dd_dm_dy.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_backup_dd_dm_dy)

        self.label_backup_th_tm = QLabel(self.gbox_backup)
        self.label_backup_th_tm.setObjectName(u"label_backup_th_tm")
        self.label_backup_th_tm.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_backup_th_tm)


        self.horizontalLayout_3.addWidget(self.gbox_backup)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.gbox_dm_view = QGroupBox(self.centralwidget)
        self.gbox_dm_view.setObjectName(u"gbox_dm_view")

        self.verticalLayout_2.addWidget(self.gbox_dm_view)

        self.gbox_dm_analytics = QGroupBox(self.centralwidget)
        self.gbox_dm_analytics.setObjectName(u"gbox_dm_analytics")

        self.verticalLayout_2.addWidget(self.gbox_dm_analytics)

        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        form_main.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(form_main)
        self.statusbar.setObjectName(u"statusbar")
        form_main.setStatusBar(self.statusbar)

        self.retranslateUi(form_main)

        QMetaObject.connectSlotsByName(form_main)
    # setupUi

    def retranslateUi(self, form_main):
        form_main.setWindowTitle(QCoreApplication.translate("form_main", u"MainWindow", None))
        self.gbox_dm_dy.setTitle(QCoreApplication.translate("form_main", u"\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u043f\u0435\u0440\u0438\u043e\u0434", None))
        self.label_dm_dy_prev.setText(QCoreApplication.translate("form_main", u"\u044f\u043d\u0432<br>2025", None))
        self.label_dm_dy.setText(QCoreApplication.translate("form_main", u"\u0424\u0415\u0412<br>2025", None))
        self.label_dm_dy_next.setText(QCoreApplication.translate("form_main", u"\u043c\u0430\u0440<br>2025", None))
        self.gbox_accounts.setTitle(QCoreApplication.translate("form_main", u"\u0421\u0447\u0435\u0442\u0430", None))
        self.label_amout.setText(QCoreApplication.translate("form_main", u"000 000", None))
        self.label_5.setText(QCoreApplication.translate("form_main", u"\u043e\u0441\u0442\u0430\u0442\u043e\u043a \u043d\u0430 \u043d\u0430\u0447\u0430\u043b\u043e \u043c\u0435\u0441\u044f\u0446\u0430", None))
        self.gbox_operations.setTitle(QCoreApplication.translate("form_main", u"\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u0438", None))
        self.label_delta.setText(QCoreApplication.translate("form_main", u"+000 000", None))
        self.label__subdelta.setText(QCoreApplication.translate("form_main", u"+000 000 / -000 000", None))
        self.gbox_backup.setTitle(QCoreApplication.translate("form_main", u"\u041a\u043e\u043f\u0438\u044f \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.label_backup_dd_dm_dy.setText(QCoreApplication.translate("form_main", u"00 \u041c\u0415\u0421 0000", None))
        self.label_backup_th_tm.setText(QCoreApplication.translate("form_main", u"00:00", None))
        self.gbox_dm_view.setTitle(QCoreApplication.translate("form_main", u"\u041e\u0431\u0437\u043e\u0440 \u043c\u0435\u0441\u044f\u0446\u0430", None))
        self.gbox_dm_analytics.setTitle(QCoreApplication.translate("form_main", u"\u0410\u043d\u0430\u043b\u0438\u0442\u0438\u043a\u0430 \u043c\u0435\u0441\u044f\u0446\u0430", None))
    # retranslateUi


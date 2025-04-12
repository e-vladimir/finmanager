# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_mainufKzak.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
    QMainWindow, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

from L20_PySide6 import C20_ActiveLabel
from L21_dia_dm_view import C21_DiaDmView

class Ui_FormMain(object):
    def setupUi(self, FormMain):
        if not FormMain.objectName():
            FormMain.setObjectName(u"FormMain")
        FormMain.resize(1024, 768)
        self.centralwidget = QWidget(FormMain)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.GBoxDmDy = QGroupBox(self.centralwidget)
        self.GBoxDmDy.setObjectName(u"GBoxDmDy")
        self.horizontalLayout = QHBoxLayout(self.GBoxDmDy)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.LabelPrevDmDy = C20_ActiveLabel(self.GBoxDmDy)
        self.LabelPrevDmDy.setObjectName(u"LabelPrevDmDy")
        self.LabelPrevDmDy.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.LabelPrevDmDy.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.LabelPrevDmDy)

        self.LabelDmDy = C20_ActiveLabel(self.GBoxDmDy)
        self.LabelDmDy.setObjectName(u"LabelDmDy")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.LabelDmDy.setFont(font)
        self.LabelDmDy.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.LabelDmDy.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.LabelDmDy)

        self.LabelNextDmDy = C20_ActiveLabel(self.GBoxDmDy)
        self.LabelNextDmDy.setObjectName(u"LabelNextDmDy")
        self.LabelNextDmDy.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.LabelNextDmDy.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.LabelNextDmDy)


        self.horizontalLayout_3.addWidget(self.GBoxDmDy)

        self.GBoxAccounts = QGroupBox(self.centralwidget)
        self.GBoxAccounts.setObjectName(u"GBoxAccounts")
        self.verticalLayout = QVBoxLayout(self.GBoxAccounts)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.LabelInitialBalance = C20_ActiveLabel(self.GBoxAccounts)
        self.LabelInitialBalance.setObjectName(u"LabelInitialBalance")
        font1 = QFont()
        font1.setBold(True)
        self.LabelInitialBalance.setFont(font1)
        self.LabelInitialBalance.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.LabelInitialBalance.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.LabelInitialBalance)

        self.label_5 = QLabel(self.GBoxAccounts)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_5)


        self.horizontalLayout_3.addWidget(self.GBoxAccounts)

        self.GBoxOperations = QGroupBox(self.centralwidget)
        self.GBoxOperations.setObjectName(u"GBoxOperations")
        self.verticalLayout_3 = QVBoxLayout(self.GBoxOperations)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.LabelDelta = C20_ActiveLabel(self.GBoxOperations)
        self.LabelDelta.setObjectName(u"LabelDelta")
        self.LabelDelta.setFont(font1)
        self.LabelDelta.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.LabelDelta.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.LabelDelta)

        self.LabelSubdelta = QLabel(self.GBoxOperations)
        self.LabelSubdelta.setObjectName(u"LabelSubdelta")
        self.LabelSubdelta.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.LabelSubdelta)


        self.horizontalLayout_3.addWidget(self.GBoxOperations)

        self.GBoxBackup = QGroupBox(self.centralwidget)
        self.GBoxBackup.setObjectName(u"GBoxBackup")
        self.verticalLayout_4 = QVBoxLayout(self.GBoxBackup)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.LabelBackupDdDmDy = C20_ActiveLabel(self.GBoxBackup)
        self.LabelBackupDdDmDy.setObjectName(u"LabelBackupDdDmDy")
        self.LabelBackupDdDmDy.setFont(font1)
        self.LabelBackupDdDmDy.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.LabelBackupDdDmDy.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.LabelBackupDdDmDy)

        self.LabelBackupThTm = QLabel(self.GBoxBackup)
        self.LabelBackupThTm.setObjectName(u"LabelBackupThTm")
        self.LabelBackupThTm.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.LabelBackupThTm)


        self.horizontalLayout_3.addWidget(self.GBoxBackup)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.GBoxDmView = QGroupBox(self.centralwidget)
        self.GBoxDmView.setObjectName(u"GBoxDmView")
        self.GBoxDmView.setMaximumSize(QSize(16777215, 300))
        self.verticalLayout_5 = QVBoxLayout(self.GBoxDmView)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.DiaDmViewer = C21_DiaDmView(self.GBoxDmView)
        self.DiaDmViewer.setObjectName(u"DiaDmViewer")
        self.DiaDmViewer.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.DiaDmViewer)


        self.verticalLayout_2.addWidget(self.GBoxDmView)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.verticalLayout_2.setStretch(1, 1)
        FormMain.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(FormMain)
        self.statusbar.setObjectName(u"statusbar")
        FormMain.setStatusBar(self.statusbar)

        self.retranslateUi(FormMain)

        QMetaObject.connectSlotsByName(FormMain)
    # setupUi

    def retranslateUi(self, FormMain):
        FormMain.setWindowTitle(QCoreApplication.translate("FormMain", u"MainWindow", None))
        self.GBoxDmDy.setTitle(QCoreApplication.translate("FormMain", u"\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u043f\u0435\u0440\u0438\u043e\u0434", None))
        self.LabelPrevDmDy.setText(QCoreApplication.translate("FormMain", u"\u044f\u043d\u0432<br>2025", None))
        self.LabelDmDy.setText(QCoreApplication.translate("FormMain", u"\u0424\u0415\u0412<br>2025", None))
        self.LabelNextDmDy.setText(QCoreApplication.translate("FormMain", u"\u043c\u0430\u0440<br>2025", None))
        self.GBoxAccounts.setTitle(QCoreApplication.translate("FormMain", u"\u0421\u0447\u0435\u0442\u0430", None))
        self.LabelInitialBalance.setText(QCoreApplication.translate("FormMain", u"000 000", None))
        self.label_5.setText(QCoreApplication.translate("FormMain", u"\u043e\u0441\u0442\u0430\u0442\u043e\u043a \u043d\u0430 \u043d\u0430\u0447\u0430\u043b\u043e \u043c\u0435\u0441\u044f\u0446\u0430", None))
        self.GBoxOperations.setTitle(QCoreApplication.translate("FormMain", u"\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u0438", None))
        self.LabelDelta.setText(QCoreApplication.translate("FormMain", u"+000 000", None))
        self.LabelSubdelta.setText(QCoreApplication.translate("FormMain", u"+000 000 / -000 000", None))
        self.GBoxBackup.setTitle(QCoreApplication.translate("FormMain", u"\u041a\u043e\u043f\u0438\u044f \u0430\u0440\u0445\u0438\u0432\u0430 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.LabelBackupDdDmDy.setText(QCoreApplication.translate("FormMain", u"00 \u041c\u0415\u0421 0000", None))
        self.LabelBackupThTm.setText(QCoreApplication.translate("FormMain", u"00:00", None))
        self.GBoxDmView.setTitle(QCoreApplication.translate("FormMain", u"\u041e\u0431\u0437\u043e\u0440 \u043c\u0435\u0441\u044f\u0446\u0430", None))
    # retranslateUi


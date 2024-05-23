# ФОРМА ПРАВИЛ ОБРАБОТКИ: КАРКАС ДАННЫХ

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_rulesAAdzMI.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QHeaderView,
    QMainWindow, QSizePolicy, QStatusBar, QTreeView,
    QVBoxLayout, QWidget)

class Ui_form_rules(object):
    def setupUi(self, form_rules):
        if not form_rules.objectName():
            form_rules.setObjectName(u"form_rules")
        form_rules.resize(800, 600)
        self.centralwidget = QWidget(form_rules)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.cbbox_rules_types = QComboBox(self.centralwidget)
        self.cbbox_rules_types.setObjectName(u"cbbox_rules_types")

        self.verticalLayout_3.addWidget(self.cbbox_rules_types)

        self.tree_data = QTreeView(self.centralwidget)
        self.tree_data.setObjectName(u"tree_data")
        self.tree_data.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tree_data.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tree_data.setAlternatingRowColors(True)
        self.tree_data.setRootIsDecorated(False)
        self.tree_data.setItemsExpandable(False)
        self.tree_data.setExpandsOnDoubleClick(False)
        self.tree_data.header().setMinimumSectionSize(20)

        self.verticalLayout_3.addWidget(self.tree_data)

        form_rules.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(form_rules)
        self.statusbar.setObjectName(u"statusbar")
        form_rules.setStatusBar(self.statusbar)

        self.retranslateUi(form_rules)

        QMetaObject.connectSlotsByName(form_rules)
    # setupUi

    def retranslateUi(self, form_rules):
        form_rules.setWindowTitle(QCoreApplication.translate("form_rules", u"\u041f\u0440\u0430\u0432\u0438\u043b\u0430", None))
    # retranslateUi

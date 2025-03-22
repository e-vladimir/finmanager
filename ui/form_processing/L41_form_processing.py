# ФОРМА ОБРАБОТКА ДАННЫХ: МОДЕЛЬ UI
# 22 мар 2025

from PySide6.QtGui       import QAction, QIcon
from PySide6.QtWidgets   import QMenu

from L20_PySide6         import C20_PySideForm
from L40_form_processing import Ui_FormProcessing


class C41_FormProcessing(C20_PySideForm, Ui_FormProcessing):
	""" Форма Обработка данных: Модель UI """

	def InitUi(self): self.setupUi(self)

	def InitMenus(self):
		""" Инициализация меню """
		self.InitMenuOperations()

	def InitMenuOperations(self):
		""" Инициализацию меню операций """
		icon_arrow_r1    = QIcon("./L0/icons/arrow_right.svg")
		icon_arrow_r2    = QIcon("./L0/icons/arrow_right_2.svg")
		icon_edit        = QIcon("./L0/icons/edit.svg")
		icon_replace     = QIcon("./L0/icons/replace.svg")
		icon_square_blue = QIcon("./L0/icons/square_blue.svg")

		self.ActionSetOperationsFilterDescription            = QAction(icon_edit,        "Описание содержит...")
		self.ActionSetOperationsProcessingReplaceDescription = QAction(icon_arrow_r1,    "Заменить фрагмент описания")
		self.ActionSetOperationsProcessingSetDescription     = QAction(icon_arrow_r2,    "Установить фрагмент")
		self.ActionSetOperationsProcessingSetColor           = QAction(icon_square_blue, "Установить цвет")
		self.ActionProcessingOperations                      = QAction(icon_replace,     "Выполнить обработку")

		self.MenuOperation                                   = QMenu("Обработка операций")
		self.MenuOperation.addSection("Критерии фильтрации")
		self.MenuOperation.addAction(self.ActionSetOperationsFilterDescription)

		self.MenuOperation.addSection("Обработка операций")
		self.MenuOperation.addAction(self.ActionSetOperationsProcessingReplaceDescription)
		self.MenuOperation.addAction(self.ActionSetOperationsProcessingSetDescription)
		self.MenuOperation.addAction(self.ActionSetOperationsProcessingSetColor)

		self.MenuOperation.addSeparator()
		self.MenuOperation.addAction(self.ActionProcessingOperations)

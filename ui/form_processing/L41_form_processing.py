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
		self.InitMenuManual()
		self.InitMenuAuto()

	def InitMenuManual(self):
		""" Инициализация меню Ручная обработка """
		icon_blocks     = QIcon("./L0/icons/blocks.svg")
		icon_layers     = QIcon("./L0/icons/layers.svg")
		icon_processing = QIcon("./L0/icons/processing.svg")

		self.ActionManualObjectsTypeOperations = QAction(icon_blocks,     "Операции")
		self.ActionManualProcessing            = QAction(icon_processing, "Выполнить обработку")

		self.MenuManual                        = QMenu("Ручная обработка")
		self.SubmenuManualObjectsType          = self.MenuManual.addMenu(icon_layers, "Тип объекта не выбран")
		self.SubmenuManualObjectsType.addAction(self.ActionManualObjectsTypeOperations)

		self.MenuManual.addSeparator()
		self.MenuManual.addAction(self.ActionManualProcessing)

	def InitMenuAuto(self):
		""" Инициализация меню Автоматическая обработка """
		icon_blocks     = QIcon("./L0/icons/blocks.svg")
		icon_layers     = QIcon("./L0/icons/layers.svg")

		self.ActionAutoRulesTypeReplaceDescription = QAction(icon_blocks, "Замена фрагментов описания")

		self.MenuAuto                              = QMenu("Автоматическая обработка")
		self.SubmenuAutoRulesType                  = self.MenuAuto.addMenu(icon_layers, "Тип правил не выбран")
		self.SubmenuAutoRulesType.addAction(self.ActionAutoRulesTypeReplaceDescription)

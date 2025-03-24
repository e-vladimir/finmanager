# ФОРМА ОБРАБОТКА ДАННЫХ: МЕХАНИКА УПРАВЛЕНИЯ
# 22 мар 2025

from PySide6.QtGui       import QCursor
from PySide6.QtWidgets   import QHeaderView

from L60_form_processing import C60_FormProcessing


class C70_FormProcessing(C60_FormProcessing):
	""" Форма Обработка данных: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка """
		self.setWindowTitle(f"Обработка данных - {self.Workspace.DmDyToString()}")

	# Меню ручной обработки данных
	def AdjustMenuManual(self):
		""" Настройка меню ручной обработки данных """
		pass

	def AdjustMenuManualText(self):
		""" Настройка названий элементов меню ручной обработки данных """
		self.SubmenuManualObjectsType.setTitle(self.processing_objects_type)

	def AdjustMenuManualEnable(self):
		""" Настройка доступности элементов меню ручной обработки данных """
		pass

	def ShowMenuManual(self):
		""" Отображение меню ручной обработки данных """
		self.MenuManual.exec_(QCursor().pos())

	# Вкладки режима обработки
	def AdjustTabsMainText(self):
		""" Настройка названий вкладок режима обработки """
		self.TabsMain.setTabText(0, f"Ручная обработка: {self.processing_objects_type}")

	# Дерево данных ручной обработки данных
	def AdjustTreeDataManualSize(self):
		""" Настройка размеров дерева данных ручной обработки данных """
		self.TreeDataManual.resizeColumnToContents(0)

	def AdjustTreeDataManualExpand(self):
		""" Настройка раскрытия дерева данных ручной обработки данных """
		self.TreeDataManual.expandAll()

	def AdjustTreeDataManualColor(self):
		""" Настройка цветовой схемы дерева данных ручной обработки данных """
		self.ModelDataManual.adjustGroupView(True,
		                                     True,
		                                     True)

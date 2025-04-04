# ФОРМА ЭКСПОРТ ДАННЫХ: МЕХАНИКА УПРАВЛЕНИЯ
# 01 апр 2025

from PySide6.QtGui   import QCursor

from L60_form_export import C60_FormExport


class C70_FormExport(C60_FormExport):
	""" Форма экспорт данных: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка """
		self.setWindowTitle(f"Экспорт данных - {self.Workspace.DmDyToString()}")

	# Дерево данных экспорта операций
	def AdjustTreeDataOperationsSize(self):
		""" Настройка размеров дерева данных ручной обработки """
		self.TreeDataOperations.resizeColumnToContents(0)

	def AdjustTreeDataOperationsExpand(self):
		""" Настройка раскрытия дерева данных ручной обработки """
		self.TreeDataOperations.expandAll()

	def AdjustTreeDataOperationsColor(self):
		""" Настройка цветовой схемы дерева данных ручной обработки """
		self.ModelDataOperations.adjustGroupView(True,
			                                     True,
			                                     True)

	# Меню экспорта операций
	def AdjustMenuOperations(self):
		""" Настройка меню ручной обработки """
		pass

	def AdjustMenuOperationsText(self):
		""" Настройка названий элементов меню ручной обработки """
		pass

	def AdjustMenuOperationsEnable(self):
		""" Настройка доступности элементов меню ручной обработки """
		pass

	def ShowMenuOperations(self):
		""" Отображение меню ручной обработки """
		self.MenuOperations.exec_(QCursor().pos())

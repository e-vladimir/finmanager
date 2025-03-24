# ФОРМА ОБРАБОТКА ДАННЫХ: МЕХАНИКА УПРАВЛЕНИЯ
# 22 мар 2025

from PySide6.QtGui       import QCursor

from L60_form_processing import C60_FormProcessing


class C70_FormProcessing(C60_FormProcessing):
	""" Форма Обработка данных: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка """
		match self.TabsMain.currentIndex():
			case 0: self.setWindowTitle(f"Ручная обработка: {self.processing_objects_type} - {self.Workspace.DmDyToString()}")
			case _: self.setWindowTitle(f"Обработка данных - {self.Workspace.DmDyToString()}")

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

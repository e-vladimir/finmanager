# ФОРМА ОБРАБОТКА ДАННЫХ: МЕХАНИКА УПРАВЛЕНИЯ
# 22 мар 2025

from PySide6.QtGui       import QCursor

from L00_form_processing import OBJECTS_TYPE
from L00_rules           import RULES
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
		self.SubmenuManualObjectsType.setTitle("Объект не выбран" if self._processing_object_type == OBJECTS_TYPE.NONE else self._processing_object_type)

	def AdjustMenuManualEnable(self):
		""" Настройка доступности элементов меню ручной обработки данных """
		pass

	def ShowMenuManual(self):
		""" Отображение меню ручной обработки данных """
		self.MenuManual.exec_(QCursor().pos())

	# Меню автоматической обработки данных
	def AdjustMenuAuto(self):
		""" Настройка меню автоматической обработки данных """
		pass

	def AdjustMenuAutoText(self):
		""" Настройка названий элементов меню ручной обработки данных """
		self.SubmenuAutoRulesType.setTitle("Тип правил не выбран" if self._processing_rules_type == RULES.NONE else self._processing_rules_type)

	def AdjustMenuAutoEnable(self):
		""" Настройка доступности элементов меню автоматической обработки данных """
		pass

	def ShowMenuAuto(self):
		""" Отображение меню автоматической обработки данных """
		self.MenuAuto.exec_(QCursor().pos())

	# Вкладки режима обработки
	def AdjustTabsMainText(self):
		""" Настройка названий вкладок режима обработки """
		self.TabsMain.setTabText(0, f"Ручная обработка: {self.processing_objects_type}")

		tab_name : str = "Автоматическая обработка"
		if not self.processing_rules_type == RULES.NONE: tab_name += f": {self.processing_rules_type}"

		self.TabsMain.setTabText(1, tab_name)

	def SwitchTabsMainToManual(self):
		""" Переключение основной вкладки на Ручную обработку  """
		self.TabsMain.setCurrentIndex(0)

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

# ФОРМА ОБРАБОТКА ДАННЫХ: МЕХАНИКА УПРАВЛЕНИЯ
# 22 мар 2025

from PySide6.QtCore      import Qt
from PySide6.QtGui       import QCursor
from PySide6.QtWidgets   import QHeaderView

from L00_form_processing import OBJECTS_TYPE
from L00_rules           import RULES
from L60_form_processing import C60_FormProcessing


class C70_FormProcessing(C60_FormProcessing):
	""" Форма Обработка данных: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка """
		self.setWindowTitle(f"Обработка данных - {self.Workspace.DmDyToString()}")

	# Меню ручной обработки
	def AdjustMenuManual(self):
		""" Настройка меню ручной обработки """
		pass

	def AdjustMenuManualText(self):
		""" Настройка названий элементов меню ручной обработки """
		self.SubmenuManualObjectsType.setTitle("Объект не выбран" if self._processing_object_type == OBJECTS_TYPE.NONE else self._processing_object_type)

	def AdjustMenuManualEnable(self):
		""" Настройка доступности элементов меню ручной обработки """
		pass

	def ShowMenuManual(self):
		""" Отображение меню ручной обработки """
		self.MenuManual.exec_(QCursor().pos())

	# Меню автоматической обработки
	def AdjustMenuAuto(self):
		""" Настройка меню автоматической обработки """
		self.MenuAuto.clear()

		self.MenuAuto.addMenu(self.SubmenuAutoRulesType)
		self.MenuAuto.addSeparator()

		if self.processing_rules_type == RULES.NONE: return

		if self.processing_ido:
			self.MenuAuto.addAction(self.ActionAutoEditRuleInput)
			self.MenuAuto.addAction(self.ActionAutoEditRuleBlock)
			self.MenuAuto.addAction(self.ActionAutoEditRuleOutput)
			self.MenuAuto.addSeparator()
			self.MenuAuto.addAction(self.ActionAutoDeleteRule)
			self.MenuAuto.addSeparator()

		self.MenuAuto.addAction(self.ActionAutoCreateRule)
		self.MenuAuto.addSeparator()

		self.MenuAuto.addMenu(self.SubmenuAutoRules)

		if self.processing_ido:
			self.MenuAuto.addMenu(self.SubmenuAutoRule)

	def AdjustMenuAutoText(self):
		""" Настройка названий элементов меню ручной обработки """
		self.SubmenuAutoRulesType.setTitle("Тип правил не выбран" if self._processing_rules_type == RULES.NONE else self._processing_rules_type)

		match self.processing_rules_type:
			case RULES.REPLACE_DESCRIPTION:
				self.ActionAutoEditRuleInput.setText("Редактировать поиск фрагмента")
				self.ActionAutoEditRuleBlock.setText("Редактировать условие пропуска")
				self.ActionAutoEditRuleOutput.setText("Редактировать замену на фрагмент")

			case _                        :
				self.ActionAutoEditRuleInput.setText("Редактировать input")
				self.ActionAutoEditRuleBlock.setText("Редактировать block")
				self.ActionAutoEditRuleOutput.setText("Редактировать output")

	def AdjustMenuAutoEnable(self):
		""" Настройка доступности элементов меню автоматической обработки """
		pass

	def ShowMenuAuto(self):
		""" Отображение меню автоматической обработки """
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

	# Дерево данных ручной обработки
	def AdjustTreeDataManualSize(self):
		""" Настройка размеров дерева данных ручной обработки """
		self.TreeDataManual.resizeColumnToContents(0)

	def AdjustTreeDataManualExpand(self):
		""" Настройка раскрытия дерева данных ручной обработки """
		self.TreeDataManual.expandAll()

	def AdjustTreeDataManualColor(self):
		""" Настройка цветовой схемы дерева данных ручной обработки """
		self.ModelDataManual.adjustGroupView(True,
		                                     True,
		                                     True)

	# Таблица данных автоматической обработки
	def AdjustTableDataAutoSize(self):
		""" Настройка размеров таблицы данных автоматической обработки """
		for idx_col in range(self.ModelDataAuto.columnCount()):
			self.TableDataAuto.horizontalHeader().setSectionResizeMode(idx_col, QHeaderView.ResizeMode.Stretch)

	def AdjustTableDataAutoSort(self):
		""" Настройка сортировки таблицы данных автоматической обработки """
		match self.processing_rules_type:
			case RULES.REPLACE_DESCRIPTION: self.TableDataAuto.sortByColumn(2, Qt.SortOrder.AscendingOrder)

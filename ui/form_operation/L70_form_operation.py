# ФОРМА ФИНАНСОВАЯ ОПЕРАЦИЯ: МЕХАНИКА УПРАВЛЕНИЯ

from G11_convertor_data import AmountToString

from L60_form_operation import C60_FormOperation


class C70_FormOperation(C60_FormOperation):
	""" Форма Финансовая операция: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка формы """
		amount   : str = AmountToString(self.operation.Amount())
		dd_dm_dy : str = self.operation.DdDmDyToString()

		self.setWindowTitle(f"{amount} от {dd_dm_dy}")

	# Дерево данных
	def AdjustTreeData_Size(self):
		""" Настройка дерева данных: Размеры """
		self.tree_data.setColumnWidth(0, 150)

	def AdjustTreeData_Color(self):
		""" Настройка дерева данных: Цвета """
		self.model_data.adjustGroupView(True, True, True)

	def AdjustTreeData_Expand(self):
		""" Настройка дерева данных: Раскрытие """
		self.tree_data.expandAll()

# ФОРМА ФИНАНСОВАЯ ОПЕРАЦИЯ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_operation import C80_FormOperation


class C90_FormOperation(C80_FormOperation):
	""" Форма Финансовая операция: Логика управления """

	# Форма
	def on_Open(self):
		""" Открытие формы """
		self.ReadOperationFromWorkspace()

		self.InitModel()
		self.LoadOperation()

		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Color()
		self.AdjustTreeData_Size()

		self.ShowTitle()

# ФОРМА УПРАВЛЕНИЕ АВТОЗАМЕНОЙ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_control_autoreplace import C80_FormControlAutoreplace


class C90_FormControlAutoreplace(C80_FormControlAutoreplace):
	""" Форма Управление автозаменой: Логика управления """

	def on_Open(self):
		""" Открытие формы """
		self.ShowTitle()

		self.InitModelData()

		self.ShowRules()

		self.AdjustTableData_Size()
		self.AdjustTableData_Color()

	def on_Show(self):
		""" Отображение формы """
		self.AdjustTableData_Size()
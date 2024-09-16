# ФОРМА ФИНСТАТИСТИКА: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_finstatistics import C80_FormFinstatistics


class C90_FormFinstatistics(C80_FormFinstatistics):
	""" Форма Финстатистика: Логика управления """

	def on_Show(self):
		""" Отображение формы """
		self.ShowTitle()

		self.InitModelData()
		self.LoadFinstatisticsByFinstruct()
		self.LoadFinstatisticsByLabels()

		self.AdjustTableData_Span()
		self.AdjustTableData_Size()
		self.AdjustTableData_Colors()
		self.AdjustTableData_Align()

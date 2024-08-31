# ФОРМА ЗАПИСЬ ФИНДЕЙСТВИЙ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_finactions_record import C80_FormFinactionsRecord


class C90_FormFinactionsRecord(C80_FormFinactionsRecord):
	""" Форма Запись финдействий: Логика управления """

	def on_Open(self):
		""" Открытие формы """
		self.ShowTitle()

		self.InitModel()

		self.AdjustTableData_Font()
		self.AdjustTableData_Alignment()
		self.AdjustTableData_Size()
		self.AdjustTableData_Color()

		self.LoadFinactionsRecord()

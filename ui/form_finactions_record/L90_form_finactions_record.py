# ФОРМА ЗАПИСЬ ФИНДЕЙСТВИЙ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_finactions_record import C80_FormFinactionsRecord


class C90_FormFinactionsRecord(C80_FormFinactionsRecord):
	""" Форма Запись финдействий: Логика управления """

	def on_Open(self):
		""" Открытие формы """
		self.InitModelFinstruct()

		self.LoadFinstruct()
		self.AdjustTreeDataColors()
		self.AdjustTreeDataExpand()

		self.FillCbboxDy()
		self.FillCbboxDm()

		self.ReadFinactionsRecordIdo()

		self.ShowTitle()

		self.ShowDy()
		self.ShowDm()
		self.ShowDd()

		self.ShowAmount()

		self.ShowSrcNote()
		self.ShowSrcAmount()

		self.ShowNote()
		self.ShowFinstruct()
		self.ShowLabels()

	def on_Close(self):
		self.SaveFinactionsRecord()
		self.SendFinactionsRecordIdo()

		self.application.form_finactions.UpdateDataPartial()

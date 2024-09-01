# ФОРМА ФИНДЕЙСТВИЯ: ЛОГИКА ДАННЫХ

from G10_math_linear     import CalcBetween

from L70_form_finactions import C70_FormFinactions


class C80_FormFinactions(C70_FormFinactions):
	""" Форма Финдействия: Логика данных """

	# Финдействия
	def LoadFinactions(self):
		""" Загрузка финдействий """
		dy, dm = self.workspace.DyDm()

		for self._processing_dd in self.finactions.DdsInDyDm(dy, dm):
			self.LoadDd()

			for self._processing_ido in self.finactions.IdosInDyDmDd(dy, dm, self._processing_dd): self.LoadFinactionsRecord()

	# Запись финдействий
	def CreateRecordFinactions(self):
		""" Создание записи финдействий """
		dy, dm = self.workspace.DyDm()
		dd     = CalcBetween(1, self._processing_dd, 31)
		ido    = self.finactions.CreateRecord(dy, dm, dd)

		self._processing_dd  = dd
		self._processing_ido = ido

	def OpenRecordFinactions(self):
		""" Открытие записи финдействий """
		self.workspace.IdoFinactionsRecord(self._processing_ido)

		self.application.form_finactions_record.Open()

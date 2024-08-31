# ФОРМА ФИНДЕЙСТВИЯ: ЛОГИКА ДАННЫХ

from G10_math_linear     import CalcBetween

from L70_form_finactions import C70_FormFinactions


class C80_FormFinactions(C70_FormFinactions):
	""" Форма Финдействия: Логика данных """

	# Финдействия
	def LoadFinactions(self):
		""" Загрузка финдействий """
		dy, dm = self.workspace.DyDm()

		for self._dd_processing in self.finactions.DdsInDyDm(dy, dm):
			self.LoadDd()

			for self._ido_processing in self.finactions.IdosInDyDmDd(dy, dm, self._dd_processing): self.LoadRecordFinactions()

	# Запись финдействий
	def CreateRecord(self):
		""" Создание записи финдействий """
		dy, dm = self.workspace.DyDm()
		dd     = CalcBetween(1, self._dd_processing, 31)
		ido    = self.finactions.CreateRecord(dy, dm, dd)

		self._dd_processing  = dd
		self._ido_processing = ido

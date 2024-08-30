# ФОРМА ФИНДЕЙСТВИЯ: ЛОГИКА ДАННЫХ

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

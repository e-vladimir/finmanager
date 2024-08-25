# ФОРМА ФИНСТРУКТУРА: ЛОГИКА ДАННЫХ

from L70_form_finstruct import C70_FormFinstruct


class C80_FormFinstruct(C70_FormFinstruct):
	""" Форма Финструктура: Логика данных """

	def LoadFinstruct(self):
		""" Загрузка финструктуры """
		dy, dm = self.workspace.DyDm()

		for self._name_processing in self.finstruct.Groups(dy, dm): self.LoadFinstructGroup()
		for self._ido_processing  in self.finstruct.Idos(dy, dm)  : self.LoadFinstructRecord()

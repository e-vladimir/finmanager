# ФОРМА ОСНОВНАЯ: ЛОГИКА ДАННЫХ

from L70_form_main import C70_FormMain


class C80_FormMain(C70_FormMain):
	""" Форма основная: Логика данных """

	def SetDyDm(self):
		""" Установка года и месяца """
		self.workspace.Dy(self._processing_dy)
		self.workspace.Dm(self._processing_dm)

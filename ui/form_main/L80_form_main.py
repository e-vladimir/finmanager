# ФОРМА ОСНОВНАЯ: ЛОГИКА ДАННЫХ

from L70_form_main import C70_FormMain


class C80_FormMain(C70_FormMain):
	""" Форма основная: Логика данных """

	def SetDyDm(self):
		""" Установка года и месяца """
		self.workspace.Dy(self._dy_processing)
		self.workspace.Dm(self._dm_processing)

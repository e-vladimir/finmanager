# ФОРМА ФИНДЕЙСТВИЯ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_finactions import C80_FormFinactions


class C90_FormFinactions(C80_FormFinactions):
	""" Форма Финдействия: Логика управления """

	def on_Show(self):
		""" Отображение формы """
		self.ShowTitle()

		self.InitModel()
		self.LoadFinactions()

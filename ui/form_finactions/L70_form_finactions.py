# ФОРМА ФИНДЕЙСТВИЯ: МЕХАНИКА УПРАВЛЕНИЯ

from L60_form_finactions import C60_FormFinactions


class C70_FormFinactions(C60_FormFinactions):
	""" Форма Финдействия: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка окна """
		self.setWindowTitle(f"Финдействия - {self.workspace.DmDyToString()}")

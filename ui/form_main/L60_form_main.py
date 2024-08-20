# ФОРМА ОСНОВНАЯ: МЕХАНИКА ДАННЫХ

from L00_months    import MONTHS_SHORT
from L50_form_main import C50_FormMain


class C60_FormMain(C50_FormMain):
	""" Форма основная: Механика данных """

	def ReadDyProcessingFromCbboxDy(self):
		""" Считывание года из панели финпериода """
		self._dy_processing = int(self.cbbox_dy.currentText())

	def ReadDmProcessingFromCbboxDm(self):
		""" Считывание месяца из панели финпериода """
		self._dm_processing = MONTHS_SHORT.index(self.cbbox_dm.currentText())

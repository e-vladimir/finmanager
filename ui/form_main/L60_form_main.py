# ФОРМА ОСНОВНАЯ: МЕХАНИКА ДАННЫХ

from L00_months    import MONTHS_SHORT
from L50_form_main import C50_FormMain


class C60_FormMain(C50_FormMain):
	""" Форма основная: Механика данных """

	def ReadProcessingDyFromCbboxDy(self):
		""" Считывание года из панели финпериода """
		self._processing_dy = int(self.cbbox_dy.currentText())

	def ReadProcessingDmFromCbboxDm(self):
		""" Считывание месяца из панели финпериода """
		self._processing_dm = MONTHS_SHORT.index(self.cbbox_dm.currentText())

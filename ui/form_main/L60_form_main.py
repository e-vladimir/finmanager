# ФОРМА ОСНОВНАЯ: МЕХАНИКА ДАННЫХ

from L00_months    import MONTHS_SHORT
from L00_reports   import REPORTS
from L50_form_main import C50_FormMain


class C60_FormMain(C50_FormMain):
	""" Форма основная: Механика данных """

	def ReadProcessingDyFromCbboxDy(self):
		""" Считывание года из панели финпериода """
		self._processing_dy = int(self.cbbox_dy.currentText())

	def ReadProcessingDmFromCbboxDm(self):
		""" Считывание месяца из панели финпериода """
		self._processing_dm = MONTHS_SHORT.index(self.cbbox_dm.currentText())

	def ReadProcessingReport(self):
		""" Считывание типа отчёта """
		self._processing_report = None

		value : str = self.cbbox_reports.currentText()
		if value not in REPORTS: return

		self._processing_report = REPORTS(value)

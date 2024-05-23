# ФОРМА ОСНОВНАЯ: ЛОГИКА ДАННЫХ

from L70_form_main import C70_FormMain


class C80_FormMain(C70_FormMain):
	""" Форма основная: Логика данных """

	# Генерация отчётности
	def GenerateSummaryReport(self):
		""" Сводный отчёт за месяц """
		self.report.GenerateSummaryReport()
		self.report.SaveReportToPDF()
		self.report.OpenReport()

	def GenerateHistoryFinstateReport(self):
		""" Хронология финсостояния """
		self.report.GenerateHistoryFinstateReport()

		self.report.SaveReportToPDF()
		self.report.OpenReport()

# ФОРМА ОСНОВНАЯ: ЛОГИКА ДАННЫХ

from L00_reports   import REPORTS
from L70_form_main import C70_FormMain


class C80_FormMain(C70_FormMain):
	""" Форма основная: Логика данных """

	# Параметры рабочего пространства
	def SetDyDm(self):
		""" Установка года и месяца """
		self.workspace.Dy(self._processing_dy)
		self.workspace.Dm(self._processing_dm)

	# Генерация отчётов
	def GenerateReportHistoryFinstate(self):
		""" Генерация отчёта хронологии финсостояния """
		self.finreports.DirectoryPath(self.application._path_reports)
		self.finreports.ReportType(REPORTS.HISTORY_FINSTATE)

		self.finreports.GenerateReportHistoryFinstate()

	def GenerateReportSummaryMonth(self):
		""" Генерация сводного отчёта за месяц """
		self.finreports.DirectoryPath(self.application._path_reports)
		self.finreports.ReportType(REPORTS.SUMMARY_MONTH)
		self.finreports.Dy(self.workspace.Dy())
		self.finreports.Dm(self.workspace.Dm())

		self.finreports.GenerateReportSummaryMonth()

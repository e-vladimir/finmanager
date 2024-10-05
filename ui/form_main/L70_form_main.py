# ФОРМА ОСНОВНАЯ: МЕХАНИКА УПРАВЛЕНИЯ

from L00_months    import MONTHS_SHORT
from L00_reports   import REPORTS
from L60_form_main import C60_FormMain


class C70_FormMain(C60_FormMain):
	""" Форма основная: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка окна """
		self.setWindowTitle(f"Финменеджер 19.1 - {self.workspace.DmDyToString()}")

	# Панель финпериода
	def FillCbboxDy(self):
		""" Заполнение списка годов """
		self.cbbox_dy.clear()
		self.cbbox_dy.addItems(list(map(str, self.workspace.AvailableDys())))

	def FillCbboxDm(self):
		""" Заполнение списка месяцев """
		self.cbbox_dm.clear()
		self.cbbox_dm.addItems(MONTHS_SHORT[1:])

	def ShowDy(self):
		""" Отображение года """
		self.cbbox_dy.setCurrentText(f"{self.workspace.Dy()}")

	def ShowDm(self):
		""" Отображение месяца """
		self.cbbox_dm.setCurrentText(f"{MONTHS_SHORT[self.workspace.Dm()]}")

	# Панель отчётности
	def FillCbbReports(self):
		""" Заполнение списка доступной отчётности """
		self.cbbox_reports.clear()

		self.cbbox_reports.addItem(REPORTS.HISTORY_FINSTATE)
		self.cbbox_reports.addItem(REPORTS.SUMMARY_MONTH)

	def ResetCbbReport(self):
		""" Сброс списка доступных отчётов """
		self.cbbox_reports.setCurrentIndex(-1)

	# Отчётность
	def ProcessingRequestReport(self):
		""" Обработка запроса отчёта """
		match self._processing_report:
			case REPORTS.HISTORY_FINSTATE: self.on_RequestReportHistoryFinstate()
			case REPORTS.SUMMARY_MONTH   : self.on_RequestReportSummaryMonth()

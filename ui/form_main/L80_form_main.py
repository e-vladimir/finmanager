# ФОРМА ОСНОВНАЯ: ЛОГИКА ДАННЫХ

from L00_months    import MONTHS
from L00_reports   import REPORTS
from L20_PySide6   import RequestItem, RequestText
from L70_form_main import C70_FormMain


class C80_FormMain(C70_FormMain):
	""" Форма Основная: Логика данных """

	# Рабочий период
	def SetDyDm(self):
		""" Установка рабочего периода """
		dydm_raw : str | None = RequestText("Рабочий период", "Формат: МЕС ГОД", self.workspace.DmDyToString())
		if dydm_raw is None: return

		try   :
			dm_raw, dy_raw = dydm_raw.lower().split(' ')

			dy : int       = int(dy_raw)
			dm : MONTHS    = MONTHS.FindByNameS(dm_raw)
		except: return

		self.workspace.DyDm(dy, dm.code)

	# Отчётность за месяц
	def GenerateReportDm(self):
		""" Выбор и генерация отчёта за месяц """
		reports         : list[str]  = []
		reports.append(REPORTS.DM)

		selected_report : str | None = RequestItem("Генерация отчётности", "Доступные отчёты за месяц", reports)
		if selected_report is None: return

		match REPORTS(selected_report):
			case REPORTS.DM:
				dy, dm = self.workspace.DyDm()
				self.report.GenerateReportDm(dy, dm)

	# Отчётность сводная
	def GenerateReportSummary(self):
		""" Выбор и генерация сводного отчёта """
		pass

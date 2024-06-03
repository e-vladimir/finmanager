# ГЕНЕТАОР ОТЧЁТОВ: ЛОГИКА ДАННЫХ

import subprocess

from   os             import mkdir
from   pathlib        import Path

from   L11_datetime   import *
from   L70_report     import C70_Report


class C80_Report(C70_Report):
	""" Генератор отчётов: Логика данных """

	# Шаблоны
	def LoadPatterns(self):
		""" Загрузка шаблонов отчёта """
		path_pattern = Path("./L0/pattern_report.html")

		with open(path_pattern, "r") as file_pattern: self._report_patterns = file_pattern.read().splitlines()

	# Генерация отчётов
	def GenerateSummaryReport(self):
		""" Генерация сводного отчёта """
		self.ReportType("Сводный отчёт")
		self.ReportDy(self.workspace.Dy())
		self.ReportDm(self.workspace.Dm())

		self.InitReport()
		self.AppendHeader()
		self.AppendSeparator()

		self.AppendFinstate()
		self.AppendSeparator()

		self.AppendFinstatistic()
		self.AppendSeparator()

		self.AppendFindata()
		self.AppendSeparator()

		self.CloseReport()

	def GenerateHistoryFinstateReport(self):
		""" Генерация хронологии финсостояния """
		self.ReportType("Хронология финсостояния")
		self.ReportDy(CurrentDy())
		self.ReportDm(CurrentDm())

		self.InitReport()
		self.AppendHeader()
		self.AppendSeparator()

		self.CalcNamesProcessingFromFinstruct()
		for self._name_processing in self._names_processing:
			self.AppendRecordFinstructHistoryRemains()
			self.AppendSeparator()

		self.CloseReport()

	# Работа с файлами отчётов
	def GenerateReportFilename(self):
		""" Генерация имени файла """
		dir_root    : Path = Path("./").absolute()
		dir_reports : Path = dir_root.joinpath("reports")
		file_report : Path = dir_reports.joinpath(f"{self.ReportDy()}-{self.ReportDm():02d} {self.ReportType()}.pdf")

		self._path_report  = file_report

		if not dir_reports.exists(): mkdir(dir_reports)

	def SaveReportToPDF(self):
		""" Сохранение отчёта в PDF формат """
		self.GenerateReportFilename()

		with open("out.html", "w") as file:
			file.write('\n'.join(self._report_data))

		# pdfkit.from_string('\n'.join(self._report_data), f"{self._path_report}")

	def OpenReport(self):
		""" Открытие файла отчёта """
		subprocess.Popen([f"evince '{self._path_report}'"], shell=True)

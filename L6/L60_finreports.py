# ФИНОТЧЁТНОСТЬ: МЕХАНИКА ДАННЫХ

from enum           import Enum
from pathlib        import Path

from L00_reports    import REPORTS
from L50_finreports import C50_Finreports


class C60_Finreports(C50_Finreports):
	""" Финотчётность: Механика данных """

	# Параметры
	def ReportType(self, data: Enum = None) -> Enum:
		""" Тип отчёта """
		if data is None: return self._report_type
		else           :        self._report_type = data

	def DirectoryPath(self, directory: Path = None) -> Path:
		""" Директория отчётов """
		if directory is None: return self._directory_path
		else                :        self._directory_path = directory

	def Dy(self, year: int = None) -> int:
		""" Год """
		if year is None: return self._dy
		else           :        self._dy = year

	def Dm(self, month: int = None) -> int:
		""" Месяц """
		if month is None: return self._dm
		else            :        self._dm = month

	def CalcFilename(self):
		""" Вычисление имени файла """
		match self._report_type:
			case REPORTS.HISTORY_FINSTATE: self._file_name = "Хронология финсостояния"
			case REPORTS.SUMMARY_MONTH   : self._file_name = f"{self._dy}.{self._dm:02d} - Сводный отчёт"

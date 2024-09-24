# ФИНОТЧЁТНОСТЬ: ЛОГИКА ДАННЫХ

from itertools          import product
from pathlib            import Path

from G11_convertor_data import AmountToString
from L00_months import MONTHS_SHORT

from L30_reports_fpdf   import C30_ProcessorReportsFpdf2
from L70_finreports     import C70_Finreports
from L90_finactions import C90_FinactionsRecord
from L90_finstructs     import C90_FinstructRecord


class C80_Finreports(C70_Finreports):
	""" Финотчётность: Логика данных """

	# Генератор отчётов
	def GenerateReportHistoryFinstate(self):
		""" Генерация отчёта: Хронология финсостояния """
		report           = C30_ProcessorReportsFpdf2()
		report._header_l = "Хронология финсостояния".upper()
		report._header_r = ""
		report._header_b = ""

		report.LoadFonts(Path("./L0/fonts/"))

		dys : list[int]  = self.finactions.AvailableDys()

		for finstruct_name in self.finstruct.Names():
			data : list[list[str]] = []

			report.AppendPage()
			report.AppendH1(finstruct_name)

			header : list[str] = ["Месяц/Год", "Было", "Стало", "Изменение", "Поступило", "Выбыло"]
			sizes  : list[int] = [25, 15, 15, 15, 15, 15]
			aligns : list[str] = [        "L",         "R",         "R",         "R",         "R",      "R"]

			for dy, dm in product(dys, range(1, 13)):
				finstruct_record = C90_FinstructRecord()
				if not finstruct_record.SwitchByName(dy, dm, finstruct_name): continue

				amount_income  : float = finstruct_record.AmountIncome()
				amount_outcome : float = finstruct_record.AmountOutcome()
				balance_start  : float = finstruct_record.BalanceStart()
				balance_delta  : float = amount_income + amount_outcome
				balance_end    : float = balance_start + balance_delta

				data.append([f"{MONTHS_SHORT[dm]} {dy}",
				             f"{AmountToString(balance_start)}",
				             f"{AmountToString(balance_end)}",
				             f"{AmountToString(balance_delta, flag_sign=True)}",
				             f"{AmountToString(amount_income, flag_sign=True)}",
				             f"{AmountToString(amount_outcome)}",
				             ])

			report.AppendTable(header, data, sizes, aligns)

		report.ExportReportToPdf(Path("./reports/Хронология финсостояния.pdf"))

	def GenerateReportSummaryMonth(self):
		""" Генерация отчёта: Сводный отчёт за месяц """
		report                   = C30_ProcessorReportsFpdf2()
		report._header_l         = "СВОДНЫЙ ОТЧЁТ".upper()
		report._header_r         = f"{MONTHS_SHORT[self._dm]} {self._dy}".upper()
		report._header_b         = "за месяц"

		report.LoadFonts(Path("./L0/fonts/"))

		report.AppendPage()

		report.AppendH1("ОСТАТОК ПО СЧЕТАМ")
		data   : list[list[str]] = []
		header : list[str]       = ["Счёт", "Было", "Стало", "Изменение", "Поступило", "Выбыло"]
		sizes  : list[int]       = [25, 15, 15, 15, 15, 15]
		aligns : list[str]       = ["L", "R", "R", "R", "R", "R"]

		for finstruct_name in self.finstruct.NamesInDyDm(self._dy, self._dm):
			finstruct_record = C90_FinstructRecord()
			if not finstruct_record.SwitchByName(self._dy, self._dm, finstruct_name): continue

			amount_income  : float = finstruct_record.AmountIncome()
			amount_outcome : float = finstruct_record.AmountOutcome()
			balance_start  : float = finstruct_record.BalanceStart()
			balance_delta  : float = amount_income + amount_outcome
			balance_end    : float = balance_start + balance_delta

			data.append([f"{finstruct_name}",
			             f"{AmountToString(balance_start)}",
			             f"{AmountToString(balance_end)}",
			             f"{AmountToString(balance_delta, flag_sign=True)}",
			             f"{AmountToString(amount_income, flag_sign=True)}",
			             f"{AmountToString(amount_outcome)}"
			             ])

		report.AppendTable(header, data, sizes, aligns)

		report.AppendH1("СТАТИСТИКА ПО МЕТКАМ")
		data   : list[list[str]] = []
		header : list[str]       = ["Метка", "Поступило", "Выбыло"]
		sizes  : list[int]       = [70, 15, 15]
		aligns : list[str]       = ["L", "R", "R"]

		data_raw                 = self.finstatistics.CaptureStatistic(self._dy, self._dm)

		for label in sorted(data_raw.keys()):
			data.append([f"{label}",
			             f"{AmountToString(data_raw[label].income, flag_sign=True)}",
			             f"{AmountToString(data_raw[label].outcome, flag_sign=True)}",
			             ])

		report.AppendTable(header, data, sizes, aligns)

		report.AppendPage()

		report.AppendH1("ФИНДЕЙСТВИЯ")
		data   : list[list[str]] = []
		header : list[str]       = ["Дата", "Сумма", "Счёт", "Примечание"]
		sizes  : list[int]       = [15, 10, 30, 45]
		aligns : list[str]       = ["L", "R", "L", "L"]

		for finactions_ido in self.finactions.IdosInDyDmDd(self._dy, self._dm):
			finactions_record = C90_FinactionsRecord(finactions_ido)
			data.append([f"{finactions_record.DdDmDyToString()}",
			             f"{AmountToString(finactions_record.Amount(), flag_sign=True)}",
			             f"{'\n'.join(self.finstruct.IdosToNames(finactions_record.FinstructIdos()))}",
			             f"{finactions_record.Note()}",
			             ])

		report.AppendTable(header, data, sizes, aligns)

		report.ExportReportToPdf(Path(f"./reports/{self._dy:04d}.{self._dm:02d} - Сводный отчёт за месяц.pdf"))

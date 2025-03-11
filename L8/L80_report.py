# ГЕНЕРАТОР ОТЧЁТОВ: ЛОГИКА ДАННЫХ
# 10 мар 2025

from itertools          import product
from pathlib            import Path
from fpdf               import Align

from G11_convertor_data import AmountToString

from L30_reports_fpdf   import C30_ProcessorReportsFpdf2, MONTHS_SHORT
from L70_report         import C70_Report
from L90_account        import C90_Account


class C80_Report(C70_Report):
	""" Генератор отчётов: Логика данных """

	# Генерация отчётности
	def GenerateReportBalances(self) -> Path | None:
		""" Генерация отчёта по остаткам """
		dys      : list[int] = self.Accounts.AvailableDys()
		dms      : list[int] = list(range(1, 13))
		names    : list[str] = self.Accounts.Names()

		filepath : Path      = Path("./reports/Отчёт по остаткам.pdf")

		account              = C90_Account()

		try:
			report          = C30_ProcessorReportsFpdf2()
			report.LoadFonts(Path("./L0/fonts"))
			report.info_document.title = "Отчёт по остаткам"

			for name in names:
				report.NewPage()
				report.AppendH1(name)

				header : list = ["Месяц", "Остаток\nна начало месяца"]
				data   : list = []

				for dy, dm in product(dys, dms):
					if not account.SwitchByName(dy, dm, name): continue

					data.append([f"{MONTHS_SHORT[dm]} {dy:04d}",
					             AmountToString(account.initial_balance, flag_point=False, flag_sign=False)])


				report.AppendTable("", header, data, sizes=[100], aligns=[Align.L, Align.R])

			report.SaveToPdf(filepath)
			return filepath
		except Exception as err: print(err)

		return None

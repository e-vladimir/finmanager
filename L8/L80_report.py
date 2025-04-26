# ГЕНЕРАТОР ОТЧЁТОВ: ЛОГИКА ДАННЫХ
# 10 мар 2025

from itertools          import product
from pathlib            import Path
from fpdf               import Align

from G11_convertor_data import AmountToString

from L00_months         import MONTHS
from L00_operations import OPERATIONS
from L30_reports_fpdf   import C30_ProcessorReportsFpdf2, MONTHS_SHORT
from L70_report         import C70_Report
from L90_account        import C90_Account
from L90_operations     import C90_Operation


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
					             AmountToString(account.balance_initial, flag_point=False, flag_sign=False)])


				report.AppendTable("", header, data, sizes=[100], aligns=[Align.L, Align.R])

			report.SaveToPdf(filepath)
			return filepath
		except Exception as err: print(err)

		return None

	def GenerateReportDm(self, dy: int, dm: int):
		""" Генерация отчёта за месяц """
		generator_pdf                  = C30_ProcessorReportsFpdf2()
		generator_pdf.LoadFonts(Path("./L0/fonts"))

		generator_pdf.info_document.title    = f"Отчёт за месяц"
		generator_pdf.info_document.subtitle = f"{MONTHS(dm).name_short} {dy:04d}"

		generator_pdf.NewPage()

		generator_pdf.AppendH1(f"{MONTHS(dm).name_short} {dy:04d}")
		generator_pdf.AppendH2(f"Остатки по счетам")

		for account_group_name in self.Accounts.Groups(dy, dm):
			table_header : list[str]       = []
			table_header.append("Наименование счёта")
			table_header.append("Остаток\nначальный")
			table_header.append("Объём\nпоступлений")
			table_header.append("Объём\nсписаний")
			table_header.append("Изменение\nостатка")
			table_header.append("Остаток\nитоговый")

			table_data   : list[list[str]] = []
			for account_name in self.Accounts.Names(dy, dm, account_group_name):
				account = C90_Account()
				account.SwitchByName(dy, dm, account_name)

				balance_initial : int = account.balance_initial
				balance_final   : int = account.balance_summary
				balance_delta   : int = balance_final - balance_initial

				subdata : list[str] = []
				subdata.append(account_name)
				subdata.append(AmountToString( balance_initial,        flag_point=False, flag_sign=False))
				subdata.append(AmountToString(account.amount_income, flag_point=False, flag_sign=True))
				subdata.append(AmountToString(-account.amount_outcome, flag_point=False, flag_sign=True))
				subdata.append(AmountToString( balance_delta,          flag_point=False, flag_sign=True))
				subdata.append(AmountToString( balance_final,          flag_point=False, flag_sign=False))

				table_data.append(subdata)

			generator_pdf.AppendTable(description = account_group_name,
			                          header      = table_header,
			                          data        = table_data,
			                          sizes       = [60],
			                          aligns      = [Align.L, Align.R, Align.R, Align.R, Align.R, Align.R])

		generator_pdf.NewPage()
		generator_pdf.AppendH2(f"Реестр операций")

		operation                      = C90_Operation()

		table_header: list[str]        = []
		table_header.append("Дата")
		table_header.append("Сумма")
		table_header.append("Описание")

		flag_first  : bool             = True

		for account_ido in self.Accounts.Idos(dy, dm):
			table_data: list[list[str]] = []

			for dd in range(1, 32):
				for operation_ido in self.Operations.Idos(dy, dm, dd, account_ido, use_cache=True, type_operation=OPERATIONS.PHYSICAL):
					operation.Ido(operation_ido)

					subdata: list[str] = []
					subdata.append(operation.DdDmDyToString())
					subdata.append(AmountToString(operation.amount, flag_sign=True))
					subdata.append(operation.DestinationOrDescription())

					if not subdata: continue

					table_data.append(subdata)

			if not table_data: continue

			account = C90_Account(account_ido)
			if not flag_first: generator_pdf.NewPage()

			flag_first = False

			generator_pdf.AppendH3(f"{account.group}:  {account.name}")
			generator_pdf.AppendTable(description = "",
			                          header      = table_header,
			                          data        = table_data,
			                          sizes       = [25, 20],
			                          aligns      = [Align.R, Align.R])

		filepath     : Path            = Path(f"./reports/{dy:04d}-{dm:02d} - Отчёт за месяц ({MONTHS(dm).name_short}).pdf")
		generator_pdf.SaveToPdf(filepath)

		return filepath

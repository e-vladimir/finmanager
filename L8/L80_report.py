# ОТЧЁТНОСТЬ: ЛОГИКА ДАННЫХ

from pathlib            import Path

from fpdf               import Align

from G10_datetime       import CurrentDy
from G11_convertor_data import AmountToString

from L00_months         import MONTHS
from L30_reports_fpdf   import C30_ProcessorReportsFpdf2
from L70_report         import C70_Report
from L90_accounts       import C90_Account
from L90_operations     import C90_Operation


class C80_Report(C70_Report):
	""" Отчётность: Логика данных """

	# Генерация отчётов
	def GenerateReportDm(self, dy: int, dm: int):
		""" Генерация отчёта за месяц """
		generator_pdf  = C30_ProcessorReportsFpdf2()
		generator_pdf.LoadFonts(Path("./L0/fonts"))

		generator_pdf.info_document.title    = f"Отчёт за месяц"
		generator_pdf.info_document.subtitle = f"{MONTHS(dm).name_short} {dy:04d}"

		generator_pdf.NewPage()

		generator_pdf.AppendH1(f"{MONTHS(dm).name_short} {dy:04d}")
		generator_pdf.AppendH2(f"Остатки по счетам")

		for account_group_name in self.accounts.GroupsNamesInDyDm(dy, dm):
			table_header : list[str]       = []
			table_header.append("Наименование счёта")
			table_header.append("Объём\nпоступлений")
			table_header.append("Объём\nсписаний")
			table_header.append("Остаток\nначальный")
			table_header.append("Изменение\nостатка")
			table_header.append("Остаток\nитоговый")

			table_data   : list[list[str]] = []
			for account_name in self.accounts.AccountsNamesInDyDm(dy, dm, account_group_name):
				account = C90_Account()
				account.SwitchByNameInDyDm(dy, dm, account_name)

				balance_initial : int = account.BalanceInitial()
				balance_final   : int = account.BalanceFinal()
				balance_delta   : int = balance_final - balance_initial

				subdata : list[str] = []
				subdata.append(account_name)
				subdata.append(AmountToString( account.AmountIncome(),  flag_point=False, flag_sign=True))
				subdata.append(AmountToString(-account.AmountOutcome(), flag_point=False, flag_sign=True))
				subdata.append(AmountToString( balance_initial,         flag_point=False, flag_sign=False))
				subdata.append(AmountToString( balance_delta,           flag_point=False, flag_sign=True))
				subdata.append(AmountToString( balance_final,           flag_point=False, flag_sign=False))

				table_data.append(subdata)

			generator_pdf.AppendTable(description = account_group_name,
			                          header      = table_header,
			                          data        = table_data,
			                          sizes       = [60],
			                          aligns      = [Align.L, Align.R, Align.R, Align.R, Align.R, Align.R])

		generator_pdf.NewPage()
		generator_pdf.AppendH2(f"Статистика")

		statistic = self.statistics.CaptureDataInDm(dy, dm)

		table_header : list[str]       = []
		table_header.append("Метка статистики")
		table_header.append("Объём поступлений")
		table_header.append("Объём списаний")

		table_data   : list[list[str]] = []

		for statistic_item in statistic:
			subdata : list[str] = []
			subdata.append(statistic_item.caption)
			subdata.append(AmountToString(statistic_item.amount_income,  flag_sign=True))
			subdata.append(AmountToString(statistic_item.amount_outcome, flag_sign=True))

			table_data.append(subdata)

		table_data.sort()

		generator_pdf.AppendTable(description = "Статистика по меткам",
		                          header      = table_header,
		                          data        = table_data,
		                          sizes       = [100],
		                          aligns      = [Align.L, Align.R, Align.R])

		generator_pdf.NewPage()
		generator_pdf.AppendH2(f"Реестр операций")

		table_header : list[str]      = []
		table_header.append("Дата")
		table_header.append("Сумма")
		table_header.append("Счёт")
		table_header.append("Назначение")

		table_data   : list[list[str]] = []
		for dd in range(1, 32):
			for operation_ido in self.operations.OperationsIdosInDyDmDd(dy, dm, dd):
				operation = C90_Operation(operation_ido)

				subdata : list[str] = []
				subdata.append(operation.DdDmDyToString())
				subdata.append(AmountToString(operation.Amount(), flag_sign = True))
				subdata.append('\n'.join(self.accounts.IdosToNames(operation.AccountsIdos())))
				subdata.append(operation.Description())

				table_data.append(subdata)

		generator_pdf.AppendTable(description = "",
		                          header      = table_header,
		                          data        = table_data,
		                          sizes       = [25, 20, 50],
		                          aligns      = [Align.R, Align.R, Align.L])

		filename: str = f"{dy:04d}-{dm:02d} - Отчёт за месяц ({MONTHS(dm).name_short}).pdf"
		generator_pdf.SaveToPdf(Path(f"./reports/{filename}"))

	def GenerateReportBalanceForAllDm(self):
		""" Генерация отчёта по остаткам за все периоды """
		account_names : list[str] = self.accounts.AccountsNames()
		if not account_names: return

		dy_start : int = self.operations.DyStart()
		if not dy_start     : return

		generator_pdf  = C30_ProcessorReportsFpdf2()
		generator_pdf.LoadFonts(Path("./L0/fonts"))

		generator_pdf.info_document.title    = f"Отчёт по остаткам за все периоды"

		for idx_account, account_name in enumerate(account_names):
			table_header : list[str]       = []
			table_header.append("Месяц")
			table_header.append("Остаток начальный")

			table_data   : list[list[str]] = []

			for dy in reversed(range(dy_start, CurrentDy())):
				for dm in reversed(range(1, 13)):
					account = C90_Account()
					if not account.SwitchByNameInDyDm(dy, dm, account_name): continue

					subdata : list[str] = []
					subdata.append(f"{MONTHS(dm).name_short} {dy}")
					subdata.append(AmountToString(account.BalanceInitial()))

					table_data.append(subdata)

			if not table_data: continue

			generator_pdf.NewPage()
			generator_pdf.AppendH2(f"{account_name}")
			generator_pdf.AppendTable(description = "",
			                          header      = table_header,
			                          data        = table_data,
			                          sizes       = [100],
			                          aligns      = [Align.L, Align.R])

		filename: str = f"Отчёт по остаткам (Все периоды).pdf"
		generator_pdf.SaveToPdf(Path(f"./reports/{filename}"))

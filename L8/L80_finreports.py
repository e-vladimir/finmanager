# ФИНОТЧЁТНОСТЬ: ЛОГИКА ДАННЫХ

from itertools          import product

from G11_convertor_data import AmountToString

from L00_months         import MONTHS_SHORT
from L70_finreports     import C70_Finreports
from L90_finstructs     import C90_FinstructRecord


class C80_Finreports(C70_Finreports):
	""" Финотчётность: Логика данных """

	# Генератор отчётов
	def GenerateReportHistoryFinstate(self):
		""" Генерация отчёта: Хронология финсостояния """
		self.CreateDocument()

		dys  : list[int]       = self.finactions.AvailableDys()
		for finstruct_name in self.finstruct.Names():
			data    : list[list[str]] = []

			subdata : list[str]       = []
			subdata.append("Период")
			subdata.append("Остаток-Н")
			subdata.append("Остаток-К")
			subdata.append("Изменение")
			subdata.append("Поступило")
			subdata.append("Выбыло")

			data.append(subdata)

			for dy, dm in product(dys, range(1, 13)):
				if     finstruct_name not in self.finstruct.NamesInDyDm(dy, dm): continue

				finstruct_record = C90_FinstructRecord()
				if not finstruct_record.SwitchByName(dy, dm, finstruct_name)   : continue

				balance_start  : float = finstruct_record.BalanceStart()
				balance_calc   : float = finstruct_record.BalanceCalc()
				amount_income  : float = finstruct_record.AmountIncome()
				amount_outcome : float = finstruct_record.AmountOutcome()
				balance_delta  : float = amount_income + amount_outcome

				subdata        : list[str] = []
				subdata.append(f"{MONTHS_SHORT[dm]} {dy}")
				subdata.append(f"{AmountToString(balance_start)}")
				subdata.append(f"{AmountToString(balance_calc)}")
				subdata.append(f"{AmountToString(balance_delta)}")
				subdata.append(f"{AmountToString(amount_income)}")
				subdata.append(f"{AmountToString(amount_outcome)}")

				data.append(subdata)

			self.CreatePage()
			self.SetupLayoutSingle()
			self.AppendReportHeader()
			self.AppendFinstructHistory(finstruct_name, data)

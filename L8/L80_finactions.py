# ФИНДЕЙСТВИЯ: ЛОГИКА ДАННЫХ

from G30_cactus_datafilters import C30_FilterLinear1D

from L00_containers         import CONTAINER_LOCAL
from L00_months             import MONTHS_SHORT
from L70_finactions         import C70_FinactionsRecord, C70_Finactions


class C80_FinactionsRecord(C70_FinactionsRecord):
	""" Запись финдействий: Логика данных """

	# Генерация данных
	def DdDmDyToString(self) -> str:
		""" Число Месяц Год в строку """
		return f"{self.Dd():02d} {MONTHS_SHORT[self.Dm()]} {self.Dy()}"

	# Действия
	def SplitAmount(self, amount: int) -> str:
		""" Разделение записи финдействий """
		self.Amount(self.Amount() - amount)

		record = C80_FinactionsRecord()
		record.GenerateIdo()
		record.RegisterObject(CONTAINER_LOCAL)

		record.Dy(self.Dy())
		record.Dm(self.Dm())
		record.Dd(self.Dd())

		record.SrcAmount(self.SrcAmount())
		record.SrcNote(self.SrcNote())

		record.Amount(amount)

		record.Note(self.Note())
		record.FinstructIdos(self.FinstructIdos())
		record.Labels(self.Labels())

		return record.Ido().data


class C80_Finactions(C70_Finactions):
	""" Финдействия: Логика данных """

	# Выборки данных
	def IdosInDyDmDd(self, dy: int, dm: int = None, dd: int = None) -> list[str]:
		""" Список IDO в указанном периоде """
		record            = C80_FinactionsRecord()

		filter_finactions = C30_FilterLinear1D(record.Idc().data)
		filter_finactions.FilterIdpVlpByEqual(record.f_dy.Idp().data, dy)

		if dm is not None: filter_finactions.FilterIdpVlpByEqual(record.f_dm.Idp().data, dm)
		if dd is not None: filter_finactions.FilterIdpVlpByEqual(record.f_dd.Idp().data, dd)

		filter_finactions.Capture(CONTAINER_LOCAL)

		return filter_finactions.Idos(record.f_amount.Idp().data).data

	def DdsInDyDm(self, dy: int, dm: int) -> list[int]:
		""" Список дней в периоде """
		record            = C80_FinactionsRecord()

		filter_finactions = C30_FilterLinear1D(record.Idc().data)
		filter_finactions.FilterIdpVlpByEqual(record.f_dy.Idp().data, dy)
		filter_finactions.FilterIdpVlpByEqual(record.f_dm.Idp().data, dm)

		filter_finactions.Capture(CONTAINER_LOCAL)

		return filter_finactions.ToIntegers(record.f_dd.Idp().data, flag_distinct=True, flag_sort=True).data

	# Запись финданных
	def CreateRecord(self, dy: int, dm: int, dd: int) -> str:
		""" Создание записи финдействий """
		record = C80_FinactionsRecord()
		record.GenerateIdo()
		record.RegisterObject(CONTAINER_LOCAL)

		record.Dy(dy)
		record.Dm(dm)
		record.Dd(dd)
		record.SrcNote("")
		record.SrcAmount(0.00)
		record.Note("")
		record.Amount(0.00)
		record.Labels([])
		record.FinstructIdos([])
		record.Uid("")

		return record.Ido().data

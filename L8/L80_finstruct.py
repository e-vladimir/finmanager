# ФИНСТРУКТУРА: ЛОГИКА ДАННЫХ

from G30_cactus_datafilters import C30_FilterLinear1D

from L00_containers         import CONTAINER_LOCAL
from L40_finactions         import C40_FinactionsRecord
from L70_finstruct          import C70_FinstructRecord, C70_Finstruct


class C80_FinstructRecord(C70_FinstructRecord):
	""" Запись финструктуры: Логика данных """

	# Финсостояние
	def CalcBalanceCalc(self) -> float:
		""" Расчёт Остатка расчётного """
		finactions_record     = C40_FinactionsRecord()

		filter_data           = C30_FilterLinear1D(finactions_record.Idc().data)
		filter_data.FilterIdpVlpByEqual(finactions_record.f_dy.Idp().data, self.Dy())
		filter_data.FilterIdpVlpByEqual(finactions_record.f_dm.Idp().data, self.Dm())
		filter_data.FilterIdpVlpByInclude(finactions_record.f_finstruct_idos.Idp().data, self.Ido().data)
		filter_data.Capture(CONTAINER_LOCAL)

		amounts : list[float] = [0] + filter_data.ToFloats(finactions_record.f_amount.Idp().data).data

		return self.BalanceStart() + sum(amounts)

	def CalcAmountIncome(self) -> float:
		""" Расчёт Объёма поступлений """
		finactions_record     = C40_FinactionsRecord()

		filter_data           = C30_FilterLinear1D(finactions_record.Idc().data)
		filter_data.FilterIdpVlpByEqual(finactions_record.f_dy.Idp().data, self.Dy())
		filter_data.FilterIdpVlpByEqual(finactions_record.f_dm.Idp().data, self.Dm())
		filter_data.FilterIdpVlpByInclude(finactions_record.f_finstruct_idos.Idp().data, self.Ido().data)
		filter_data.Capture(CONTAINER_LOCAL)

		amounts : list[float] = [0] + filter_data.ToFloats(finactions_record.f_amount.Idp().data).data
		amounts               = filter(lambda amount: amount > 0, amounts)

		return sum(amounts)

	def CalcAmountOutcome(self) -> float:
		""" Расчёт Объёма расхода """
		finactions_record     = C40_FinactionsRecord()

		filter_data           = C30_FilterLinear1D(finactions_record.Idc().data)
		filter_data.FilterIdpVlpByEqual(finactions_record.f_dy.Idp().data, self.Dy())
		filter_data.FilterIdpVlpByEqual(finactions_record.f_dm.Idp().data, self.Dm())
		filter_data.FilterIdpVlpByInclude(finactions_record.f_finstruct_idos.Idp().data, self.Ido().data)
		filter_data.Capture(CONTAINER_LOCAL)

		amounts : list[float] = [0] + filter_data.ToFloats(finactions_record.f_amount.Idp().data).data
		amounts               = filter(lambda amount: amount < 0, amounts)

		return sum(amounts)


class C80_Finstruct(C70_Finstruct):
	""" Финструктура: Логика данных """

	# Выборки данных
	def Groups(self, dy: int, dm: int) -> list[str]:
		""" Группы записей финструктуры """
		record      = C80_FinstructRecord()

		filter_data = C30_FilterLinear1D(record.Idc().data)
		filter_data.FilterIdpVlpByEqual(record.f_dy.Idp().data, dy)
		filter_data.FilterIdpVlpByEqual(record.f_dm.Idp().data, dm)
		filter_data.Capture(CONTAINER_LOCAL)

		return filter_data.ToStrings(record.f_group.Idp().data, flag_distinct=True, flag_sort=True).data

	def Names(self, dy: int, dm: int) -> list[str]:
		""" Наименования записей финструктуры """
		record      = C80_FinstructRecord()

		filter_data = C30_FilterLinear1D(record.Idc().data)
		filter_data.FilterIdpVlpByEqual(record.f_dy.Idp().data, dy)
		filter_data.FilterIdpVlpByEqual(record.f_dm.Idp().data, dm)
		filter_data.Capture(CONTAINER_LOCAL)

		return filter_data.ToStrings(record.f_name.Idp().data, flag_distinct=True, flag_sort=True).data

	def Idos(self, dy: int, dm: int) -> list[str]:
		""" Список IDO записей финструктуры """
		record      = C80_FinstructRecord()

		filter_data = C30_FilterLinear1D(record.Idc().data)
		filter_data.FilterIdpVlpByEqual(record.f_dy.Idp().data, dy)
		filter_data.FilterIdpVlpByEqual(record.f_dm.Idp().data, dm)
		filter_data.Capture(CONTAINER_LOCAL)

		return filter_data.Idos(record.f_name.Idp().data).data

	def NamesInGroup(self, dy: int, dm: int, group: str) -> list[str]:
		""" Список наименований счетов в группе """
		record      = C80_FinstructRecord()

		filter_data = C30_FilterLinear1D(record.Idc().data)
		filter_data.FilterIdpVlpByEqual(record.f_dy.Idp().data, dy)
		filter_data.FilterIdpVlpByEqual(record.f_dm.Idp().data, dm)
		filter_data.FilterIdpVlpByEqual(record.f_group.Idp().data, group)
		filter_data.Capture(CONTAINER_LOCAL)

		return filter_data.ToStrings(record.f_name.Idp().data, flag_distinct=True, flag_sort=True).data

	def IdosInGroup(self, dy: int, dm: int, group: str) -> list[str]:
		""" Список IDO счетов в группе """
		record      = C80_FinstructRecord()

		filter_data = C30_FilterLinear1D(record.Idc().data)
		filter_data.FilterIdpVlpByEqual(record.f_dy.Idp().data, dy)
		filter_data.FilterIdpVlpByEqual(record.f_dm.Idp().data, dm)
		filter_data.FilterIdpVlpByEqual(record.f_group.Idp().data, group)
		filter_data.Capture(CONTAINER_LOCAL)

		return filter_data.Idos(record.f_name.Idp().data).data

	# Конвертация данных
	def IdosToNames(self, idos: list[str]) -> list[str]:
		""" IDO в названия """
		return list(sorted([C80_FinstructRecord(ido).Name() for ido in idos]))

	# Управление записью финструктуры
	def Create(self, dy: int, dm: int, record_name: str, group_name: str) -> bool:
		""" Создание записи финструктуры """
		if record_name in self.Names(dy, dm): return False

		record = C80_FinstructRecord()
		record.GenerateIdo()
		record.RegisterObject(CONTAINER_LOCAL)
		record.Dy(dy)
		record.Dm(dm)
		record.Name(record_name)
		record.Group(group_name)
		record.BalanceStart(0.00)

		return True

	def Rename(self, dy: int, dm: int, name_old: str, name_new: str) -> bool:
		""" Изменение наименования записи финструктуры """
		if     name_new in self.Names(dy, dm)      : return False

		record = C80_FinstructRecord()
		if not record.SwitchByName(dy, dm, name_old): return False

		record.Name(name_new)

		return True

	def Regroup(self, dy: int, dm: int, name_old: str, name_new: str) -> bool:
		""" Изменение наименования группы финструктуры """
		if name_new in self.Groups(dy, dm): return False

		for ido in self.IdosInGroup(dy, dm ,name_old):
			record = C80_FinstructRecord(ido)
			record.Group(name_new)

		return True

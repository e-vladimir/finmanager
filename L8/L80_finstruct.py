# ФИНСТРУКТУРА: ЛОГИКА ДАННЫХ

from G30_cactus_datafilters import C30_FilterLinear1D

from L00_containers         import CONTAINER_LOCAL
from L70_finstruct          import C70_FinstructRecord, C70_Finstruct


class C80_FinstructRecord(C70_FinstructRecord):
	""" Запись финструктуры: Логика данных """
	pass


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

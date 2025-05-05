# АНАЛИТИКА ДАННЫХ: ЛОГИКА ДАННЫХ
# 27 апр 2025

from G30_cactus_datafilters import C30_FilterLinear1D

from L00_containers         import CONTAINERS
from L00_months import MONTHS_SHORT
from L00_operations         import OPERATIONS
from L20_finmanager_struct  import T20_AmountItem, T20_StructItem
from L70_analytics          import C70_Analytics, C70_AnalyticsItem
from L90_operations         import C90_Operation, C90_Operations


class C80_AnalyticsItem(C70_AnalyticsItem):
	""" Элемент аналитики данных: Логика данных """

	# Конвертация
	def ToT20StructItem(self) -> T20_StructItem:
		""" Конвертация в формат T20_StructItem """
		return T20_StructItem(name   = self.name,
		                      ido    = self.Ido().data,
		                      parent = self.parent_ido)

	# Выборка данных
	def SubNames(self) -> list[str]:
		""" Карта наименований """
		struct_data : list[T20_StructItem] = [C80_AnalyticsItem(ido).ToT20StructItem() for ido in self.Idos(CONTAINERS.DISK).data]
		idos        : list[str]            = [struct_item.ido for struct_item in struct_data if struct_item.parent == self.Ido().data]

		for ido in idos: idos.extend([struct_item.ido for struct_item in struct_data if struct_item.parent == ido])

		return [struct_item.name for struct_item in struct_data if struct_item.ido in idos]

	def Amount(self, dy: int, dm: int, use_cache: bool = False) -> T20_AmountItem:
		""" Объём операций """
		destinations : set[str]    = {destination.lower() for destination in [self.name] + self.SubNames()}
		amounts      : list[float] = []
		idos         : list[str]   = C90_Operations.Idos(dy, dm, use_cache=use_cache, type_operation=OPERATIONS.ANALYTICAL)

		for ido in idos:
			operation = C90_Operation(ido)

			if not destinations.intersection(set(operation.destination)): continue

			amounts.append(operation.amount)

		return T20_AmountItem(name           = self.name,
		                      amount_income  = int(sum(filter(lambda amount: amount > 0, amounts))),
		                      amount_outcome = int(sum(filter(lambda amount: amount < 0, amounts)))
		                      )


class C80_Analytics(C70_Analytics):
	""" Аналитика данных: Логика данных """

	# Выборка данных
	def Idos(self, parent_ido: str = None) -> list[str]:
		""" Список IDO """
		analytics_item   = C80_AnalyticsItem()
		idc        : str = analytics_item.Idc().data
		idp_parent : str = analytics_item.FParentIdo.Idp().data
		idp_name   : str = analytics_item.FName.Idp().data

		filter_data      = C30_FilterLinear1D(idc)
		filter_data.FilterIdpVlpByEqual(idp_parent, parent_ido)
		filter_data.Capture(CONTAINERS.DISK)

		return filter_data.Idos(idp_name).data

	def Names(self, parent_name: str = None) -> list[str]:
		""" Список названий элементов аналитики """
		analytics_item   = C80_AnalyticsItem()
		idc        : str = analytics_item.Idc().data
		idp_parent : str = analytics_item.FParentIdo.Idp().data
		idp_name   : str = analytics_item.FName.Idp().data

		filter_data      = C30_FilterLinear1D(idc)

		if parent_name:
			analytics_item.SwitchByName(parent_name)
			filter_data.FilterIdpVlpByEqual(idp_parent, analytics_item.Ido().data)

		filter_data.Capture(CONTAINERS.DISK)

		return filter_data.ToStrings(idp_name, True, True).data

	def Amount(self, dy: int, dm: int, use_cache: bool = False) -> T20_AmountItem:
		""" Объём операций за месяц """
		amounts : list[float] = C90_Operations.Amounts(dy, dm, use_cache=use_cache, type_operation=OPERATIONS.ANALYTICAL)

		return T20_AmountItem(name           = f"{MONTHS_SHORT[dm]} {dy}",
		                      amount_income  = int(sum(filter(lambda amount: amount > 0, amounts))),
		                      amount_outcome = int(sum(filter(lambda amount: amount < 0, amounts)))
		                      )

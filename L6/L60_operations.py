# ФИНАНСОВЫЕ ОПЕРАЦИИ: МЕХАНИКА ДАННЫХ
# 11 мар 2025

from G30_cactus_datafilters import C30_FilterLinear1D

from L00_colors             import COLORS
from L00_containers         import CONTAINERS
from L50_operations         import C50_Operation, C50_Operations


class C60_Operation(C50_Operation):
	""" Финансовая операция: Механика данных """

	# Работа с кешированием
	@property
	def use_cache(self) -> bool:
		return self._use_cache

	@use_cache.setter
	def use_cache(self, flag: bool):
		self._use_cache = flag


	# Счета
	@property
	def account_idos(self) -> list[str]:
		return self.FAccountIdos.ToStrings(CONTAINERS.CACHE if self.use_cache else CONTAINERS.DISK).data

	@account_idos.setter
	def account_idos(self, idos: list[str]):
		self.FAccountIdos.FromStrings(CONTAINERS.DISK, idos)


	# Сумма
	@property
	def amount(self) -> float:
		return self.FAmount.ToFloat(CONTAINERS.CACHE if self.use_cache else CONTAINERS.DISK).data

	@amount.setter
	def amount(self, amount: float):
		self.FAmount.FromFloat(CONTAINERS.DISK, amount)


	# Год
	@property
	def dy(self) -> int:
		return self.FDy.ToInteger(CONTAINERS.CACHE if self.use_cache else CONTAINERS.DISK).data

	@dy.setter
	def dy(self, year: int):
		self.FDy.FromInteger(CONTAINERS.DISK, year)


	# Месяц
	@property
	def dm(self) -> int:
		return self.FDm.ToInteger(CONTAINERS.CACHE if self.use_cache else CONTAINERS.DISK).data

	@dm.setter
	def dm(self, month: int):
		self.FDm.FromInteger(CONTAINERS.DISK, month)


	# Число месяца
	@property
	def dd(self) -> int:
		return self.FDd.ToInteger(CONTAINERS.CACHE if self.use_cache else CONTAINERS.DISK).data

	@dd.setter
	def dd(self, day: int):
		self.FDd.FromInteger(CONTAINERS.DISK, day)


	# Описание
	@property
	def description(self) -> str:
		return self.FDescription.ToString(CONTAINERS.CACHE if self.use_cache else CONTAINERS.DISK).data

	@description.setter
	def description(self, text: str):
		self.FDescription.FromString(CONTAINERS.DISK, text)


	# Назначение
	@property
	def destination(self) -> str:
		return self.FDestination.ToString(CONTAINERS.CACHE if self.use_cache else CONTAINERS.DISK).data

	@destination.setter
	def destination(self, text: str):
		self.FDestination.FromString(CONTAINERS.DISK, text)


	# Цветовая метка
	@property
	def color(self) -> COLORS:
		return COLORS(self.FColor.ToString(CONTAINERS.CACHE if self.use_cache else CONTAINERS.DISK).data)

	@color.setter
	def color(self, color: COLORS):
		self.FColor.FromString(CONTAINERS.DISK, color.value)


	# Метки
	@property
	def labels(self) -> list[str]:
		return self.FLabels.ToStrings(CONTAINERS.CACHE if self.use_cache else CONTAINERS.DISK).data

	@labels.setter
	def labels(self, labels: list[str]):
		self.FLabels.FromStrings(CONTAINERS.DISK, labels)


	# Корневая операция
	@property
	def parent_ido(self) -> str:
		return self.FParentIdo.ToString(CONTAINERS.CACHE if self.use_cache else CONTAINERS.DISK).data

	@parent_ido.setter
	def parent_ido(self, ido: str):
		self.FParentIdo.FromString(CONTAINERS.DISK, ido)


	# Отметка Не учитывать
	@property
	def skip(self) -> bool:
		return self.FSkip.ToBoolean(CONTAINERS.CACHE if self.use_cache else CONTAINERS.DISK).data

	@skip.setter
	def skip(self, flag: bool):
		self.FSkip.FromBoolean(CONTAINERS.DISK, flag)


	# Виртуальные операции
	@property
	def virtual_idos(self) -> list[str]:
		return self.FVirtualIdos.ToStrings(CONTAINERS.CACHE if self.use_cache else CONTAINERS.DISK).data

	@virtual_idos.setter
	def virtual_idos(self, idos: list[str]):
		self.FVirtualIdos.FromStrings(CONTAINERS.DISK, idos)

	def CalcVirtualIdos(self):
		""" Формирование списка виртуальных операций """
		idc            : str = self.Idc().data
		idp_parent_ido : str = self.FParentIdo.Idp().data
		idp_amount     : str = self.FAmount.Idp().data

		filter_data          = C30_FilterLinear1D(idc)
		filter_data.FilterIdpVlpByEqual(idp_parent_ido, self.Ido().data)
		filter_data.Capture(CONTAINERS.DISK)

		self.virtual_idos    = filter_data.Idos(idp_amount).data


class C60_Operations(C50_Operations):
	""" Финансовые операции: Механика данных """
	pass

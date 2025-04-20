# ФИНАНСОВЫЕ ОПЕРАЦИИ: МЕХАНИКА ДАННЫХ
# 11 мар 2025

from G10_list       import ClearList

from L00_colors     import COLORS
from L00_containers import CONTAINERS
from L50_operations import C50_Operation, C50_Operations


class C60_Operation(C50_Operation):
	""" Финансовая операция: Механика данных """

	# Работа с кешированием
	@property
	def use_cache(self) -> bool:
		return self._use_cache

	@use_cache.setter
	def use_cache(self, flag: bool):
		self._use_cache = flag


	# Год
	@property
	def dy(self) -> int:
		return self.FDy.ToInteger(CONTAINERS.CACHE if self.use_cache else CONTAINERS.DISK).data

	@dy.setter
	def dy(self, year: int):
		self.FDy.FromInteger(CONTAINERS.DISK, year)

		if not self.use_cache: return
		self.FDy.FromInteger(CONTAINERS.CACHE, year)


	# Месяц
	@property
	def dm(self) -> int:
		return self.FDm.ToInteger(CONTAINERS.CACHE if self.use_cache else CONTAINERS.DISK).data

	@dm.setter
	def dm(self, month: int):
		self.FDm.FromInteger(CONTAINERS.DISK, month)

		if not self.use_cache: return
		self.FDm.FromInteger(CONTAINERS.CACHE, month)


	# Число месяца
	@property
	def dd(self) -> int:
		return self.FDd.ToInteger(CONTAINERS.CACHE if self.use_cache else CONTAINERS.DISK).data

	@dd.setter
	def dd(self, day: int):
		self.FDd.FromInteger(CONTAINERS.DISK, day)

		if not self.use_cache: return
		self.FDd.FromInteger(CONTAINERS.CACHE, day)


	# Счета
	@property
	def account_idos(self) -> list[str]:
		return self.FAccountIdos.ToStrings(CONTAINERS.CACHE if self.use_cache else CONTAINERS.DISK).data

	@account_idos.setter
	def account_idos(self, idos: list[str]):
		self.FAccountIdos.FromStrings(CONTAINERS.DISK, idos)

		if not self.use_cache: return
		self.FAccountIdos.FromStrings(CONTAINERS.CACHE, idos)


	# Сумма
	@property
	def amount(self) -> float:
		return self.FAmount.ToFloat(CONTAINERS.CACHE if self.use_cache else CONTAINERS.DISK).data

	@amount.setter
	def amount(self, amount: float):
		self.FAmount.FromFloat(CONTAINERS.DISK, amount)

		if not self.use_cache: return
		self.FAmount.FromFloat(CONTAINERS.CACHE, amount)


	# Описание
	@property
	def description(self) -> str:
		return self.FDescription.ToString(CONTAINERS.CACHE if self.use_cache else CONTAINERS.DISK).data

	@description.setter
	def description(self, text: str):
		self.FDescription.FromString(CONTAINERS.DISK, text)

		if not self.use_cache: return
		self.FDescription.FromString(CONTAINERS.CACHE, text)


	# Назначение
	@property
	def destination(self) -> str:
		return self.FDestination.ToString(CONTAINERS.CACHE if self.use_cache else CONTAINERS.DISK).data

	@destination.setter
	def destination(self, text: str):
		self.FDestination.FromString(CONTAINERS.DISK, text)

		if not self.use_cache: return
		self.FDestination.FromString(CONTAINERS.CACHE, text)


	# Цветовая метка
	@property
	def color(self) -> COLORS:
		return COLORS(self.FColor.ToString(CONTAINERS.CACHE if self.use_cache else CONTAINERS.DISK).data)

	@color.setter
	def color(self, color: COLORS):
		self.FColor.FromString(CONTAINERS.DISK, color.value)

		if not self.use_cache: return
		self.FColor.FromString(CONTAINERS.CACHE, color.value)


	# Метки
	@property
	def labels(self) -> list[str]:
		return sorted(self.FLabels.ToStrings(CONTAINERS.CACHE if self.use_cache else CONTAINERS.DISK).data)

	@labels.setter
	def labels(self, items: list[str]):
		self.FLabels.FromStrings(CONTAINERS.DISK, ClearList(items))

		if not self.use_cache: return
		self.FLabels.FromStrings(CONTAINERS.CACHE, ClearList(items))


	# Отметка Не учитывать
	@property
	def skip(self) -> bool:
		return self.FSkip.ToBoolean(CONTAINERS.CACHE if self.use_cache else CONTAINERS.DISK).data

	@skip.setter
	def skip(self, flag: bool):
		self.FSkip.FromBoolean(CONTAINERS.DISK, flag)

		if not self.use_cache: return
		self.FSkip.FromBoolean(CONTAINERS.CACHE, flag)



class C60_Operations(C50_Operations):
	""" Финансовые операции: Механика данных """
	pass

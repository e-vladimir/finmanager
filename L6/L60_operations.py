# ФИНАНСОВЫЕ ОПЕРАЦИИ: МЕХАНИКА ДАННЫХ
# 11 мар 2025

from L00_containers import CONTAINERS
from L50_operations import C50_Operation, C50_Operations


class C60_Operation(C50_Operation):
	""" Финансовая операция: Механика данных """

	# Год
	@property
	def dy(self) -> int:
		return self.FDy.ToInteger(CONTAINERS.DISK).data
	@dy.setter
	def dy(self, year: int):
		self.FDy.FromInteger(CONTAINERS.DISK, year)

	# Месяц
	@property
	def dm(self) -> int:
		return self.FDm.ToInteger(CONTAINERS.DISK).data
	@dm.setter
	def dm(self, month: int):
		self.FDm.FromInteger(CONTAINERS.DISK, month)

	# Число месяца
	@property
	def dd(self) -> int:
		return self.FDd.ToInteger(CONTAINERS.DISK).data
	@dd.setter
	def dd(self, day: int):
		self.FDd.FromInteger(CONTAINERS.DISK, day)

	# Счета
	@property
	def accounts_ido(self) -> list[str]:
		return self.FAccountIdos.ToStrings(CONTAINERS.DISK).data
	@accounts_ido.setter
	def accounts_ido(self, idos: list[str]):
		self.FAccountIdos.FromStrings(CONTAINERS.DISK, idos)

	# Сумма
	@property
	def amount(self) -> float:
		return self.FAmount.ToFloat(CONTAINERS.DISK).data
	@amount.setter
	def amount(self, amount: float):
		self.FAmount.FromFloat(CONTAINERS.DISK, amount)

	# Описание
	@property
	def description(self) -> str:
		return self.FDescription.ToString(CONTAINERS.DISK).data
	@description.setter
	def description(self, text: str):
		self.FDescription.FromString(CONTAINERS.DISK, text)


class C60_Operations(C50_Operations):
	""" Финансовые операции: Механика данных """
	pass

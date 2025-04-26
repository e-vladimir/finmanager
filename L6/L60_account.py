# СЧЁТ: МЕХАНИКА ДАННЫХ
# 14 фев 2025

from G30_cactus_datafilters import C30_FilterLinear1D

from L00_containers         import CONTAINERS
from L00_operations         import OPERATIONS
from L50_account            import C50_Account, C50_Accounts
from L90_operations         import C90_Operations


class C60_Account(C50_Account):
	""" Счёт: Механика данных """

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


	# Название счёта
	@property
	def name(self) -> str:
		return self.FName.ToString(CONTAINERS.DISK).data

	@name.setter
	def name(self, text: str):
		self.FName.FromString(CONTAINERS.DISK, text)


	# Группа счетов
	@property
	def group(self) -> str:
		return self.FGroup.ToString(CONTAINERS.DISK).data

	@group.setter
	def group(self, name: str):
		self.FGroup.FromString(CONTAINERS.DISK, name)


	# Остаток на начало месяца
	@property
	def balance_initial(self) -> int:
		return self.FBalanceInitial.ToInteger(CONTAINERS.DISK).data

	@balance_initial.setter
	def balance_initial(self, amount: int):
		self.FBalanceInitial.FromInteger(CONTAINERS.DISK, amount)


	# Остаток на конец месяца
	@property
	def balance_summary(self) -> int:
		return int(self.balance_initial + sum(C90_Operations.Amounts(dy            = self.dy,
		                                                             dm            = self.dm,
		                                                             account_ido   = self.Ido().data,
		                                                             type_operation = OPERATIONS.ACCOUNTING)
		                                      )
		           )


	# Объём поступлений
	@property
	def amount_income(self) -> int:
		return sum(filter(lambda amount: amount > 0,
		                  C90_Operations.Amounts(dy             = self.dy,
		                                         dm             = self.dm,
		                                         account_ido    = self.Ido().data,
		                                         type_operation = OPERATIONS.ACCOUNTING)
		                  )
		           )


	# Объём списаний
	@property
	def amount_outcome(self) -> int:
		return abs(sum(filter(lambda amount: amount < 0,
		                  C90_Operations.Amounts(dy             = self.dy,
		                                         dm             = self.dm,
		                                         account_ido    = self.Ido().data,
		                                         type_operation = OPERATIONS.ACCOUNTING)
		                  )
		               ))


	# IDO
	def SwitchByName(self, dy: int, dm: int, name: str) -> bool:
		""" Переключение по названию счёта """
		if not name: return False

		idc      : str = self.Idc().data
		idp_dy   : str = self.FDy.Idp().data
		idp_dm   : str = self.FDm.Idp().data
		idp_name : str = self.FName.Idp().data

		filter_data    = C30_FilterLinear1D(idc)
		filter_data.FilterIdpVlpByEqual(idp_dy, dy)
		filter_data.FilterIdpVlpByEqual(idp_dm, dm)
		filter_data.FilterIdpVlpByEqual(idp_name, name)
		filter_data.Capture(CONTAINERS.DISK)

		try   : self.Ido(filter_data.Idos().data[0])
		except: return False

		return True


class C60_Accounts(C50_Accounts):
	""" Контроллер счетов: Механика данных """

	# Выборка данных
	@classmethod
	def CalcBalanceInitial(cls, dy: int, dm: int) -> int:
		""" Общий баланс на начало месяца """
		account           = C60_Account()
		idc         : str = account.Idc().data
		idp_dy      : str = account.FDy.Idp().data
		idp_dm      : str = account.FDm.Idp().data
		idp_balance : str = account.FBalanceInitial.Idp().data

		filter_data = C30_FilterLinear1D(idc)
		filter_data.FilterIdpVlpByEqual(idp_dy, dy)
		filter_data.FilterIdpVlpByEqual(idp_dm, dm)
		filter_data.Capture(CONTAINERS.DISK)

		return sum(filter_data.ToIntegers(idp_balance).data)

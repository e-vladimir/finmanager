# СЧЕТА: ЛОГИКА ДАННЫХ

from G10_datetime           import CalcDyDmByShiftDm
from G30_cactus_datafilters import C30_FilterLinear1D

from L00_containers         import CONTAINERS
from L70_accounts           import C70_Accounts, C70_AccountGroup, C70_Account


class C80_Account(C70_Account):
	""" Счёт: Логика данных """

	# Перенос в смежные периоды
	def TransferToNextDm(self):
		""" Перенос месяца в следующий месяц """
		dy, dm = self.DyDm()
		dy, dm = CalcDyDmByShiftDm(dy, dm, 1)

		account = C80_Account()
		if not account.SwitchByNameInDyDm(dy, dm, self.Name()):
			account.GenerateIdo()
			account.RegisterObject(CONTAINERS.DISK)
			account.Name(self.Name())
			account.Dy(dy)
			account.Dm(dm)

		account.Group(self.Group())

	def TransferToPrevDm(self):
		""" Перенос месяца в предыдущий месяц """
		dy, dm = self.DyDm()
		dy, dm = CalcDyDmByShiftDm(dy, dm, -1)

		account = C80_Account()
		if not account.SwitchByNameInDyDm(dy, dm, self.Name()):
			account.GenerateIdo()
			account.RegisterObject(CONTAINERS.DISK)
			account.Name(self.Name())
			account.Dy(dy)
			account.Dm(dm)

		account.Group(self.Group())

	# Управление группой счетов
	def ChangeGroup(self, group_name: str) -> bool:
		""" Смена группы счетов """
		if not group_name: return False

		idc       : str = self.Idc().data
		idp_dy    : str = self.f_dy.Idp().data
		idp_dm    : str = self.f_dm.Idp().data
		idp_name  : str = self.f_name.Idp().data

		filter_accounts = C30_FilterLinear1D(idc)
		filter_accounts.FilterIdpVlpByEqual(idp_dy, self.Dy())
		filter_accounts.FilterIdpVlpByEqual(idp_dm, self.Dm())
		filter_accounts.Capture(CONTAINERS.DISK)

		accounts_names : list[str] = filter_accounts.ToStrings(idp_name, True, True).data

		if group_name in accounts_names: return False

		self.Group(group_name)

		return True


class C80_AccountGroup(C70_AccountGroup):
	""" Группа счетов: Логика данных """

	# Перенос в смежные периоды
	def TransferToNextDm(self, dy: int, dm: int):
		""" Перенос группы счетов в следующий месяц """
		for ido in self.AccountsIdosInDyDm(dy, dm):
			account = C80_Account(ido)
			account.TransferToNextDm()

	def TransferToPrevDm(self, dy: int, dm: int):
		""" Перенос группы счетов в прошлый месяц """
		for ido in self.AccountsIdosInDyDm(dy, dm):
			account = C80_Account(ido)
			account.TransferToPrevDm()

	# Управление группой счетов
	def Rename(self, dy: int, dm: int, group_name: str) -> bool:
		""" Переименование группы счетов """
		if not self.ProcessingGroup()    : return False
		if not group_name                : return False

		account                  = C80_Account()

		idc          : str       = account.Idc().data
		idp_dy       : str       = account.f_dy.Idp().data
		idp_dm       : str       = account.f_dm.Idp().data
		idp_group    : str       = account.f_group.Idp().data

		filter_accounts          = C30_FilterLinear1D(idc)
		filter_accounts.FilterIdpVlpByEqual(idp_dy, dy)
		filter_accounts.FilterIdpVlpByEqual(idp_dm, dm)
		filter_accounts.Capture(CONTAINERS.DISK)

		groups_names : list[str] = filter_accounts.ToStrings(idp_group, True, True).data
		if     group_name in groups_names: return False

		filter_accounts.FilterIdpVlpByEqual(idp_group, self.ProcessingGroup())
		filter_accounts.Capture(CONTAINERS.DISK)

		idos         : list[str] = filter_accounts.Idos().data

		for ido in idos:
			account.Ido(ido)
			account.Group(group_name)

	# Счета
	def AccountsIdosInDyDm(self, dy: int, dm: int) -> list[str]:
		""" Список IDO счетов в указанном периоде """
		if not self._processing_group: return []

		account         = C80_Account()

		idc       : str = account.Idc().data
		idp_dy    : str = account.f_dy.Idp().data
		idp_dm    : str = account.f_dm.Idp().data
		idp_name  : str = account.f_name.Idp().data
		idp_group : str = account.f_group.Idp().data

		filter_accounts = C30_FilterLinear1D(idc)
		filter_accounts.FilterIdpVlpByEqual(idp_dy, dy)
		filter_accounts.FilterIdpVlpByEqual(idp_dm, dm)
		filter_accounts.FilterIdpVlpByEqual(idp_group, self.ProcessingGroup())
		filter_accounts.Capture(CONTAINERS.DISK)

		return filter_accounts.Idos(idp_name).data


class C80_Accounts(C70_Accounts):
	""" Счета: Логика данных """

	# Счета
	def IdosToNames(self, idos: list[str]) -> list[str]:
		""" Список IDO в список названий """
		result : list[str] = []

		for ido in idos:
			account = C80_Account(ido)
			result.append(account.Name())

		result.sort()

		return result

	def NamesToIdos(self, dy: int, dm: int, names: list[str]) -> list[str]:
		""" Список IDO из списка наименований """
		result : list[str] = []

		account            = C80_Account()
		for name in names:
			if not account.SwitchByNameInDyDm(dy, dm, name): continue

			result.append(account.Ido().data)

		return result

	def AccountsIdosInDyDm(self, dy: int, dm: int = None) -> list[str]:
		""" Список IDO счетов в указанном периоде """
		account         = C80_Account()

		idc       : str = account.Idc().data
		idp_dy    : str = account.f_dy.Idp().data
		idp_dm    : str = account.f_dm.Idp().data
		idp_name  : str = account.f_name.Idp().data

		filter_accounts = C30_FilterLinear1D(idc)
		filter_accounts.FilterIdpVlpByEqual(idp_dy, dy)
		filter_accounts.FilterIdpVlpByEqual(idp_dm, dm)
		filter_accounts.Capture(CONTAINERS.DISK)

		return filter_accounts.Idos(idp_name).data

	def AccountsNamesInDyDm(self, dy: int, dm: int = None, group_name: str = None) -> list[str]:
		""" Список названий счетов в указанном периоде """
		account         = C80_Account()

		idc       : str = account.Idc().data
		idp_dy    : str = account.f_dy.Idp().data
		idp_dm    : str = account.f_dm.Idp().data
		idp_group : str = account.f_group.Idp().data
		idp_name  : str = account.f_name.Idp().data

		filter_accounts = C30_FilterLinear1D(idc)
		filter_accounts.FilterIdpVlpByEqual(idp_dy, dy)
		filter_accounts.FilterIdpVlpByEqual(idp_dm, dm)
		filter_accounts.FilterIdpVlpByEqual(idp_group, group_name)
		filter_accounts.Capture(CONTAINERS.DISK)

		return filter_accounts.ToStrings(idp_name, True, True).data

	# Группа счетов
	def GroupsNamesInDyDm(self, dy: int, dm: int = None) -> list[str]:
		""" Список названий групп счетов в указанном периоде """
		account         = C80_Account()

		idc       : str = account.Idc().data
		idp_dy    : str = account.f_dy.Idp().data
		idp_dm    : str = account.f_dm.Idp().data
		idp_group : str = account.f_group.Idp().data

		filter_accounts = C30_FilterLinear1D(idc)
		filter_accounts.FilterIdpVlpByEqual(idp_dy, dy)
		filter_accounts.FilterIdpVlpByEqual(idp_dm, dm)
		filter_accounts.Capture(CONTAINERS.DISK)

		return filter_accounts.ToStrings(idp_group, True, True).data

	# Счёт
	def CreateAccountInDyDm(self, dy: int, dm: int, group_name: str, account_name: str) -> str:
		""" Создание счёта """
		if not account_name                                    : return ""
		if not group_name                                      : return ""

		if     account_name in self.AccountsNamesInDyDm(dy, dm): return ""
		if     account_name in self.GroupsNamesInDyDm(dy, dm)  : return ""

		account = C80_Account()
		account.GenerateIdo()
		account.RegisterObject(CONTAINERS.DISK)

		account.Dy(dy)
		account.Dm(dm)
		account.Name(account_name)
		account.Group(group_name)

		return account.Ido().data

	def RenameAccountInDyDm(self, dy: int, dm: int, name_old: str, name_new: str) -> bool:
		""" Переименование счёта """
		if     name_new in self.AccountsNamesInDyDm(dy, dm): return False

		account = C80_Account()
		if not account.SwitchByNameInDyDm(dy, dm, name_old): return False

		account.Name(name_new)

		return True

	# Перенос в смежные периоды
	def TransferToNextDm(self, dy: int, dm: int):
		""" Перенос структуры счетов в следующий месяц """
		for ido in self.AccountsIdosInDyDm(dy, dm):
			account = C80_Account(ido)
			account.TransferToNextDm()

	def TransferToPrevDm(self, dy: int, dm: int):
		""" Перенос структуры счетов в прошлый месяц """
		for ido in self.AccountsIdosInDyDm(dy, dm):
			account = C80_Account(ido)
			account.TransferToPrevDm()

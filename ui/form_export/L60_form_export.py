# ФОРМА ЭКСПОРТ ДАННЫХ: МЕХАНИКА ДАННЫХ
# 01 апр 2025

from pathlib         import Path

from G10_datetime    import CurrentDy

from L00_form_export import ACCOUNTS, EXPORT_FIELDS, INTERVALS
from L00_months      import MONTHS_SHORT
from L20_PySide6 import C20_StandardItem, ROLES, RequestDirectory, RequestItem, RequestText, RequestValue
from L50_form_export import C50_FormExport


class C60_FormExport(C50_FormExport):
	""" Форма экспорт данных: Механика данных """

	# Экспорт операций: Режим интервала
	@property
	def operations_interval_mode(self) -> INTERVALS:
		return self._operations_interval_mode

	@operations_interval_mode.setter
	def operations_interval_mode(self, mode: INTERVALS):
		self._operations_interval_mode = mode

	def SetOperationsIntervalMode(self):
		""" Установка значения """
		modes : list[str]  = [INTERVALS.ALL,
		                      INTERVALS.DY,
		                      INTERVALS.DM]

		mode  : str | None = RequestItem("Экспорт данных",
		                                 "Интервал экспорта",
		                                 modes)
		if mode is None: return

		self.operations_interval_mode = INTERVALS(mode)

		self.on_OptionsOperationsChanged()

	# Экспорт операций: Год
	@property
	def operations_interval_dy(self) -> int:
		return self._operations_interval_dy

	@operations_interval_dy.setter
	def operations_interval_dy(self, year: int):
		self._operations_interval_dy = year

	def SetOperationsIntervalDy(self):
		""" Установка значения """
		match self.operations_interval_mode:
			case INTERVALS.ALL: return
			case INTERVALS.DM : return

		dy : int | None = RequestValue("Экспорт данных",
		                               "Интервал экспорта: год",
		                               self.operations_interval_dy,
		                               CurrentDy() - 100,
		                               CurrentDy())
		if dy is None: return

		self.operations_interval_dy = dy

		self.on_OptionsOperationsChanged()


	# Экспорт операций: Месяц
	@property
	def operations_interval_dm(self) -> int:
		return self._operations_interval_dm

	@operations_interval_dm.setter
	def operations_interval_dm(self, month: int):
		self._operations_interval_dm = month

	def SetOperationsIntervalDm(self):
		""" Установка значения """
		match self.operations_interval_mode:
			case INTERVALS.ALL: return
			case INTERVALS.DY : return

		text  : str | None = RequestText("Экспорт данных",
		                                "Интервал экспорта: месяц",
		                                f"{MONTHS_SHORT[self.operations_interval_dm]} {self.operations_interval_dy}")
		if text is None: return

		dm_dy : list[str]  = (text.lower()
		                          .strip()
		                          .split(' '))
		dm    : str        = dm_dy[0]
		dy    : str        = dm_dy[1]

		if     dm not in MONTHS_SHORT: return
		if not dy.isdigit()          : return

		self.operations_interval_dy = int(dy)
		self.operations_interval_dm = MONTHS_SHORT.index(dm)

		self.on_OptionsOperationsChanged()


	# Экспорт операций: Режим счётов
	@property
	def operations_accounts_mode(self) -> ACCOUNTS:
		return self._operations_accounts_mode

	@operations_accounts_mode.setter
	def operations_accounts_mode(self, mode: ACCOUNTS):
		self._operations_accounts_mode = mode

	def SetOperationsAccountsMode(self):
		""" Установка значения """
		modes : list[str]  = [ACCOUNTS.ALL,
		                      ACCOUNTS.GROUP,
		                      ACCOUNTS.ACCOUNT]

		mode  : str | None = RequestItem("Экспорт данных",
		                                 "Счета",
		                                 modes)

		if mode is None: return

		self.operations_accounts_mode = ACCOUNTS(mode)

		self.on_OptionsOperationsChanged()


	# Экспорт операций: Группа счетов
	@property
	def operations_accounts_group(self) -> str:
		return self._operations_accounts_group

	@operations_accounts_group.setter
	def operations_accounts_group(self, group_name: str):
		self._operations_accounts_group = group_name

	def SetOperationsAccountsGroup(self):
		""" Установка значения """
		match self.operations_accounts_mode:
			case ACCOUNTS.ALL    : return
			case ACCOUNTS.ACCOUNT: return

		groups : list[str] = []
		match self.operations_interval_mode:
			case INTERVALS.ALL: groups = self.Accounts.Groups()
			case INTERVALS.DY : groups = self.Accounts.Groups(self.operations_interval_dy)
			case INTERVALS.DM : groups = self.Accounts.Groups(self.operations_interval_dy, self._operations_interval_dm)

		group : str | None = RequestItem("Экспорт данных",
		                                 "Группа счетов",
		                                 groups)
		if group is None: return

		self.operations_accounts_group = group

		self.on_OptionsOperationsChanged()


	# Экспорт операций: Счёт
	@property
	def operations_accounts_account(self) -> str:
		return self._operations_accounts_account

	@operations_accounts_account.setter
	def operations_accounts_account(self, account_name: str):
		self._operations_accounts_account = account_name

	def SetOperationsAccountsAccount(self):
		""" Установка значения """
		match self.operations_accounts_mode:
			case ACCOUNTS.ALL  : return
			case ACCOUNTS.GROUP: return

		accounts : list[str] = []
		match self.operations_interval_mode:
			case INTERVALS.ALL: accounts = self.Accounts.Names()
			case INTERVALS.DY : accounts = self.Accounts.Names(self.operations_interval_dy)
			case INTERVALS.DM : accounts = self.Accounts.Names(self.operations_interval_dy, self._operations_interval_dm)

		account : str | None = RequestItem("Экспорт данных",
		                                   "Счёт",
		                                   accounts)
		if account is None: return

		self.operations_accounts_account = account

		self.on_OptionsOperationsChanged()


	# Экспорт операций: Директория
	@property
	def operations_directory(self) -> Path:
		return self._operations_directory

	@operations_directory.setter
	def operations_directory(self, path: Path):
		self._operations_directory = path

	def SetOperationsDirectory(self):
		""" Установка значения """
		directory : Path | None = RequestDirectory("Экспорт данных", f"{self.operations_directory}")
		if directory is None: return

		self.operations_directory = directory

		self.on_OptionsOperationsChanged()


	# Рабочее поле
	@property
	def processing_field(self) -> EXPORT_FIELDS:
		return self._processing_field

	@processing_field.setter
	def processing_field(self, field: EXPORT_FIELDS):
		self._processing_field = field

	def ReadProcessingFieldFromTreeDataOperations(self):
		""" Чтение из дерева данных экспорта операций """
		self.processing_field = EXPORT_FIELDS(self.TreeDataOperations.currentIndex().data(ROLES.IDO))


	# Модель данных экспорта операций
	def InitModelDataOperations(self):
		""" Инициализация модели данных экспорта операций """
		self.ModelDataOperations.removeAll()
		self.ModelDataOperations.setHorizontalHeaderLabels(["Параметр", "Значение"])

		items             = [EXPORT_FIELDS.INTERVAL,
		                     EXPORT_FIELDS.ACCOUNTS,
		                     EXPORT_FIELDS.DIRECTORY
		                     ]

		group_filter      = C20_StandardItem("Параметры экспорта")

		for item in items:
			item_field        = C20_StandardItem(title        = item,
			                                     data         = item,
			                                     data_role    = ROLES.IDO)
			item_value        = C20_StandardItem("",
			                                     item,
			                                     ROLES.IDO)
			group_filter.appendRow([item_field, item_value])

		self.ModelDataOperations.appendRow([group_filter, C20_StandardItem("")])

	def LoadModelDataOperations(self):
		""" Загрузка модели данных экспорта операций """
		indexes   = self.ModelDataOperations.indexesInRowByIdo(EXPORT_FIELDS.INTERVAL)
		item_data = self.ModelDataOperations.itemFromIndex(indexes[1])

		match self.operations_interval_mode:
			case INTERVALS.ALL: item_data.setText(f"За всё время")
			case INTERVALS.DY : item_data.setText(f"{self.operations_interval_dy} год")
			case INTERVALS.DM : item_data.setText(f"{MONTHS_SHORT[self.operations_interval_dm]} {self.operations_interval_dy}")

		indexes   = self.ModelDataOperations.indexesInRowByIdo(EXPORT_FIELDS.ACCOUNTS)
		item_data = self.ModelDataOperations.itemFromIndex(indexes[1])

		match self.operations_accounts_mode:
			case ACCOUNTS.ALL    : item_data.setText(f"Все счета")
			case ACCOUNTS.GROUP  : item_data.setText(f"Группа счетов {self.operations_accounts_group}")
			case ACCOUNTS.ACCOUNT: item_data.setText(f"{self.operations_accounts_account}")

		indexes   = self.ModelDataOperations.indexesInRowByIdo(EXPORT_FIELDS.DIRECTORY)
		item_data = self.ModelDataOperations.itemFromIndex(indexes[1])
		item_data.setText(f"{self.operations_directory.absolute()}")

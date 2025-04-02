# ФОРМА ЭКСПОРТ ДАННЫХ: МЕХАНИКА ДАННЫХ
# 01 апр 2025

from pathlib         import Path

from L00_form_export import ACCOUNTS, EXPORT, INTERVALS
from L00_months      import MONTHS_SHORT
from L20_PySide6     import C20_StandardItem, ROLES
from L50_form_export import C50_FormExport


class C60_FormExport(C50_FormExport):
	""" Форма экспорт данных: Механика данных """

	# Экспорт операций: Режим интервала
	@property
	def operations_interval_mode(self) -> INTERVALS:
		return self._operations_interval_mode

	@operations_interval_mode.setter
	def operations_interval_mode(self, mode: INTERVALS):
		self.operations_interval_mode = mode


	# Экспорт операций: Год
	@property
	def operations_interval_dy(self) -> int:
		return self._operations_interval_dy

	@operations_interval_dy.setter
	def operations_interval_dy(self, year: int):
		self._operations_interval_dy = year


	# Экспорт операций: Месяц
	@property
	def operations_interval_dm(self) -> int:
		return self._operations_interval_dm

	@operations_interval_dm.setter
	def operations_interval_dm(self, month: int):
		self._operations_interval_dm = month


	# Экспорт операций: Режим счётов
	@property
	def operations_accounts_mode(self) -> ACCOUNTS:
		return self._operations_accounts_mode

	@operations_accounts_mode.setter
	def operations_accounts_mode(self, mode: ACCOUNTS):
		self._operations_accounts_mode = mode


	# Экспорт операций: Группа счетов
	@property
	def operations_accounts_group(self) -> str:
		return self._operations_accounts_group

	@operations_accounts_group.setter
	def operations_accounts_group(self, group_name: str):
		self._operations_accounts_group = group_name


	# Экспорт операций: Счёт
	@property
	def operations_accounts_account(self) -> str:
		return self._operations_accounts_account

	@operations_accounts_account.setter
	def operations_accounts_account(self, account_name: str):
		self._operations_accounts_account = account_name


	# Экспорт операций: Директория
	@property
	def operations_directory(self) -> Path:
		return self._operations_directory

	@operations_directory.setter
	def operations_directory(self, path: Path):
		self._operations_directory = path


	# Модель данных экспорта операций
	def InitModelDataOperations(self):
		""" Инициализация модели данных экспорта операций """
		self.ModelDataOperations.removeAll()
		self.ModelDataOperations.setHorizontalHeaderLabels(["Параметр", "Значение"])

		items             = [EXPORT.INTERVAL,
		                     EXPORT.ACCOUNTS,
		                     EXPORT.DIRECTORY
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
		indexes   = self.ModelDataOperations.indexesInRowByIdo(EXPORT.INTERVAL)
		item_data = self.ModelDataOperations.itemFromIndex(indexes[1])

		match self.operations_interval_mode:
			case INTERVALS.ALL: item_data.setText(f"Все доступные периоды")
			case INTERVALS.DY : item_data.setText(f"{self.operations_interval_dy} год")
			case INTERVALS.DM : item_data.setText(f"{MONTHS_SHORT[self.operations_interval_dm]} {self.operations_interval_dy}")

		indexes   = self.ModelDataOperations.indexesInRowByIdo(EXPORT.ACCOUNTS)
		item_data = self.ModelDataOperations.itemFromIndex(indexes[1])

		match self.operations_accounts_mode:
			case ACCOUNTS.ALL    : item_data.setText(f"Все счета")
			case ACCOUNTS.GROUP  : item_data.setText(f"Группа счетов {self.operations_accounts_group}")
			case ACCOUNTS.ACCOUNT: item_data.setText(f"{self.operations_accounts_account}")

		indexes   = self.ModelDataOperations.indexesInRowByIdo(EXPORT.DIRECTORY)
		item_data = self.ModelDataOperations.itemFromIndex(indexes[1])
		item_data.setText(f"{self.operations_directory.absolute()}")

# ФОРМА ЭКСПОРТ ДАННЫХ: МЕХАНИКА ДАННЫХ

from PySide6.QtCore    import QModelIndex

from L00_months        import MONTHS
from L00_struct_export import EXPORT_ID, EXPORT_MODE_DATE, EXPORT_MODE_ACCOUNTS
from L20_PySide6       import C20_StandardItem, ROLES
from L50_form_export   import C50_FormExport


class C60_FormExport(C50_FormExport):
	""" Форма Экспорт данных: Механика данных """

	# Модель экспорта операций
	def InitModelDataOperations(self):
		""" Инициализация модели данных финансовых операций """
		self.model_operations.removeAll()

		item_input  = C20_StandardItem("ПАРАМЕТРЫ ВЫБОРКИ")
		item_input.appendRow([C20_StandardItem("Период данных",      EXPORT_ID.MODE_DATE, ROLES.IDO), C20_StandardItem("Все периоды", EXPORT_ID.MODE_DATE, ROLES.IDO)])
		item_input.appendRow([C20_StandardItem("Счёт",               EXPORT_ID.ACCOUNT,   ROLES.IDO), C20_StandardItem("Все счета",   EXPORT_ID.ACCOUNT,   ROLES.IDO)])
		self.model_operations.appendRow([item_input, C20_StandardItem("")])

		item_output = C20_StandardItem("ПАРАМЕТРЫ ЭКСПОРТА")
		item_output.appendRow([C20_StandardItem("Директория данных", EXPORT_ID.DIRECTORY, ROLES.IDO), C20_StandardItem("",            EXPORT_ID.DIRECTORY, ROLES.IDO)])
		item_output.appendRow([C20_StandardItem("Имя файла",         EXPORT_ID.FILENAME,  ROLES.IDO), C20_StandardItem("",            EXPORT_ID.FILENAME,  ROLES.IDO)])
		self.model_operations.appendRow([item_output, C20_StandardItem("")])

	def LoadModelDataOperations(self):
		""" Загрузка данных в модель данных финансовых операций """
		indexes_data = self.model_operations.indexesInRowByIdo(EXPORT_ID.MODE_DATE)
		item_data    = self.model_operations.itemFromIndex(indexes_data[1])

		match self._operations_input_mode_date:
			case EXPORT_MODE_DATE.ALL: item_data.setText(f"Все периоды")
			case EXPORT_MODE_DATE.DY : item_data.setText(f"{self._operations_input_dy} год")
			case EXPORT_MODE_DATE.DM : item_data.setText(f"{MONTHS(self._operations_input_dm).name_s} {self._operations_input_dy}")

		indexes_data = self.model_operations.indexesInRowByIdo(EXPORT_ID.ACCOUNT)
		item_data    = self.model_operations.itemFromIndex(indexes_data[1])
		match self._operations_input_mode_account:
			case EXPORT_MODE_ACCOUNTS.ALL   :
				item_data.setText(f"Все счета")

			case EXPORT_MODE_ACCOUNTS.GROUP :
				item_data.setText(f"Группа счетов: {self._operations_input_account}")

			case EXPORT_MODE_ACCOUNTS.SINGLE:
				item_data.setText(f"{self._operations_input_account}")

		indexes_data = self.model_operations.indexesInRowByIdo(EXPORT_ID.DIRECTORY)
		item_data    = self.model_operations.itemFromIndex(indexes_data[1])
		item_data.setText(f"{self._operations_output_path.absolute()}")

		indexes_data = self.model_operations.indexesInRowByIdo(EXPORT_ID.FILENAME)
		item_data    = self.model_operations.itemFromIndex(indexes_data[1])
		item_data.setText('\n'.join(self._operations_output_files))

	# Параметры
	def ReadProcessingIdFromTreeDataOperations(self):
		""" Чтение ID из дерева Финансовые операции """
		current_index : QModelIndex = self.tree_data_operations.currentIndex()
		self._processing_ido = current_index.data(ROLES.IDO)

	def CalcOperationsOutputFiles(self):
		""" Расчёт списка файлов при экспорте """
		prefix_date : str        = ""
		dy          : int | None = self._operations_input_dy
		dm          : int | None = self._operations_input_dm

		match self._operations_input_mode_date:
			case EXPORT_MODE_DATE.ALL:
				prefix_date = ""
				dy          = None
				dm          = None

			case EXPORT_MODE_DATE.DY :
				prefix_date = f"{self._operations_input_dy}_"
				dm          = None

			case EXPORT_MODE_DATE.DM :
				prefix_date = f"{self._operations_input_dy}-{self._operations_input_dm:02d}_"

		accounts    : list[str]  = []

		match self._operations_input_mode_account:
			case EXPORT_MODE_ACCOUNTS.ALL:
				accounts = self.accounts.AccountsNamesInDyDm(dy, dm)

			case EXPORT_MODE_ACCOUNTS.GROUP:
				accounts = self.accounts.AccountsNamesInDyDm(dy, dm, self._operations_input_account)

			case EXPORT_MODE_ACCOUNTS.SINGLE:
				accounts.append(self._operations_input_account)

		self._operations_output_files = [f"{prefix_date}{account}.csv" for account in accounts]

# ФОРМА ЭКСПОРТ ДАННЫХ: ЛОГИКА ДАННЫХ
# 01 апр 2025

from itertools          import product
from pathlib            import Path

from PySide6.QtCore     import Qt
from PySide6.QtWidgets  import QProgressDialog

from G11_convertor_data import AmountToString

from L00_form_export    import ACCOUNTS, EXPORT_FIELDS, INTERVALS
from L70_form_export    import C70_FormExport
from L90_account        import C90_Account
from L90_operations     import C90_Operation


class C80_FormExport(C70_FormExport):
	""" Форма экспорт данных: Логика данных """

	# Экспорт операций
	def EditOptionsOperations(self):
		""" Редактирование параметров экспорта операций """

		match self.processing_field:
			case EXPORT_FIELDS.INTERVAL : self.on_RequestEditOperationsInterval()
			case EXPORT_FIELDS.ACCOUNTS : self.on_RequestEditOperationsAccounts()
			case EXPORT_FIELDS.DIRECTORY: self.on_RequestEditOperationsDirectory()

	def ExportOperations(self):
		""" Экспорт операций """
		account_names : list[str]  = []

		dy            : int | None = None
		dm            : int | None = None

		dys           : list[int]  = []
		dms           : list[int]  = []

		prefix        : str        = ""

		match self.operations_interval_mode:
			case INTERVALS.ALL:
				dy     = None
				dm     = None

				dys    = self.Accounts.AvailableDys()
				dms    = list(range(1, 13))

				prefix = ""

			case INTERVALS.DY :
				dy     = self.operations_interval_dy
				dm     = None

				dys    = [self.operations_interval_dy]
				dms    = list(range(1, 13))

				prefix = f"{self.operations_interval_dy}_"

			case INTERVALS.DM :
				dy     = self.operations_interval_dy
				dm     = self.operations_interval_dm

				dys    = [self.operations_interval_dy]
				dms    = [self.operations_interval_dm]

				prefix = f"{self.operations_interval_dy}-{self.operations_interval_dm:02d}_"


		match self.operations_accounts_mode:
			case ACCOUNTS.ALL    : account_names =  self.Accounts.Names(dy, dm)
			case ACCOUNTS.GROUP  : account_names =  self.Accounts.Names(dy, dm, self.operations_accounts_group)
			case ACCOUNTS.ACCOUNT: account_names = [self.operations_accounts_account]

		if not account_names: return

		count         : int        = 0

		for account_name in account_names:
			for dy, dm in product(dys, dms):
				account = C90_Account()
				if not account.SwitchByName(dy, dm, account_name): continue

				count += len(self.Operations.Idos(dy, dm, None, account.Ido().data))

		dialog_export    = QProgressDialog(self)
		dialog_export.setWindowTitle("Экспорт операций")
		dialog_export.setMaximum(count - 1)
		dialog_export.setWindowModality(Qt.WindowModality.WindowModal)
		dialog_export.setLabelText(f"Осталось обработать операций: {dialog_export.maximum()}")
		dialog_export.setMinimumWidth(480)
		dialog_export.forceShow()

		for account_name in account_names:
			data : list = []
			data.append(';'.join(["Дата", "Сумма", "Описание", "Назначение"]))

			for dy, dm in product(dys, dms):
				account = C90_Account()
				if not account.SwitchByName(dy, dm, account_name): continue

				for dd in range(31):
					for operation_ido in self.Operations.Idos(dy, dm, dd, account.Ido().data):
						dialog_export.setValue(dialog_export.value() + 1)
						dialog_export.setLabelText(f"Осталось обработать операций: {dialog_export.maximum() - dialog_export.value()}")

						operation = C90_Operation(operation_ido)
						subdata : list[str] = [operation.DdDmDyToString(),
						                       AmountToString(operation.amount, flag_point=True),
						                       operation.description,
						                       operation.destination,
						                       ]

						data.append(';'.join(subdata))

			filepath : Path = self.operations_directory / f"{prefix}{account_name}.csv"
			with open(filepath, "w") as file_data:
				file_data.write('\n'.join(data))

		dialog_export.close()

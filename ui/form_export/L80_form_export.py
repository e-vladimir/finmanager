# ФОРМА ЭКСПОРТ ДАННЫХ: ЛОГИКА ДАННЫХ

from   itertools              import product
from   pathlib                import Path

from   PySide6.QtCore         import Qt
from   PySide6.QtWidgets      import QProgressDialog

from   G30_cactus_datafilters import C30_FilterLinear1D

from   L00_containers         import CONTAINERS
from   L00_months             import MONTHS
from   L00_struct_export      import EXPORT_MODE_DATE, EXPORT_MODE_ACCOUNTS
from   L20_PySide6            import RequestDirectory, RequestItem, RequestText
from   L70_form_export        import C70_FormExport
from   L90_accounts           import C90_Account
from   L90_operations         import C90_Operation


class C80_FormExport(C70_FormExport):
	""" Форма Экспорт данных: Логика данных """

	# Экспорт Финансовых операций
	def SetDataInOperations(self):
		""" Изменение периода выборки данных """
		modes : list[str]  = []
		modes.append(EXPORT_MODE_DATE.ALL)
		modes.append(EXPORT_MODE_DATE.DY)
		modes.append(EXPORT_MODE_DATE.DM)

		mode  : str | None = RequestItem("Экспорт данных: Финансовые операции", "Период экспорта", modes)
		if mode is None: return

		self._operations_input_mode_date = EXPORT_MODE_DATE(mode)

		match self._operations_input_mode_date:
			case EXPORT_MODE_DATE.ALL:
				return

			case EXPORT_MODE_DATE.DY:
				dy : str | None = RequestText("Экспорт данных: Финансовые операции", "Год экспорта финансовых операций", f"{self._operations_input_dy}")

				if dy is None: return

				try   : self._operations_input_dy = int(dy)
				except: return

			case EXPORT_MODE_DATE.DM:
				dydm_raw: str | None = RequestText("Рабочий период", "Месяц экспорта финансовых операций: МЕС ГОД", f"{MONTHS(self._operations_input_dm).name_short} {self._operations_input_dy}")
				if dydm_raw is None: return

				try:
					dm_raw, dy_raw = dydm_raw.lower().split(' ')

					dy: int = int(dy_raw)
					dm: MONTHS = MONTHS.FindByNameS(dm_raw)
				except:
					return

				self._operations_input_dy = dy
				self._operations_input_dm = dm.code

	def SetAccountInOperations(self):
		""" Изменение счёта выборки данных """
		modes : list[str]  = []
		modes.append(EXPORT_MODE_ACCOUNTS.ALL)
		modes.append(EXPORT_MODE_ACCOUNTS.GROUP)
		modes.append(EXPORT_MODE_ACCOUNTS.SINGLE)

		mode  : str | None = RequestItem("Экспорт данных: Финансовые операции", "Экспорт счетов", modes)
		if mode is None: return

		match mode:
			case EXPORT_MODE_ACCOUNTS.ALL.value:
				self._operations_input_mode_account = EXPORT_MODE_ACCOUNTS.ALL

			case EXPORT_MODE_ACCOUNTS.GROUP.value:
				dy, dm             = self.workspace.DyDm()

				match self._operations_input_mode_date:
					case EXPORT_MODE_DATE.ALL:
						dy = None
						dm = None

					case EXPORT_MODE_DATE.DY:
						dm = None

				groups             = self.accounts.GroupsNamesInDyDm(dy, dm)
				if not groups       : return

				group : str | None = RequestItem("Экспорт данных: Финансовые операции", "Экспорт группы счетов", groups)
				if     group is None: return

				self._operations_input_mode_account = EXPORT_MODE_ACCOUNTS.GROUP
				self._operations_input_account      = group

			case EXPORT_MODE_ACCOUNTS.SINGLE.value:
				dy, dm            = self.workspace.DyDm()

				match self._operations_input_mode_date:
					case EXPORT_MODE_DATE.ALL:
						dy = None
						dm = None

					case EXPORT_MODE_DATE.DY:
						dm = None

				names             = self.accounts.AccountsNamesInDyDm(dy, dm)
				if not names       : return

				name : str | None = RequestItem("Экспорт данных: Финансовые операции", "Экспорт счета", names)
				if     name is None: return

				self._operations_input_mode_account = EXPORT_MODE_ACCOUNTS.SINGLE
				self._operations_input_account      = name

	def SetPathInOperations(self):
		""" Изменение директории экспорта """
		path : Path | None = RequestDirectory("Экспорт данных: Финансовые операции", f"{self._operations_output_path}")
		if path is None: return

		self._operations_output_path = path

	def ExportOperations(self):
		""" Выполнение экспорта данных """
		prefix_name   : str        = ""
		dy            : int | None = self._operations_input_dy
		dm            : int | None = self._operations_input_dm

		match self._operations_input_mode_date:
			case EXPORT_MODE_DATE.ALL:
				prefix_name = ""
				dy          = None
				dm          = None

			case EXPORT_MODE_DATE.DY :
				prefix_name = f"{self._operations_input_dy}_"
				dm          = None

			case EXPORT_MODE_DATE.DM :
				prefix_name = f"{self._operations_input_dy}-{self._operations_input_dm:02d}_"

		account_names : list[str]  = []

		match self._operations_input_mode_account:
			case EXPORT_MODE_ACCOUNTS.ALL:
				account_names = self.accounts.AccountsNamesInDyDm(dy, dm)

			case EXPORT_MODE_ACCOUNTS.GROUP:
				account_names = self.accounts.AccountsNamesInDyDm(dy, dm, self._operations_input_account)

			case EXPORT_MODE_ACCOUNTS.SINGLE:
				account_names = [self._operations_input_account]

		dys           : list[int]  = []
		dms           : list[int]  = []
		dds           : list[int]  = list(range(1, 32))

		match self._operations_input_mode_date:
			case EXPORT_MODE_DATE.ALL:
				operation   = C90_Operation()
				idc   : str = operation.Idc().data
				idp_dy: str = operation.f_dy.Idp().data

				filter_data = C30_FilterLinear1D(idc)
				filter_data.Capture(CONTAINERS.DISK)

				dys         = filter_data.ToIntegers(idp_dy, True, True).data
				dms         = list(range(1, 13))

			case EXPORT_MODE_DATE.DY :
				dys = [self._operations_input_dy]
				dms = list(range(1, 13))

			case EXPORT_MODE_DATE.DM :
				dys = [self._operations_input_dy]
				dms = [self._operations_input_dm]

		dialog_export              = QProgressDialog(self)
		dialog_export.setWindowTitle("Экспорт финансовых операций")
		dialog_export.setMaximum(len(account_names))
		dialog_export.setWindowModality(Qt.WindowModality.WindowModal)
		dialog_export.setLabelText(f"Осталось обработать: {dialog_export.maximum()} счетов")
		dialog_export.setMinimumWidth(480)

		for index_data, account_name in enumerate(account_names):
			dialog_export.setValue(index_data + 1)
			dialog_export.setLabelText(f"Осталось обработать: {dialog_export.maximum() - dialog_export.value()} счетов")

			file_name : str       = f"{prefix_name}{account_name}.csv"
			file_path : Path      = self._operations_output_path.joinpath(file_name)
			file_data : list[str] = []

			for dy, dm in product(dys, dms):
				account           = C90_Account()
				if not account.SwitchByNameInDyDm(dy, dm, account_name): continue

				ido_account : str = account.Ido().data

				for dd in dds:
					idos_operations : list[str] = self.operations.OperationsIdosInDyDmDd(dy, dm, dd)

					for ido_operation in idos_operations:
						operation           = C90_Operation(ido_operation)

						if ido_account not in operation.AccountsIdos(): continue

						subdata : list[str] = []
						subdata.append(f"{operation.Dy():04d}-{operation.Dm():02d}-{operation.Dd():02d}")
						subdata.append(f"{operation.Amount():0.2f}".replace('.', ','))
						subdata.append(f"{operation.Description()}")
						subdata.append(f"{operation.Destination()}")
						subdata.append(', '.join(operation.Labels()))

						file_data.append(';'.join(subdata) + ';')

			if not file_data: continue

			file_data.insert(0, "Дата;Сумма;Описание;Назначение;Метки")

			with open(file_path, "w") as file_account: file_account.write('\n'.join(file_data))

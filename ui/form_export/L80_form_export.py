# ФОРМА ЭКСПОРТ ДАННЫХ: ЛОГИКА ДАННЫХ

from pathlib           import Path

from L00_months        import MONTHS
from L00_struct_export import EXPORT_MODE_DATE, EXPORT_MODE_ACCOUNTS
from L20_PySide6       import RequestDirectory, RequestItem, RequestText
from L70_form_export   import C70_FormExport


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
				dydm_raw: str | None = RequestText("Рабочий период", "Месяц экспорта финансовых операций: МЕС ГОД", f"{MONTHS(self._operations_input_dm).name_s} {self._operations_input_dy}")
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
		print("Export")

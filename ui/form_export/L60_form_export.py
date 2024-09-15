# ФОРМА ЭКСПОРТ ДАННЫХ: МЕХАНИКА ДАННЫХ

from pathlib           import Path

from PySide6.QtCore    import QModelIndex
from PySide6.QtWidgets import QFileDialog

from L00_months        import MONTHS_SHORT
from L00_options       import OPTIONS
from L20_PySide6 import RequestItem, RequestItems
from L50_form_export   import C50_FormExport


class C60_FormExport(C50_FormExport):
	""" Форма Экспорт данных: Механика данных """

	# Параметры
	def ReadProcessingRowFromTableFinactionsData(self):
		""" Чтение строки из таблицы данных финдействий """
		current_index : QModelIndex = self.table_finactions_data.currentIndex()
		self._processing_row = current_index.row()

	def SetOptionsFinactionsPeriodMode(self):
		""" Установка параметра экспорта финдействий: Режим периода """
		modes : list[str]  = [OPTIONS.MODE_ALL, OPTIONS.MODE_DM, OPTIONS.MODE_DY]
		mode  : str | None = RequestItem("Экспорт финдействий", "Период экспорта финдействий", modes)
		if mode is None: return

		self._options_finactions_period_mode = OPTIONS(mode)

	def SetOptionsFinactionsPeriodDm(self):
		""" Установка параметра экспорта финдействий: Месяц """
		dms : list[str]  = MONTHS_SHORT[1:]
		dm  : str | None = RequestItem("Экспорт финдействий", "Экспорт за месяц", dms)
		if dm is None: return

		self._options_finactions_period_dm = MONTHS_SHORT.index(dm)

	def SetOptionsFinactionsPeriodDy(self):
		""" Установка параметра экспорта финдействий: Месяц """
		dys : list[str]  = [str(dy) for dy in self.workspace.AvailableDys()]
		dy  : str | None = RequestItem("Экспорт финдействий", "Экспорт за год", dys)
		if dy is None: return

		self._options_finactions_period_dy = int(dy)

	def SetOptionsFinactionsFinstructMode(self):
		""" Установка параметра экспорта финдействий: Режим финструктуры """
		modes : list[str]  = [OPTIONS.MODE_ALL, OPTIONS.MODE_SELECT]
		mode  : str | None = RequestItem("Экспорт финдействий", "Экспорт финдействий по счёту", modes)
		if mode is None: return

		self._options_finactions_finstruct_mode = OPTIONS(mode)

	def SetOptionsFinactionsFinstructNames(self):
		""" Установка параметра экспорта финдействий: Счёт/Счета """
		dy, dm             = self.workspace.DyDm()
		names : list[str]  = []

		match self._options_finactions_period_mode:
			case OPTIONS.MODE_ALL: names: list[str] = self.finstruct.Names()
			case OPTIONS.MODE_DY : names: list[str] = self.finstruct.NamesInDyDm(dy)
			case OPTIONS.MODE_DM : names: list[str] = self.finstruct.NamesInDyDm(dy, dm)

		names  : list[str] | None = RequestItems("Экспорт финдействий", "Список счетов", names)

		if names is None: return

		self._options_finactions_finstruct_names = names

	def SetOptionsFinactionsFolder(self):
		""" Установка параметра экспорта финдействий: Директория экспорта """
		dialog_folder = QFileDialog(self)
		folder : str  =  dialog_folder.getExistingDirectory(self, "Экспорт финдействий", f"{self._options_finactions_folder}")

		if not folder: return

		self._options_finactions_folder = Path(folder)

	def CalcOptionsFinactionsFilenames(self):
		""" Формирование списка файлов """
		self._options_finactions_filenames.clear()

		dy                    = self._options_finactions_period_dy
		dm                    = self._options_finactions_period_dm
		filenames : list[str] = []

		match self._options_finactions_finstruct_mode:
			case OPTIONS.MODE_SELECT:
				filenames.extend(self._options_finactions_finstruct_names)

			case OPTIONS.MODE_ALL:
				match self._options_finactions_period_mode:
					case OPTIONS.MODE_ALL: filenames.extend(self.finstruct.Names())
					case OPTIONS.MODE_DY : filenames.extend(self.finstruct.NamesInDyDm(dy))
					case OPTIONS.MODE_DM : filenames.extend(self.finstruct.NamesInDyDm(dy, dm))

		prefix  : str = ""
		postfix : str = ".csv"

		match self._options_finactions_period_mode:
			case OPTIONS.MODE_DM: prefix = f"{self._options_finactions_period_dy} {MONTHS_SHORT[self._options_finactions_period_dm]} - "
			case OPTIONS.MODE_DY: prefix = f"{self._options_finactions_period_dy} - "

		for filename in filenames:
			if not filename: continue

			self._options_finactions_filenames.append(f"{prefix}{filename}{postfix}")

	# Модель финдействий
	def InitModelFinactions(self):
		""" Инициализация модели финдействий """
		self.model_finactions.removeAll()

		self.model_finactions.fastAppendRow(["ПЕРИОД", ""])       # 0
		self.model_finactions.fastAppendRow(["Режим выборки", ""])
		self.model_finactions.fastAppendRow(["Год", ""])
		self.model_finactions.fastAppendRow(["Месяц", ""])
		self.model_finactions.fastAppendRow(["", ""])

		self.model_finactions.fastAppendRow(["СЧЁТ", ""])         # 5
		self.model_finactions.fastAppendRow(["Режим выборки", ""])
		self.model_finactions.fastAppendRow(["Счёт/Счета", ""])
		self.model_finactions.fastAppendRow(["", ""])

		self.model_finactions.fastAppendRow(["ПАРАМЕТРЫ", ""])    # 9
		self.model_finactions.fastAppendRow(["Директория", ""])
		self.model_finactions.fastAppendRow(["Имя файла/файлов", ""])

	def LoadModelFinactions(self):
		""" Загрузка модели финдействий """
		item_data = self.model_finactions.item(1, 1)
		match self._options_finactions_period_mode:
			case OPTIONS.MODE_ALL: item_data.setText("Все периоды")
			case OPTIONS.MODE_DM : item_data.setText("Месяц")
			case OPTIONS.MODE_DY : item_data.setText("Год")

		item_data = self.model_finactions.item(2, 1)
		item_data.setText(f"{self._options_finactions_period_dy}")

		item_data = self.model_finactions.item(3, 1)
		item_data.setText(MONTHS_SHORT[self._options_finactions_period_dm])

		item_data = self.model_finactions.item(6, 1)
		match self._options_finactions_finstruct_mode:
			case OPTIONS.MODE_ALL   : item_data.setText("Все счета")
			case OPTIONS.MODE_SELECT: item_data.setText("Выбранный счёт")

		item_data = self.model_finactions.item(7, 1)
		item_data.setText('\n'.join(self._options_finactions_finstruct_names))

		item_data = self.model_finactions.item(10, 1)
		item_data.setText(f"{self._options_finactions_folder.absolute()}")

		item_data = self.model_finactions.item(11, 1)
		item_data.setText('\n'.join(self._options_finactions_filenames))

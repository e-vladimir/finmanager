# ФОРМА ИМПОРТ ДАННЫХ: МЕХАНИКА ДАННЫХ

import pyexcel
from PySide6.QtCore import QModelIndex

from   G10_convertor_format import AnyToStrings
from   L50_form_import      import C50_FormImport


class C60_FormImport(C50_FormImport):
	""" Форма Импорт данных: Механика данных """

	# Параметры
	def ReadImportFinactionsRawData(self):
		""" Чтение исходных данных финдействий из файла """
		self._import_finactions_data.clear()

		if not self._import_finactions_filepath.is_file(): return
		if not self._import_finactions_filepath.exists() : return

		file_ext : str = f"{self._import_finactions_filepath.name}".lower().split('.')[-1]
		if file_ext not in ["csv", "xls", "xlsx"]: return

		data : pyexcel.sheet.Sheet | None = None

		match file_ext:
			case "csv" :
				encodings : list[str] = ["utf-8", "cp1251"]

				for encoding in encodings:
					try   :
						data = data = pyexcel.get_sheet(file_name = f"{self._import_finactions_filepath}", encoding=encoding, delimiter=';')
						break
					except: pass

			case "xls" :
				try    : data = pyexcel.get_sheet(file_name = f"{self._import_finactions_filepath}")
				except : pass

			case "xlsx":
				try    : data = pyexcel.get_sheet(file_name = f"{self._import_finactions_filepath}")
				except : pass

		if data is None: return

		self._import_finactions_data = [AnyToStrings(list(subdata)) for subdata in data.rows()]

	def ReadProcessingColumnFromTableImportFinactionsData(self):
		""" Чтение индекса колонки из таблицы данных импорта финдействий """
		current_index : QModelIndex = self.table_import_finactions_data.currentIndex()

		self._processing_column = current_index.column()

	def ReadProcessingNameFromTableImportFinactionsData(self):
		""" Чтение наименования из таблицы данных импорта финдействий """
		self._processing_name = ""

		current_index : QModelIndex = self.table_import_finactions_data.currentIndex()
		if not current_index.isValid()     : return

		if not self._import_finactions_data: return

		try   : self._processing_name = self._import_finactions_data[0][current_index.column()]
		except: pass

	# Модель данных импорта финдействий
	def LoadModelImportFinactionsData(self):
		""" Загрузка данных модели импорта финдействий """
		self.model_import_finactions_data.removeAll()

		if not self._import_finactions_data: return

		for subdata in self._import_finactions_data[1:21]:
			self.model_import_finactions_data.fastAppendRow(subdata)

		header : list[str] = ['' for _ in range(self.model_import_finactions_data.columnCount())]

		for index_col, field in self._import_finactions_header.items():
			header[index_col] = field.value

		self.model_import_finactions_data.setHorizontalHeaderLabels(header)

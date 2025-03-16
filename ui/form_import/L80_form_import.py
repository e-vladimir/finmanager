# ФОРМА ИМПОРТ ДАННЫХ: ЛОГИКА ДАННЫХ
# 14 мар 2025

import pyexcel

from   pathlib         import Path

from   L20_PySide6     import RequestFilepath
from   L70_form_import import C70_FormImport


class C80_FormImport(C70_FormImport):
	""" Форма Импорт данных: Логика данных """

	# Данные импорта операций
	def LoadOperationsDataFromFile(self):
		""" Загрузка данных импорта операций из файла """
		filepath : Path | None = RequestFilepath("Импорт операций", "", "Поддерживаемые форматы (*.csv *.ods *.xls *.xlsx)")
		if     filepath is None : return
		if     filepath.is_dir(): return
		if not filepath.exists(): return

		self.operations_filepath = filepath

		raw : list[list[str]] = []

		match filepath.suffix:
			case ".csv" :
				for encoding in ["utf-8", "cp1251"]:
					try:
						with open(self.operations_filepath, mode='r', encoding=encoding) as file_data:
							raw = [subdata.strip().split(';') for subdata in file_data.readlines()]
					except:
						pass

			case ".ods" :
				try   : raw = [[str(item) for item in subdata] for subdata in pyexcel.get_sheet(file_name=f"{self.operations_filepath}").rows()]
				except: pass

			case ".xls" :
				try   : raw = [[str(item) for item in subdata] for subdata in pyexcel.get_sheet(file_name=f"{self.operations_filepath}").rows()]
				except: pass
				
			case ".xlsx":
				try   : raw = [[str(item) for item in subdata] for subdata in pyexcel.get_sheet(file_name=f"{self.operations_filepath}").rows()]
				except: pass

		if not raw: return

		self.operations_struct = raw[0]
		self.operations_data   = raw[1:]

		self.on_OperationsDataLoaded()

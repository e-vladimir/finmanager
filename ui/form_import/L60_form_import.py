# ФОРМА ИМПОРТ ДАННЫХ: МЕХАНИКА ДАННЫХ

import pyexcel

from   L50_form_import   import C50_FormImport


class C60_FormImport(C50_FormImport):
	""" Форма Импорт данных: Механика данных """

	# Параметры
	def ReadImportFinactionsRawData(self):
		""" Чтение исходных данных финдействий из файла """
		self._import_finactions_raw_data.clear()

		if not self._import_finactions_filepath.is_file(): return
		if not self._import_finactions_filepath.exists() : return

		file_ext : str = f"{self._import_finactions_filepath.name}".lower().split('.')[-1]

		data     : str = ""

		match file_ext:
			case "csv":
				encodings : list[str] = ["utf-8", "cp1251"]

				for encoding in encodings:
					try:
						with open(f"{self._import_finactions_filepath}", "rt", encoding=encoding) as file_data:
							raw_data = file_data.read()
							data = raw_data.replace('"', '')
					except:
						pass

			case "xls":
				for raw_data in pyexcel.iget_records(file_name = f"{self._import_finactions_filepath}"):
					print(raw_data)

			case "xlsx":
				for raw_data in pyexcel.iget_records(file_name = f"{self._import_finactions_filepath}"):
					print(raw_data)

			case _: return

		self._import_finactions_raw_data = data.split('\n')

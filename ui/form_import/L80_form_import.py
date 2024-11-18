# ФОРМА ИМПОРТ ДАННЫХ: ЛОГИКА ДАННЫХ

import pyexcel

from   L70_form_import import C70_FormImport


class C80_FormImport(C70_FormImport):
	""" Форма Импорт данных: Логика данных """

	# Данные импорта финансовых операций
	def ProcessingFileForOperations(self):
		""" Обработка файла для импорта финансовых операций """
		if self._operations_file is None: return

		file_ext : str                        = f"{self._operations_file.name}".lower().split('.')[-1]
		if file_ext not in ["csv", "xls", "xlsx", "ods"]: return

		data     : pyexcel.sheet.Sheet | None = None

		match file_ext:
			case "csv" :
				encodings : list[str] = ["utf-8", "cp1251"]

				for encoding in encodings:
					try   :
						data = pyexcel.get_sheet(file_name = f"{self._operations_file}", encoding=encoding, delimiter=';')
						break
					except: pass

			case "xls" :
				try    : data = pyexcel.get_sheet(file_name = f"{self._operations_file}")
				except : pass

			case "xlsx":
				try    : data = pyexcel.get_sheet(file_name = f"{self._operations_file}")
				except : pass

			case "ods" :
				try    : data = pyexcel.get_sheet(file_name = f"{self._operations_file}")
				except : pass

		if data is None: return

		self._operations_data.clear()

		for index_raw, subdata in enumerate(data.rows()):
			if index_raw == 0: self._operations_header = [str(item) for item in list(subdata)]
			else             : self._operations_data.append([str(item) for item in list(subdata)])

		self._operations_options = [""] * len(self._operations_header)

	def SetFieldForHeaderOperations(self):
		"""  """
		pass

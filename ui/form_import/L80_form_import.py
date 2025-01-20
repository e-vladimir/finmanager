# ФОРМА ИМПОРТ ДАННЫХ: ЛОГИКА ДАННЫХ

import pyexcel

from   datetime             import datetime

from   PySide6.QtCore       import Qt
from   PySide6.QtWidgets    import QProgressDialog

from   G10_convertor_format import StringToFloat, StringToDateTime

from   L00_fields           import FIELDS
from   L20_PySide6          import RequestItem, RequestText
from   L70_form_import      import C70_FormImport
from   L90_accounts         import C90_Account


class C80_FormImport(C70_FormImport):
	""" Форма Импорт данных: Логика данных """

	# Данные импорта финансовых операций
	def ProcessingFileInOperations(self):
		""" Обработка файла """
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

		self._operations_fields = [""] * len(self._operations_header)

	def SetFieldInOperations(self):
		""" Установка типа данных """
		if self._operations_processing_row < 0: return

		try   : header_item = self._operations_header[self._operations_processing_row]
		except: header_item = ""

		try   : type_item   = self._operations_fields[self._operations_processing_row]
		except: type_item   = ""

		fields : list[str]  = list(sorted([field.value for field in FIELDS]))

		field  : str | None = RequestItem("Импорт данных: Операции", header_item, fields)
		if field is None: return

		self._operations_fields[self._operations_processing_row] = FIELDS(field)

	def ImportOperations(self):
		""" Импорт финансовых операций """
		index_date        : int        = -1
		index_amount      : int        = -1
		index_description : int        = -1
		index_destination : int        = -1
		index_object_int  : int        = -1
		index_object_ext  : int        = -1

		for index_field, field in enumerate(self._operations_fields):
			match field:
				case FIELDS.AMOUNT      : index_amount      = index_field
				case FIELDS.DATE        : index_date        = index_field
				case FIELDS.DESCRIPTION : index_description = index_field
				case FIELDS.DESTINATION : index_destination = index_field
				case FIELDS.OBJECT_INT  : index_object_int  = index_field
				case FIELDS.OBJECT_EXT  : index_object_ext  = index_field

		if     index_date        == -1                         : return
		if     index_amount      == -1                         : return

		dy, dm = self.workspace.DyDm()

		account_names     : list[str]  = self.accounts.AccountsNamesInDyDm(dy, dm)
		account_name      : str | None = RequestText("Импорт финансовых операций", "Счёт импорта операций", "", account_names)
		if     account_name is None                            : return

		account                        = C90_Account()
		if not account.SwitchByNameInDyDm(dy, dm, account_name): return

		account_ido       : str        = account.Ido().data

		dialog_import                  = QProgressDialog(self)
		dialog_import.setWindowTitle("Импорт финансовых операций")
		dialog_import.setMaximum(len(self._operations_data))
		dialog_import.setWindowModality(Qt.WindowModality.WindowModal)
		dialog_import.setLabelText(f"Осталось обработать: {dialog_import.maximum()} записей")
		dialog_import.setMinimumWidth(480)
		dialog_import.forceShow()

		for index_data, data in enumerate(self._operations_data):
			dialog_import.setValue(index_data + 1)
			dialog_import.setLabelText(f"Осталось обработать: {dialog_import.maximum() - dialog_import.value()} записей")

			raw_date        : str             = data[index_date]
			raw_amount      : str             = data[index_amount]
			raw_description : str             = "" if index_description == -1 else data[index_description]
			raw_destination : str             = "" if index_destination == -1 else data[index_destination]
			raw_object_int  : str             = "" if index_object_int  == -1 else data[index_object_int]
			raw_object_ext  : str             = "" if index_object_ext  == -1 else data[index_object_ext]

			date            : datetime | None = StringToDateTime(raw_date)
			if     date is None             : continue

			try   : amount = StringToFloat(raw_amount)
			except: continue

			description     : str             = raw_description
			destination     : str             = raw_destination.replace(', ', ',').split(',')

			dy              : int             = date.year
			dm              : int             = date.month
			dd              : int             = date.day

			if not dy == self.workspace.Dy(): continue
			if not dm == self.workspace.Dm(): continue

			data = dict()
			data[FIELDS.AMOUNT]      = amount
			data[FIELDS.DESCRIPTION] = description
			data[FIELDS.DESTINATION] = destination
			data[FIELDS.OBJECT_INT]  = raw_object_int
			data[FIELDS.OBJECT_EXT]  = raw_object_ext

			self.operations.ImportOperation(dy, dm, dd, account_ido, data)

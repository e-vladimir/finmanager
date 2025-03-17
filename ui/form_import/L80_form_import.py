# ФОРМА ИМПОРТ ДАННЫХ: ЛОГИКА ДАННЫХ
# 14 мар 2025

import datetime
import pyexcel

from   pathlib              import Path
from   PySide6.QtCore       import Qt
from   PySide6.QtWidgets    import QProgressDialog

from   G10_convertor_format import StringToDateTime, StringToFloat

from   L00_containers       import CONTAINERS
from   L00_fields           import FIELDS
from   L20_PySide6          import RequestFilepath, RequestItem
from   L70_form_import      import C70_FormImport
from   L90_account          import C90_Account, C90_Accounts
from   L90_operations       import C90_Operation


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
				for encoding in ["cp1251", "utf-8"]:
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

		self.operations_struct_names = raw[0][:]
		self.operations_data         = raw[1:]

		self.on_OperationsDataLoaded()

	def EditOperationsStructField(self):
		""" Редактирование типа поля структуры данных импорта операций """
		struct_name  : str        = self.operations_struct_names[self.processing_row]
		struct_field : str | None = RequestItem("Импорт операций", f"{struct_name}", [field.value for field in FIELDS])
		if struct_field is None: return

		self.SetOperationsStructField(struct_name, FIELDS(struct_field))

		self.on_OperationsStructChanged()

	def ImportOperations(self):
		""" Импорт операций """
		dy, dm                         = self.Workspace.DyDm()

		idx_date        : int        = self.IndexOperationsStructByField(FIELDS.DATE)
		idx_amount      : int        = self.IndexOperationsStructByField(FIELDS.AMOUNT)
		idx_description : int        = self.IndexOperationsStructByField(FIELDS.DESCRIPTION)

		if     idx_date   == -1                        : return
		if     idx_amount == -1                        : return

		account_name      : str | None = RequestItem( "Импорт операций",
		                                             f"Период импорта: {self.Workspace.DmDyToString()}",
		                                              C90_Accounts.Names(dy, dm)
		                                             )
		if     account_name is None                      : return

		account                        = C90_Account()
		if not account.SwitchByName(dy, dm, account_name): return

		account_ido       : str        = account.Ido().data

		dialog_import                  = QProgressDialog(self)
		dialog_import.setWindowTitle("Импорт финансовых операций")
		dialog_import.setMaximum(len(self.operations_data))
		dialog_import.setWindowModality(Qt.WindowModality.WindowModal)
		dialog_import.setLabelText(f"Осталось обработать записей: {dialog_import.maximum()}")
		dialog_import.setMinimumWidth(480)
		dialog_import.forceShow()

		for idx_data, data in enumerate(self.operations_data):
			dialog_import.setValue(idx_data + 1)
			dialog_import.setLabelText(f"Осталось обработать записей: {dialog_import.maximum() - dialog_import.value()}")

			try:
				amount      : float             = StringToFloat(data[idx_amount])
				date        : datetime.datetime = StringToDateTime(data[idx_date])
				description : str               = data[idx_description]
			except: continue

			if not date.year  == dy: continue
			if not date.month == dm: continue

			operation              = C90_Operation()
			operation.GenerateIdo()
			operation.RegisterObject(CONTAINERS.DISK)

			operation.dy           = dy
			operation.dm           = dm
			operation.dd           = date.day
			operation.amount       = amount
			operation.description  = description
			operation.account_idos = [account_ido]

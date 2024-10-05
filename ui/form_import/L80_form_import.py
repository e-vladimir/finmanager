# ФОРМА ИМПОРТ ДАННЫХ: ЛОГИКА ДАННЫХ

from pathlib           import Path

from PySide6.QtCore    import Qt
from PySide6.QtWidgets import QFileDialog, QProgressDialog

from L00_fields        import FIELDS
from L20_PySide6       import RequestItem, ShowMessage
from L70_form_import   import C70_FormImport
from L90_finstructs    import C90_FinstructRecord


class C80_FormImport(C70_FormImport):
	""" Форма Импорт данных: Логика данных """

	# Импорт финдействий: Выбор файла
	def OpenLocalFileImportFinactions(self):
		""" Открытие локального файла для импорта финдействий """
		dialog              = QFileDialog()
		file_name, file_ext = dialog.getOpenFileName(self, "Импорт финдействий", f"{self._import_finactions_filepath.parent}")
		if not file_name: return

		self._import_finactions_filepath = Path(file_name)

		self.ReadImportFinactionsRawData()

	# Данные импорта финдействий
	def SetFieldImportFinactionsHeader(self):
		""" Установка типа поля колонки данных импорта финдействий """
		field_types : list[str]  = []
		field_types.append(FIELDS.DATE_TIME)
		field_types.append(FIELDS.AMOUNT)
		field_types.append(FIELDS.DESCRIPTION)
		field_types.append(FIELDS.CONTROL)

		field_type  : str | None = RequestItem("Импорт финдействий", f"Колонка: {self._processing_name}", field_types)
		if field_type is None: return

		self._import_finactions_header[self._processing_column] = FIELDS(field_type)

	def ResetFieldImportFinactionsHeader(self):
		""" Сброс типа поля колонки данных импорта финдействий """
		try   : del self._import_finactions_header[self._processing_column]
		except: pass

	def ExecImportFinactions(self):
		""" Выполнение импорта финдействий """
		dy, dm                      = self.workspace.DyDm()

		finstruct_name : str | None = RequestItem("Импорт финдействий", "Счёт импорта", self.finstruct.NamesInDyDm(dy, dm))
		if finstruct_name is None: return

		finstruct_record            = C90_FinstructRecord()
		if not finstruct_record.SwitchByName(dy, dm, finstruct_name): return

		finstruct_ido  : str        = finstruct_record.Ido().data

		dialog_progress             = QProgressDialog(self)
		dialog_progress.setWindowModality(Qt.WindowModality.WindowModal)
		dialog_progress.setMaximum(len(self._import_finactions_data))
		dialog_progress.setMinimumWidth(480)
		dialog_progress.setWindowTitle("Импорт финдействий")

		for index_row, row_data in enumerate(self._import_finactions_data[1:]):
			dialog_progress.setLabelText(f"Ожидает обработки: {dialog_progress.maximum() - dialog_progress.value()}")
			dialog_progress.setValue(index_row + 1)

			src_date_time   : str = ""
			src_amount      : str = ""
			src_description : str = ""
			src_control     : str = ""

			for index_col, field in self._import_finactions_header.items():
				match field:
					case FIELDS.DATE_TIME   : src_date_time    = row_data[index_col]
					case FIELDS.AMOUNT      : src_amount       = row_data[index_col]
					case FIELDS.DESCRIPTION : src_description += row_data[index_col] + ' '
					case FIELDS.CONTROL     : src_control      = row_data[index_col]

			self.finactions.ImportRecord(finstruct_ido, src_date_time, src_amount, src_description, src_control, dy, dm)

		dialog_progress.setValue(dialog_progress.maximum())

		ShowMessage("Импорт финдействий", "Импорт завершён")

		self.application.form_finactions.UpdateData()

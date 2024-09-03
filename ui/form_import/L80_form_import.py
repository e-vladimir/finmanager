# ФОРМА ИМПОРТ ДАННЫХ: ЛОГИКА ДАННЫХ

from pathlib           import Path

from PySide6.QtWidgets import QFileDialog

from L00_fields        import FIELDS
from L20_PySide6       import RequestItem
from L70_form_import   import C70_FormImport


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

	# Таблица данных импорта финдействий
	def SetFieldImportFinactionsHeader(self):
		""" Установка типа поля колонки данных импорта финдействий """
		field_types : list[str]  = []
		field_types.append(FIELDS.DATE_TIME)
		field_types.append(FIELDS.AMOUNT)
		field_types.append(FIELDS.NOTE)
		field_types.append(FIELDS.CONTROL)

		field_type  : str | None = RequestItem("Импорт финдействий", f"Колонка: {self._processing_name}", field_types)
		if field_type is None: return

		self._import_finactions_header[self._processing_column] = FIELDS(field_type)

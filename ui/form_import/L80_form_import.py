# ФОРМА ИМПОРТ ДАННЫХ: ЛОГИКА ДАННЫХ

from pathlib import Path

from PySide6.QtWidgets import QFileDialog

from L70_form_import   import C70_FormImport


class C80_FormImport(C70_FormImport):
	""" Форма Импорт данных: Логика данных """

	def OpenLocalFileImportFinactions(self):
		""" Открытие локального файла для импорта финдействий """
		dialog              = QFileDialog()
		file_name, file_ext = dialog.getOpenFileName(self, "Импорт финдействий", f"{self._import_finactions_filepath.parent}")
		if not file_name: return

		self._import_finactions_filepath = Path(file_name)

		self.ReadImportFinactionsRawData()

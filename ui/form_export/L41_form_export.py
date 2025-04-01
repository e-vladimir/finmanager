# ФОРМА ЭКСПОРТ ДАННЫХ: МОДЕЛЬ UI
# 01 апр 2025

from L20_PySide6     import C20_PySideForm
from L40_form_export import Ui_FormExport


class C41_FormExport(Ui_FormExport, C20_PySideForm):
	""" Форма экспорт данных: Модель UI """

	def InitUi(self): self.setupUi(self)

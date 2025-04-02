# ФОРМА ЭКСПОРТ ДАННЫХ: ЛОГИКА УПРАВЛЕНИЯ
# 01 апр 2025

from L80_form_export import C80_FormExport


class C90_FormExport(C80_FormExport):
	""" Форма экспорт данных: Логика управления """

	def on_Opened(self):
		self.InitModelDataOperations()
		self.LoadModelDataOperations()

		self.AdjustTreeDataOperationsColor()
		self.AdjustTreeDataOperationsExpand()
		self.AdjustTreeDataOperationsSize()

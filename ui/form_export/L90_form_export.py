# ФОРМА ЭКСПОРТ ДАННЫХ: ЛОГИКА УПРАВЛЕНИЯ
# 01 апр 2025

from L80_form_export import C80_FormExport


class C90_FormExport(C80_FormExport):
	""" Форма экспорт данных: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Дерево данных экспорта операций
		self.TreeDataOperations.doubleClicked.connect(self.on_RequestEditOptionsOperations)

	# Форма
	def on_Opened(self):
		self.InitModelDataOperations()
		self.LoadModelDataOperations()

		self.AdjustTreeDataOperationsColor()
		self.AdjustTreeDataOperationsExpand()
		self.AdjustTreeDataOperationsSize()

	# Парамеры экспорта операций
	def on_RequestEditOptionsOperations(self):
		""" Запрос редактирования параметров экспорта операций """
		self.ReadProcessingFieldFromTreeDataOperations()
		self.EditOptionsOperations()

	def on_OptionsOperationsChanged(self):
		""" Параметры экспорта операций изменились """
		self.LoadModelDataOperations()

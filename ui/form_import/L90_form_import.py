# ФОРМА ИМПОРТ ДАННЫХ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_import import C80_FormImport


class C90_FormImport(C80_FormImport):
	""" Форма Импорт данных: Логика управления """

	def on_Open(self):
		""" Открытие формы """
		self.ShowTitle()

		self.InitModelOperations()
		self.LoadOperationsHeader()
		self.LoadOperationsOptions()
		self.LoadOperationsData()

		self.AdjustTableOperations_Size()

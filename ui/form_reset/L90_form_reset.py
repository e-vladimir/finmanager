# ФОРМА СБРОС ДАННЫХ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_reset import C80_FormReset


class C90_FormReset(C80_FormReset):
	""" Форма Сброс данных: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Панель управления
		self.btn_exec_delete.clicked.connect(self.on_RequestProcessingReset)

	# Форма
	def on_Open(self):
		""" Открытие формы """
		self.ShowTitle()

		self.SetupModelObjects()
		self.LoadModelObjects()

		self.SetupExpandTreObjects()
		self.SetupCheckedModelObjects()

	# Панель управления
	def on_RequestProcessingReset(self):
		""" Запрос на очистку данных """
		self.ReadFlagAllPeriods()
		self.ReadFlagObjects()

		self.ReadOidsFinstruct()
		self.ReadOidsFinactions()
		self.ReadOidsFindescription()
		self.ReadOidsFindescriptionInFinactions()
		self.ReadOidsFinstate()
		self.ReadOidsFindata()
		self.ReadOidsRules()

		self.ProcessingReset()

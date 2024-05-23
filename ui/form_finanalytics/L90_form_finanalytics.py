# ФОРМА ФИНАНАЛИЗ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_finanalytics import C80_FormFinanalytics


class C90_FormFinanalytics(C80_FormFinanalytics):
	""" Форма Финанализ: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Таблица динамики финсостава
		self.table_findescription_dynamic.customContextMenuRequested.connect(self.on_RequestShowMenuFindescriptionDynamic)

		# Меню динамики финсостава
		self.menu_findescription_dynamic_inc.triggered.connect(self.on_RequestIncFindescriptionDynamic)
		self.menu_findescription_dynamic_record_dec.triggered.connect(self.on_RequestDecFindescriptionDynamic)

	def on_Open(self):
		super().on_Open()

		self.ShowTitle()

		self.on_RequestShowFindescriptionDynamic()

	def on_Resize(self):
		""" Размеры окна изменились """
		self.AdjustTableFindescriptionDynamicSize()

	# Модель динамики финсостава
	def on_RequestShowFindescriptionDynamic(self):
		""" Запрос отображения динамики финсостава """
		self.CalcDataFindescriptionDynamic()

		self.SetupModelFindescriptionDynamic()

		self.LoadModelFindescriptionDynamicIncome()
		self.LoadModelFindescriptionDynamicSeparator()
		self.LoadModelFindescriptionDynamicOutcome()

		self.AdjustTableFindescriptionDynamicSpan()
		self.AdjustTableFindescriptionDynamicColor()
		self.AdjustTableFindescriptionDynamicSize()
		self.AdjustTableFindescriptionDynamicAlign()

	def on_RequestIncFindescriptionDynamic(self):
		""" Запрос на расширение анализа финсостава """
		self.IncFindescriptionDynamic()

	def on_RequestDecFindescriptionDynamic(self):
		""" Запрос на исключение из динамики финсостава """
		self.DecFindescriptionDynamic()

	# Меню динамики финсостава
	def on_RequestShowMenuFindescriptionDynamic(self):
		""" Запрос вызова меню динамики финсостава """
		self.ReadOidProcessingFromTableFindescriptionDynamic()

		self.AdjustMenuFindescriptionText()
		self.AdjustMenuFindescriptionEnable()

		self.ShowMenuFindescriptionDynamic()

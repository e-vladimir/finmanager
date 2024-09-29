# ФОРМА ФИНАНАЛИТИКА: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_finanalitics import C80_FormFinanalitics


class C90_FormFinanalitics(C80_FormFinanalitics):
	""" Форма Финаналитика: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Дерево параметров
		self.tree_options.customContextMenuRequested.connect(self.on_RequestMenuFinanalitics)

		# Меню финаналитики
		self.menu_finanalitics_processing.triggered.connect(self.on_RequestProcessingFinanalitics)

	def on_Open(self):
		""" Открытие формы """
		self.SwitchTabsMainToOptions()

		self.ShowTitle()

		self.InitModelOptions()

		self.LoadOptionsLabels()

		self.AdjustTreeOptions_Expand()
		self.AdjustTreeOptions_Color()

		self.AdjustPageDm_Text()

		self.InitModelDataDm()

	# Меню финаналитики
	def on_RequestMenuFinanalitics(self):
		""" Запрос на отображение меню финаналитики """
		self.ShowMenuFinanalitics()

	# Финаналитика
	def on_RequestProcessingFinanalitics(self):
		""" Запрос на выполнение финаналитики """
		self.SendProcessingDy()
		self.SendProcessingDm()
		self.ReadLabelsFinanalitics()

		self.finanalitics.ExecProcessingDm()

		self.InitModelDataDm()

		self.LoadModelDataDm_Income()
		self.LoadModelDataDm_Outcome()

		self.AdjustTableDataDm_Size()
		self.AdjustTableDataDm_Align()

# ФОРМА ЗАПИСЬ ФИНДЕЙСТВИЙ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_record_finactions import C80_FormRecordFinactions


class C90_FormRecordFinactions(C80_FormRecordFinactions):
	""" Форма Запись финдействий: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Таблица данных
		self.tbl_data.doubleClicked.connect(self.on_RequestProcessingTblDataClick)

		# Таблица значений
		self.tre_values.doubleClicked.connect(self.on_RequestProcessingTreValuesClick)

		# Модель значений
		self.model_values.itemChecked.connect(self.on_RequestIncludeValue)
		self.model_values.itemUnchecked.connect(self.on_RequestExcludeValue)

	def on_Open(self):
		super().on_Open()

		self.SetupRecordFinactions()

		self.SetupModelData()

		self.LoadModelDataFromRecordFindata()
		self.LoadModelDataFromRecordFinactions()

		self.AdjustTblDataSpan()
		self.AdjustTblDataSize()
		self.AdjustTblDataColor()

		self.ShowTitle()

		self.AdjustSplitterSize()

		self.Reset()
		self.on_RequestProcessingTblDataClick()

	def on_Close(self):
		super().on_Close()

		self.PrepareUpdateDataPartial()
		self.application.form_findata.UpdateDataPartial()

	def on_RequestProcessingTblDataClick(self):
		""" Запрос на обработку двойного клика по таблице данных """
		self.ReadIdoProcessingFromTblData()
		self.ProcessingTblDataDbClick()

		self.AdjustTreValuesExpand()
		self.AdjustTreValuesCheckable()

		self.ShowCurrentValue()

	def on_DataChanged(self):
		""" Данные изменились """
		self.LoadModelDataFromRecordFinactions()

		self.AdjustTblDataSpan()
		self.AdjustTblDataSize()
		self.AdjustTblDataColor()

		self.ShowTitle()

	def on_RequestProcessingTreValuesClick(self):
		""" Обработка двойного клика по дереву значений """
		self.ReadValueProcessingFromTreValues()

		self.ProcessingTreValuesDbClick()

	def on_RequestIncludeValue(self):
		""" Обработка добавления значения """
		self.ReadValueProcessingFromModelValues()

		self.ProcessingIncludeValue()

	def on_RequestExcludeValue(self):
		""" Обработка исключения значения """
		self.ReadValueProcessingFromModelValues()

		self.ProcessingExcludeValue()

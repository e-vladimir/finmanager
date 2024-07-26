# ФОРМА ЗАПИСИ ФИНДАННЫХ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_record_findata import C80_FormRecordFindata


class C90_FormRecordFindata(C80_FormRecordFindata):
	""" Форма записи финданных: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Таблица данных
		self.table_data.doubleClicked.connect(self.on_RequestProcessingDataClicked)

		# Таблица значений
		self.table_values.doubleClicked.connect(self.on_RequestProcessingValueClicked)

	def on_Open(self):
		super().on_Open()

		self.EnableLockReading()

		self.SetupModelData()
		self.SetupRecordFindata()
		self.LoadModelDataFromFindata()
		self.LoadModelDataFromFinactions()
		self.AdjustTblDataSpan()
		self.AdjustTblDataSize()
		self.AdjustTblDataColor()
		self.AdjustSplitterSize()

		self.DisableLockReading()

		self.ShowTitle()

	# Данные записи финданных
	def on_RequestShowData(self):
		""" Запрос на отображение данных """
		self.EnableLockReading()

		self.LoadModelDataFromFindata()
		self.LoadModelDataFromFinactions()
		self.AdjustTblDataSize()
		self.AdjustSplitterSize()

		self.DisableLockReading()

	def on_RequestShowValues(self):
		""" Запрос на отображение параметров """
		self.EnableLockReading()

		self.ReadIdoProcessingFromTblData()
		self.SetupValuesModel()

		self.ProcessingCurrentIdo()

		self.ShowValueFromRecord()

		self.DisableLockReading()

	def on_DataChanged(self):
		""" Изменились данные """
		self.EnableLockReading()

		self.LoadModelDataFromFindata()
		self.AdjustTblDataSize()
		self.AdjustSplitterSize()

		self.DisableLockReading()

	def on_RequestProcessingDataClicked(self):
		"""  """
		self.ReadRowProcessingFromTblData()
		self.ReadIdoProcessingFromTblData()
		self.ProcessingTblDataClicked()

	def on_RequestProcessingValueClicked(self):
		""" Запрос на изменение значения """
		self.RequestApplyValue()

	def on_RequestOpenRecordFinactions(self):
		""" Запрос на открытие записи финдействий """
		self.OpenRecordFinactions()

	def on_Close(self):
		super().on_Close()

		self.PrepareUpdateDataPartial()
		self.application.form_findata.UpdateDataPartial()

# ФОРМА ФИНДАННЫЕ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_findata import C80_FormFindata


class C90_FormFindata(C80_FormFindata):
	""" Форма Финданные: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Дерево данных
		self.tree_data.customContextMenuRequested.connect(self.on_RequestShowMenuData)
		self.tree_data.doubleClicked.connect(self.on_RequestProcessingDbClickOnTreeData)

		# Меню данных: Финданные
		self.menu_data_findata_create.triggered.connect(self.on_RequestCreateRecordFindata)
		self.menu_data_findata_create_finactions_quick.triggered.connect(self.on_RequestQuickCreateRecordsFinactions)

		# Меню данных: Запись финданных
		self.menu_data_findata_record_open.triggered.connect(self.on_RequestOpenRecordFindata)
		self.menu_data_findata_record_delete.triggered.connect(self.on_RequestDeleteRecordFindata)

		self.menu_data_findata_record_create_finactions.triggered.connect(self.on_RequestCreateRecordFinactions)
		self.menu_data_findata_record_create_finactions_quick.triggered.connect(self.on_RequestQuickCreateRecordFinactions)

		# Меню данных: Запись финдействий
		self.menu_data_finactions_record_open.triggered.connect(self.on_RequestOpenRecordFinactions)
		self.menu_data_finactions_record_delete.triggered.connect(self.on_RequestDeleteRecordFinactions)

		# Меню данных: Управление выделением
		self.menu_data_selection_expand_by_text.triggered.connect(self.on_RequestExpandSelectionByText)
		self.menu_data_selection_collapse_by_text.triggered.connect(self.on_RequestCollapseSelectionByText)
		self.menu_data_selection_expand_by_findescription.triggered.connect(self.on_RequestExpandSelectionByFindescription)
		self.menu_data_selection_collapse_by_findescription.triggered.connect(self.on_RequestCollapseSelectionByFindescription)
		self.menu_data_selection_clean.triggered.connect(self.on_RequestCleanSelection)

		# Меню данных: Утилиты
		self.menu_data_tools_replace.triggered.connect(self.on_RequestReplaceText)

		# Меню данных: Обмен данными
		self.menu_data_exchange_import.triggered.connect(self.on_RequestImport)
		self.menu_data_exchange_export.triggered.connect(self.on_RequestExport)

		# Меню данных: Правила обработки данных
		self.menu_data_rules_replace_text.triggered.connect(self.on_RequestApplyRulesReplaceText)
		self.menu_data_rules_replace_text_for_all.triggered.connect(self.on_RequestApplyRulesReplaceTextForAll)
		self.menu_data_rules_detect_findescription.triggered.connect(self.on_RequestApplyRulesDetectFindescriptionByText)
		self.menu_data_rules_detect_findescription_for_all.triggered.connect(self.on_RequestApplyRulesDetectFindescriptionByTextForAll)

	def on_Init(self):
		super().on_Init()

		self.SetupModelData()

	def on_Open(self):
		self.ShowTitle()

		self.model_data.removeAll()

		self.LoadDataByDds()

		self.AdjustTreeDataExpand()
		self.AdjustTreeDataSize()
		self.AdjustTreeDataColor()

	def on_UpdateData(self):
		""" Запрос на обновление данных """
		self.model_data.removeAll()

		self.LoadDataByDds()

		self.AdjustTreeDataExpand()
		self.AdjustTreeDataSize()
		self.AdjustTreeDataColor()

	def on_UpdateDataPartial(self):
		""" Частичное обновление данных """
		self.ProcessingUpdateDataPartial()

		self.AdjustTreeDataExpand()
		self.AdjustTreeDataSize()
		self.AdjustTreeDataColor()

	# Дерево данных
	def on_RequestProcessingDbClickOnTreeData(self):
		""" Запрос обработки двойного клика по дереву """
		self.ReadIndexColProcessing()
		self.ReadDdProcessing()
		self.ReadOidProcessingFindata()
		self.ReadOidProcessingFinactions()

		self.ProcessingDbClickOnTreeData()

	# Меню данных
	def on_RequestShowMenuData(self):
		""" Запрос отображения меню данных """
		self.ReadDdProcessing()

		self.ReadOidProcessingFindata()
		self.ReadOidProcessingFinactions()

		self.ReadOidsProcessingFindata()
		self.ReadOidsProcessingFinactions()

		self.AdjustMenuDataText()
		self.AdjustMenuDataEnable()

		self.ShowMenuData()

	# Запись финданных
	def on_RequestCreateRecordFindata(self):
		""" Запрос создания записи финданных """
		self.ReadDdProcessing()

		self.CreateRecordFindata()

	def on_RequestOpenRecordFindata(self):
		""" Запрос на открытие записи финданных """
		self.OpenRecordFindata()

	def on_RequestDeleteRecordFindata(self):
		""" Запрос на удаление записи финданных """
		self.DeleteRecordFindata()

	def on_RequestEditNoteRecordFindata(self):
		""" Запрос редактирования примечания записи финданных """
		self.EditNoteRecordFindata()

	def on_RecordFindataCreated(self):
		""" Запись финданных создана """
		self.application.form_record_findata.Open()

	def on_RecordFindataChanged(self):
		""" Запись финданных изменилась """
		self.UpdateRecordFindata()

	def on_RecordFindataDeleted(self):
		""" Запись финданных удалена """
		self.RemoveRecordFindata()

	# Запись финдействий
	def on_RequestCreateRecordFinactions(self):
		""" Запрос на создание записи финдействий """
		self.SwitchProcessingSkip_Off()
		self.SwitchProcessingQuick_Off()

		self.CreateRecordFinactions()

	def on_RequestQuickCreateRecordFinactions(self):
		""" Запрос на быстрое создание записи финдействий """
		self.SwitchProcessingSkip_On()
		self.SwitchProcessingQuick_On()

		self.CreateRecordFinactions()

		self.ReloadRecordFindata()

		self.AdjustTreeDataExpand()
		self.AdjustTreeDataSize()

	def on_RequestQuickCreateRecordsFinactions(self):
		""" Запрос на пакетное создание записей финдействий """
		self.SwitchProcessingSkip_On()
		self.SwitchProcessingQuick_On()

		self.CreateRecordsFinactions()

		self.on_UpdateData()

	def on_RequestOpenRecordFinactions(self):
		""" Запрос открытия записи финдействий """
		self.OpenRecordFinactions()

	def on_RequestDeleteRecordFinactions(self):
		""" Запрос на удаление записи финдействий """
		self.DeleteRecordFinactions()

	def on_RequestEditNoteRecordFinactions(self):
		""" Запрос редактирования примечания записи финдействий """
		self.EditNoteRecordFinactions()

	def on_RecordFinactionsChanged(self):
		""" Запись финдействий изменилась """
		self.UpdateRecordFinactions()

		self.AdjustTreeDataSize()

	# Управление выделением
	def on_RequestExpandSelectionByText(self):
		""" Запрос на расширение выделения по тексту """
		self.SwitchProcessing_Inc()
		self.ProcessingSelectionByText()

	def on_RequestCollapseSelectionByText(self):
		""" Запрос на сокращение выделения по тексту """
		self.SwitchProcessing_Dec()
		self.ProcessingSelectionByText()

	def on_RequestExpandSelectionByFindescription(self):
		""" Запрос на расширение выделения по финсоставу """
		self.SwitchProcessing_Inc()
		self.ProcessingSelectionByFindescription()

	def on_RequestCollapseSelectionByFindescription(self):
		""" Запрос на сокращение выделения по финсоставу """
		self.SwitchProcessing_Dec()
		self.ProcessingSelectionByFindescription()

	def on_RequestCleanSelection(self):
		""" Запрос сброс выделения """
		self.CleanSelection()

	# Утилиты
	def on_RequestReplaceText(self):
		""" Запрос на замену текстовых фрагментов """
		self.ReplaceText()

	# Обмен данными
	def on_RequestImport(self):
		""" Импорт данных """
		self.application.form_import.Open()

	def on_RequestExport(self):
		""" Экспорт данных """
		self.application.form_export.Open()

	# Правила обработки данных
	def on_RequestApplyRulesReplaceText(self):
		""" Запрос на применение правил замены текстовых фрагментов """
		self.ApplyRulesReplaceText()

	def on_RequestApplyRulesReplaceTextForAll(self):
		""" Запрос на применение правил замены текстовых фрагментов для всех записей финданных """
		self.ApplyRulesReplaceTextForAll()

	def on_RequestApplyRulesDetectFindescriptionByText(self):
		""" Запрос на применение правил определения финсостава по текстовым фрагментам """
		self.ApplyRulesDetectFindescriptionByText()

	def on_RequestApplyRulesDetectFindescriptionByTextForAll(self):
		""" Запрос на применение правил определения финсостава по текстовым фрагментам для всех записей финдействий """
		self.ApplyRulesDetectFindescriptionByTextForAll()

# ФОРМА ПРАВИЛ ОБРАБОТКИ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_rules import C80_FormRules


class C90_FormRules(C80_FormRules):
	""" Форма правил обработки: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Список типов правил
		self.cbbox_rules_types.currentIndexChanged.connect(self.on_TypeRulesChanged)

		# Дерево данных
		self.tree_data.doubleClicked.connect(self.on_RequestProcessingDbClickOnTreeData)
		self.tree_data.customContextMenuRequested.connect(self.on_RequestMenu)

		# Меню правил: Правила замены текстовых фрагментов
		self.menu_replace_text_create.triggered.connect(self.on_RequestCreateRecordReplaceText)
		self.menu_replace_text_record_edit_input.triggered.connect(self.on_RequestEditInputForReplaceText)
		self.menu_replace_text_record_edit_output.triggered.connect(self.on_RequestEditOutputForReplaceText)
		self.menu_replace_text_record_delete.triggered.connect(self.on_RequestDeleteRecordReplaceText)

		# Меню правил: Правила определения финсостава
		self.menu_detect_findescription_record_edit_input.triggered.connect(self.on_RequestEditInputForDetectFindescription)
		self.menu_detect_findescription_record_delete.triggered.connect(self.on_RequestDeleteRecordDetectFindescription)
		self.menu_detect_findescription_record_wrap.triggered.connect(self.on_RequestWrapSubRecordDetectFindescription)

	# Служебные события
	def on_Init(self):
		super().on_Init()

		self.ShowRulesTypes()

	def on_Show(self):
		super().on_Show()

		self.SetupModelData()

		self.ShowData()

		self.AdjustTreeExpand()
		self.AdjustTreeDataSizes()

	# Тип событий
	def on_TypeRulesChanged(self):
		""" Тип правил изменился """
		self.ReadTypeProcessing()

		self.ShowData()

		self.AdjustTreeExpand()
		self.AdjustTreeDataSizes()

	# Меню правил
	def on_RequestMenu(self):
		""" Запрос отображению меню """
		self.ReadNameProcessing()
		self.ReadColumnProcessing()
		self.ReadIdoProcessing()

		self.AdjustMenuEnable()
		self.AdjustMenuText()

		self.ShowMenu()

	# Дерево данных
	def on_RequestProcessingDbClickOnTreeData(self):
		""" Запрос обработки двойного клика по дереву данных """
		self.ReadNameProcessing()
		self.ReadIdoProcessing()
		self.ReadColumnProcessing()

		self.ProcessingTreeDataDbClick()

	# Правила замены текстовых фрагментов
	def on_RequestCreateRecordReplaceText(self):
		""" Запрос на создание правила замены текстовых фрагментов """
		self.CreateRecordReplaceText()

	def on_RequestEditOutputForReplaceText(self):
		""" Запрос редактирования параметров правила замены текстовых фрагментов """
		self.EditOutputForRecordReplaceText()

	def on_RequestEditInputForReplaceText(self):
		""" Запрос редактирования параметров правила замены текстовых фрагментов """
		self.EditInputForRecordReplaceText()

	def on_RequestDeleteRecordReplaceText(self):
		""" Запрос удаления записи правил замены текстовых фрагментов """
		self.DeleteRecordReplaceText()

	def on_RecordReplaceTextCreated(self):
		""" Правила замены текстовых фрагментов создано """
		self.ShowData()

	def on_RecordReplaceTextChanged(self):
		""" Запись замены текстовых фрагментов изменилась """
		self.LoadRecordReplaceText()

	def on_RecordReplaceTextDeleted(self):
		""" Запись замены текстовых фрагментов удалена """
		self.SetupModelData()

		self.ShowData()

		self.AdjustTreeExpand()
		self.AdjustTreeDataSizes()

	# Правила определения финструктуры по текстовых фрагментам
	def on_RequestEditInputForDetectFindescription(self):
		""" Запрос на изменение параметров записи правил """
		self.EditInputForRecordDetectFindescription()

	def on_RequestDeleteRecordDetectFindescription(self):
		""" Запрос на удаление записи правил определения финсостава по текстовым фрагментам """
		self.DeleteRecordDetectFindescription()

	def on_RequestWrapSubRecordDetectFindescription(self):
		""" Запрос свёртки фрагментов поиска """
		self.WrapSubRecordsDetectFindescription()

	def on_RecordDetectFindescriptionDeleted(self):
		""" Запись определения финсостава удалена """
		self.SetupModelData()

		self.ShowData()

		self.AdjustTreeExpand()
		self.AdjustTreeDataSizes()

	def on_RecordDetectFindescriptionChanged(self):
		""" Запись определения финсостава изменилась """
		self.LoadRecordDetectFindescriptionByText()

# ФОРМА ФИНДЕЙСТВИЯ: ЛОГИКА УПРАВЛЕНИЯ

from L00_colors          import COLORS
from L80_form_finactions import C80_FormFinactions


class C90_FormFinactions(C80_FormFinactions):
	""" Форма Финдействия: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Дерево финдействий
		self.tree_data.customContextMenuRequested.connect(self.on_RequestMenuFinactions)
		self.tree_data.doubleClicked.connect(self.on_RequestProcessingTreeDataDbClick)

		# Меню финдействий
		self.menu_finactions_create.triggered.connect(self.on_RequestCreateFinactionsRecord)
		self.menu_finactions_import.triggered.connect(self.on_RequestImportFinactions)
		self.menu_finactions_export.triggered.connect(self.on_RequestExportFinactions)

		self.menu_finactions_record_open.triggered.connect(self.on_RequestOpenFinactionsRecord)
		self.menu_finactions_record_delete.triggered.connect(self.on_RequestDeleteFinactionsRecord)
		self.menu_finactions_record_split.triggered.connect(self.on_RequestSplitFinactionsRecord)
		self.menu_finactions_record_edit_note.triggered.connect(self.on_RequestEditNoteFinactionsRecord)

		self.menu_finactions_colors_black.triggered.connect(self.on_RequestSetColorBlack)
		self.menu_finactions_colors_gray.triggered.connect(self.on_RequestSetColorGray)
		self.menu_finactions_colors_blue.triggered.connect(self.on_RequestSetColorBlue)
		self.menu_finactions_colors_green.triggered.connect(self.on_RequestSetColorGreen)
		self.menu_finactions_colors_red.triggered.connect(self.on_RequestSetColorRed)

		self.menu_finactions_pack_reset.triggered.connect(self.on_RequestResetPack)
		self.menu_finactions_pack_expand_by_text.triggered.connect(self.on_RequestExpandPackByText)
		self.menu_finactions_pack_reduce_by_text.triggered.connect(self.on_RequestReducePackByText)

		self.menu_finactions_rules_apply.triggered.connect(self.on_RequestApplyRulesToSelections)
		self.menu_finactions_rules_apply_global.triggered.connect(self.on_RequestApplyRulesToAll)

		self.menu_finactions_tools_replace_text.triggered.connect(self.on_RequestReplaceText)

		self.menu_finactions_reset_by_dm.triggered.connect(self.on_RequestResetFinactionsByDm)
		self.menu_finactions_reset_by_finstruct.triggered.connect(self.on_RequestResetFinactionsByFinstruct)

	def on_Show(self):
		""" Отображение формы """
		self.ShowTitle()

		self.InitModel()
		self.LoadFinactions()

		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Size()
		self.AdjustTreeData_Color()

	def on_UpdateData(self):
		""" Обновление данных """
		self.ShowTitle()

		self.InitModel()
		self.LoadFinactions()

		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Size()
		self.AdjustTreeData_Color()

	# Данные
	def on_UpdateDataPartial(self):
		""" Частичное обновление данных """
		self.ReadProcessingIdoFromWorkspace()
		self.ReadProcessingDdFromRecordFinactions()

		self.CleanFinactionsRecord()

		self.LoadDd()
		self.LoadFinactionsRecord()

		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Size()
		self.AdjustTreeData_Color()

	# Меню финдействий
	def on_RequestMenuFinactions(self):
		""" Запрос отображению меню финдействий """
		self.ReadProcessingDd()
		self.ReadProcessingIdo()
		self.ReadProcessingIdos()

		self.AdjustMenuFinactionsEnable()
		self.AdjustMenuFinactionsText()

		self.ShowMenuFinactions()

	# Финдействия
	def on_RequestCreateFinactionsRecord(self):
		""" Запрос на создание записи финдействий """
		self.CreateFinactionsRecord()

		self.LoadDd()
		self.LoadFinactionsRecord()

		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Size()
		self.AdjustTreeData_Color()

	def on_RequestImportFinactions(self):
		""" Запрос на импорт финдействий """
		self.application.form_import.Open()

	def on_RequestExportFinactions(self):
		""" Запрос на импорт финдействий """
		self.application.form_export.Open()

	# Запись финдействий
	def on_RequestOpenFinactionsRecord(self):
		""" Запрос на открытие записи финдействий """
		self.OpenFinactionsRecord()

	def on_RequestDeleteFinactionsRecord(self):
		""" Запрос на удаление записи финдействий """
		self.DeleteFinactionsRecord()

		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Size()
		self.AdjustTreeData_Color()

	def on_RequestSplitFinactionsRecord(self):
		""" Запрос на разделение записи финдействий """
		self.SplitFinactionsRecord()

		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Size()
		self.AdjustTreeData_Color()

	# Дерево данных
	def on_RequestProcessingTreeDataDbClick(self):
		""" Запрос на обработку двойного клика по дереву данных """
		self.ReadProcessingColumn()
		self.ReadProcessingDd()
		self.ReadProcessingIdo()

		self.ProcessingTreeData_DbClick()

	def on_RequestEditNoteFinactionsRecord(self):
		""" Запрос на редактирование примечания записи финдействий """
		self.EditNoteFinactionsRecord()

		self.LoadFinactionsRecord()

		self.AdjustTreeData_Size()

	# Цветовая метка
	def on_RequestSetColorBlack(self):
		""" Установка цветовой метки: Черный """
		self._processing_color = COLORS.BLACK

		self.SetColor()
		self.LoadFinactionsRecord()

	def on_RequestSetColorGray(self):
		""" Установка цветовой метки: Серый """
		self._processing_color = COLORS.GRAY

		self.SetColor()
		self.LoadFinactionsRecord()

	def on_RequestSetColorBlue(self):
		""" Установка цветовой метки: Синий """
		self._processing_color = COLORS.BLUE

		self.SetColor()
		self.LoadFinactionsRecord()

	def on_RequestSetColorGreen(self):
		""" Установка цветовой метки: Зелёный """
		self._processing_color = COLORS.GREEN

		self.SetColor()
		self.LoadFinactionsRecord()

	def on_RequestSetColorRed(self):
		""" Установка цветовой метки: Красный """
		self._processing_color = COLORS.RED

		self.SetColor()
		self.LoadFinactionsRecord()

	# Пакетный режим
	def on_RequestResetPack(self):
		""" Запрос на сброс пакетного режима """
		self.ResetPack()

	def on_RequestExpandPackByText(self):
		""" Запрос на расширение пакета """
		self.ExpandPackByText()

	def on_RequestReducePackByText(self):
		""" Запрос на сокращение пакета """
		self.ReducePackByText()

	# Правила обработки данных
	def on_RequestApplyRulesToSelections(self):
		""" Запрос применения правил обработки данных к выбранным записям """
		self.ApplyRulesToSelection()

	def on_RequestApplyRulesToAll(self):
		""" Запрос применения правил обработки данных ко всем записям """
		self.ApplyRulesToAll()

	# Утилиты поиска и замены
	def on_RequestReplaceText(self):
		""" Замена текстового фрагмента """
		self.ReplaceText()

	# Сброс данных
	def on_RequestResetFinactionsByDm(self):
		""" Сброс финдействий за месяц """
		self.ResetFinactionsByDm()

		self.InitModel()
		self.LoadFinactions()

		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Size()
		self.AdjustTreeData_Color()

	def on_RequestResetFinactionsByFinstruct(self):
		""" Сброс финдействий по счёту """
		self.ResetFinactionsByFinstruct()

		self.InitModel()
		self.LoadFinactions()

		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Size()
		self.AdjustTreeData_Color()

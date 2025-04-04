# ФОРМА ЭКСПОРТ ДАННЫХ: ЛОГИКА УПРАВЛЕНИЯ
# 01 апр 2025

from L80_form_export import C80_FormExport


class C90_FormExport(C80_FormExport):
	""" Форма экспорт данных: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Дерево данных экспорта операций
		self.TreeDataOperations.doubleClicked.connect(self.on_RequestEditOperations)
		self.TreeDataOperations.customContextMenuRequested.connect(self.on_RequestShowMenuOperations)

		# Меню Экспорт операций
		self.ActionOperationsEditInterval.triggered.connect(self.on_RequestEditOperationsInterval)
		self.ActionOperationsEditAccounts.triggered.connect(self.on_RequestEditOperationsAccounts)
		self.ActionOperationsEditDirectory.triggered.connect(self.on_RequestEditOperationsDirectory)

		self.ActionExportOperations.triggered.connect(self.on_RequestExportOperations)


	# Форма
	def on_Opened(self):
		self.InitModelDataOperations()
		self.LoadModelDataOperations()

		self.AdjustTreeDataOperationsColor()
		self.AdjustTreeDataOperationsExpand()
		self.AdjustTreeDataOperationsSize()


	# Экспорт операций
	def on_RequestEditOperations(self):
		""" Запрос редактирования параметров экспорта операций """
		self.ReadProcessingFieldFromTreeDataOperations()
		self.EditOptionsOperations()

	def on_RequestEditOperationsInterval(self):
		""" Запрос редактирования интервала экспорта операций """
		self.SetOperationsIntervalMode()
		self.SetOperationsIntervalDy()
		self.SetOperationsIntervalDm()

	def on_RequestEditOperationsAccounts(self):
		""" Запрос редактирования счетов экспорта операций """
		self.SetOperationsAccountsMode()
		self.SetOperationsAccountsGroup()
		self.SetOperationsAccountsAccount()

	def on_RequestEditOperationsDirectory(self):
		""" Запрос редактирования директории экспорта операций """
		self.SetOperationsDirectory()

	def on_RequestExportOperations(self):
		""" Запрос экспорта операций """
		self.ExportOperations()

	def on_OptionsOperationsChanged(self):
		""" Параметры экспорта операций изменились """
		self.LoadModelDataOperations()


	# Меню экспорта операций
	def on_RequestShowMenuOperations(self):
		""" Запрос отображению меню экспорта операций """
		self.ReadProcessingFieldFromTreeDataOperations()

		self.AdjustMenuOperations()
		self.AdjustMenuOperationsText()
		self.AdjustMenuOperationsEnable()

		self.ShowMenuOperations()

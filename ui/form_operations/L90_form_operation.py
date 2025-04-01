# ФОРМА ОПЕРАЦИИ: ЛОГИКА УПРАВЛЕНИЯ
# 11 мар 2025

from L00_colors         import COLORS
from L80_form_operation import C80_FormOperation


class C90_FormOperation(C80_FormOperation):
	""" Форма Операции: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Дерево данных
		self.TreeData.customContextMenuRequested.connect(self.on_RequestMenuOperation)
		self.TreeData.doubleClicked.connect(self.on_TreeDataDoubleClicked)

		# Меню Операции
		self.ActionCreateOperation.triggered.connect(self.on_RequestCreateOperation)
		self.ActionOpenProcessing.triggered.connect(self.on_RequestOpenProcessing)
		self.ActionImportOperations.triggered.connect(self.on_RequestOpenFormImport)
		self.ActionExportOperations.triggered.connect(self.on_RequestOpenFormExport)
		self.ActionResetOperations.triggered.connect(self.on_RequestResetOperations)

		# Меню Операция
		self.ActionEditOperationAmount.triggered.connect(self.on_RequestEditOperationAmount)
		self.ActionEditOperationAccounts.triggered.connect(self.on_RequestEditOperationAccounts)
		self.ActionEditOperationDescription.triggered.connect(self.on_RequestEditOperationDescriptions)
		self.ActionEditOperationLabels.triggered.connect(self.on_RequestEditOperationLabels)
		self.ActionDeleteOperation.triggered.connect(self.on_RequestDeleteOperation)
		self.ActionSetOperationColorBlack.triggered.connect(self.on_RequestSetOperationColorToBlack)
		self.ActionSetOperationColorGray.triggered.connect(self.on_RequestSetOperationColorToGray)
		self.ActionSetOperationColorGreen.triggered.connect(self.on_RequestSetOperationColorToGreen)
		self.ActionSetOperationColorBlue.triggered.connect(self.on_RequestSetOperationColorToBlue)
		self.ActionSetOperationColorRed.triggered.connect(self.on_RequestSetOperationColorToRed)
		self.ActionSplitOperation.triggered.connect(self.on_RequestSplitOperation)
		self.ActionCopyOperation.triggered.connect(self.on_RequestCopyOperation)

	# Форма
	def on_Opened(self):
		""" Форма открыта """
		self.ShowTitle()

		self.InitModelData()
		self.ShowOperations()

		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Sort()
		self.AdjustTreeData_Colors()
		self.AdjustTreeData_Size()

		self.CleanModelData()

	def on_RequestPartialUpdateData(self):
		""" Частичное обновление данных """
		if not self.isVisible(): return

		self.ShowOperations()

		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Sort()
		self.AdjustTreeData_Colors()
		self.AdjustTreeData_Size()

	# Меню операций
	def on_RequestMenuOperation(self):
		""" Запрос меню операций """
		self.ReadProcessingIdoFromTreeData()
		self.ReadProcessingDdFromTreeData()

		self.AdjustMenuOperations()
		self.AdjustMenuOperation_Enable()
		self.AdjustMenuOperation_Text()

		self.ShowMenuOperation()

	# Дерево данных
	def on_TreeDataDoubleClicked(self):
		""" Двойной клик по дереву данных """
		self.ReadProcessingIdoFromTreeData()
		self.ReadProcessingIdpFromTreeData()
		self.ReadProcessingDdFromTreeData()

		self.ControlOperationIdp()

	# Операции
	def on_RequestOpenFormImport(self):
		""" Запрос на открытие формы Импорт данных """
		self.Application.FormImport.Open()

	def on_RequestOpenFormExport(self):
		""" Запрос на открытие формы Экспорт данных """
		self.Application.FormExport.Open()

	def on_RequestResetOperations(self):
		""" Запрос на сброс данных """
		self.ResetOperations()

	def on_OperationsReset(self):
		""" Операции сброшены """
		self.InitModelData()
		self.ShowOperations()

		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Sort()
		self.AdjustTreeData_Colors()
		self.AdjustTreeData_Size()

	# Операция
	def on_RequestCreateOperation(self):
		""" Запрос создания операции """
		self.CreateOperation()

	def on_RequestDeleteOperation(self):
		""" Запрос удаления операции """
		self.DeleteOperation()

	def on_RequestEditOperationAmount(self):
		""" Запрос редактирования суммы операции """
		self.EditAmountOperation()

	def on_RequestEditOperationAccounts(self):
		""" Запрос редактирования счетов операции """
		self.EditAccountsOperation()

	def on_RequestEditOperationDescriptions(self):
		""" Запрос редактирования описания операции """
		self.EditDescriptionOperation()

	def on_RequestEditOperationLabels(self):
		""" Запрос редактирования меток операции """
		self.EditLabelsOperation()

	def on_RequestSetOperationColorToBlack(self):
		""" Установка цвета операции: Чёрный """
		self.SetOperationColor(COLORS.BLACK)

	def on_RequestSetOperationColorToGray(self):
		""" Установка цвета операции: Серый """
		self.SetOperationColor(COLORS.GRAY)

	def on_RequestSetOperationColorToGreen(self):
		""" Установка цвета операции: Зелёный """
		self.SetOperationColor(COLORS.GREEN)

	def on_RequestSetOperationColorToBlue(self):
		""" Установка цвета операции: Синий """
		self.SetOperationColor(COLORS.BLUE)

	def on_RequestSetOperationColorToRed(self):
		""" Установка цвета операции: Красный """
		self.SetOperationColor(COLORS.RED)

	def on_RequestSplitOperation(self):
		""" Запрос разделения операции """
		self.SplitOperation()

	def on_RequestCopyOperation(self):
		""" Запрос копирования операции """
		self.CopyOperation()

	def on_OperationCreated(self):
		""" Операция создана """
		self.LoadDdInModelData()
		self.LoadOperationOnModelData()

		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Sort()
		self.AdjustTreeData_Colors()

	def on_OperationDeleted(self):
		""" Операция удалена """
		self.CleanModelData()

	def on_OperationChanged(self):
		""" Операция изменилась """
		self.LoadOperationOnModelData()

		self.AdjustTreeData_Size()
		self.AdjustTreeData_Sort()

	# Обработка данных
	def on_RequestOpenProcessing(self):
		""" Запрос на переход в форму Обработка данных """
		self.Application.FormProcessing.Open()

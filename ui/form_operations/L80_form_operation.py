# ФОРМА ОПЕРАЦИИ: ЛОГИКА ДАННЫХ
# 11 мар 2025

from pathlib            import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QProgressDialog

from G11_convertor_data import AmountToString

from L00_colors         import COLORS
from L00_containers     import CONTAINERS
from L00_operations     import OPERATIONS
from L20_PySide6        import RequestConfirm, RequestItems, RequestMultipleText, RequestText, RequestValue, ShowMessage
from L70_form_operation import C70_FormOperation
from L90_operations     import C90_Operation


class C80_FormOperation(C70_FormOperation):
	""" Форма Операции: Логика данных """

	# Операции
	def ShowOperations(self):
		""" Отображение операций """
		dy, dm = self.Workspace.DyDm()

		for self.processing_dd  in self.Operations.Dds(dy, dm, use_cache=True)                                     : self.LoadDdInModelData()

		for self.processing_ido in self.Operations.Idos(dy, dm, use_cache=True, type_operation=OPERATIONS.PHYSICAL): self.LoadOperationOnModelData()
		for self.processing_ido in self.Operations.Idos(dy, dm, use_cache=True, type_operation=OPERATIONS.VIRTUAL) : self.LoadOperationOnModelData()

	def ResetOperations(self):
		""" Сброс операций """
		if not RequestConfirm("Сброс операций", f"Сброс операций за {self.Workspace.DmDyToString()}"): return

		dy, dm = self.Workspace.DyDm()

		for ido in self.Operations.Idos(dy, dm): C90_Operation(ido).DeleteObject(CONTAINERS.DISK)

		self.on_OperationsReset()

	def GenerateReportDm(self):
		""" Генерация отчёта по остаткам """
		dy, dm                 = self.Workspace.DyDm()
		pdf_file : Path | None = self.Report.GenerateReportDm(dy, dm)
		if not pdf_file:
			ShowMessage("Отчёт за месяц",
			            "Генерация отчёта прервана")
			return

		ShowMessage( "Отчёт за месяц",
		            f"Отчёт сохранён в файл {pdf_file.name}",
		            f"{pdf_file.absolute()}")

	def PredictDestinations(self):
		""" Определение назначений для всех операций """
		dy, dm              = self.Workspace.DyDm()

		operation           = C90_Operation()
		operation.use_cache = True

		idos : list[str]    = self.Operations.Idos(dy, dm)

		dialog_update       = QProgressDialog(self)
		dialog_update.setWindowTitle("Определение назначения")
		dialog_update.setMaximum(len(idos))
		dialog_update.setWindowModality(Qt.WindowModality.WindowModal)
		dialog_update.setLabelText(f"Осталось обработать записей: {dialog_update.maximum()}")
		dialog_update.setMinimumWidth(480)
		dialog_update.forceShow()

		for self.processing_ido in idos:
			dialog_update.setValue(dialog_update.value() + 1)
			dialog_update.setLabelText(f"Осталось обработать записей: {dialog_update.maximum() - dialog_update.value()}")

			operation.Ido(self.processing_ido)
			operation.destination =  set(operation.destination).union(self.Application.DataCompleter.PredictDescriptions(operation.description or operation.src_description))

			self.on_OperationChanged()

	# Операция
	def CreateOperation(self):
		""" Создание операции """
		dd          : int | None = RequestValue("Создание операции", f"{self.Workspace.DmDyToString()}\n\nЧисло месяца:", self.processing_dd or 1, 1, 31)
		if dd     is None: return

		amount      : int | None = RequestValue("Создание операции", f"{dd:02d} {self.Workspace.DmDyToString()}\n\nСумма:", 0, -99999999, 99999999)
		if amount is None: return

		description : str        = RequestText("Создание операции", f"{AmountToString(amount, flag_sign=True)} от {dd:02} {self.Workspace.DmDyToString()}\n\nОписание:", "") or ""

		operation                = C90_Operation()
		operation.GenerateIdo()
		operation.RegisterObject(CONTAINERS.DISK)

		operation.dd             = dd
		operation.dm             = self.Workspace.dm
		operation.dy             = self.Workspace.dy
		operation.amount         = amount
		operation.description    = description

		self.processing_dd  = dd
		self.processing_ido = operation.Ido().data

		operation.CopyToContainer(CONTAINERS.DISK, CONTAINERS.CACHE)
		operation.Caching()

		self.on_OperationCreated()

	def DeleteOperation(self):
		""" Удаление операции """
		operation           = C90_Operation(self.processing_ido)
		operation.use_cache = True
		if not RequestConfirm("Удаление операции", operation.Information()): return

		parent_ido : str    = operation.parent_ido

		for ido in operation.virtual_idos:
			C90_Operation(ido).DeleteObject(CONTAINERS.DISK)
			C90_Operation(ido).DeleteObject(CONTAINERS.CACHE)

		operation.DeleteObject(CONTAINERS.DISK)
		operation.DeleteObject(CONTAINERS.CACHE)

		self.on_OperationDeleted()

		if not parent_ido: return

		operation.Ido(parent_ido)
		operation.CalcVirtualIdos()
		operation.Caching()

		self.processing_ido = parent_ido

		self.on_OperationChanged()

	def EditOperationAmount(self):
		""" Редактирование суммы операции """
		operation           = C90_Operation(self.processing_ido)

		amount : int | None = RequestValue("Редактирование операции", f"{operation.Information()}\n\nСумма:", int(operation.amount), -99999999, 99999999)
		if amount is None: return

		operation.amount = amount
		operation.Caching()

		self.on_OperationChanged()

	def EditOperationAccounts(self):
		""" Редактирование счетов операции """
		dy, dm                           = self.Workspace.DyDm()
		operation                        = C90_Operation(self.processing_ido)

		account_names : list[str] | None = RequestItems( "Редактирование операции",
		                                                f"{operation.Information()}\n\nСчета",
		                                                 self.Accounts.Names(dy, dm),
		                                                 self.Accounts.IdosToNames(operation.account_idos))
		if account_names is None: return

		operation.account_idos = self.Accounts.NamesToIdos(dy, dm, account_names)
		operation.Caching()

		self.on_OperationChanged()

	def EditOperationDescription(self):
		""" Редактирование описания операции """
		operation                = C90_Operation(self.processing_ido)

		description : str | None = RequestText( "Редактирование операции",
		                                       f"{operation.ShortInformation()}\n\n{operation.src_description}",
		                                        operation.description or self.Application.DataCompleter.PredictDescription(operation.description) or operation.Descriptions(),
		                                        self.Application.DataCompleter.PredictDescriptions(operation.src_description) or self.Operations.Descriptions())
		if description is None: return

		operation.description    = description
		operation.Caching()

		self.Application.DataCompleter.UpdateDescriptionInDataOperations(operation.Ido().data)

		self.on_OperationChanged()

	def EditOperationDestination(self):
		""" Редактирование назначения операции """
		operation                       = C90_Operation(self.processing_ido)

		destinations : set[str]         = set(operation.destination).union(self.Application.DataCompleter.PredictDestination(operation.description or operation.src_description))
		destinations : list[str] | None = RequestMultipleText( "Редактирование операции",
				                                              f"{operation.Information()}",
				                                               list(destinations),
				                                               list(sorted(set(self.Operations.Destinations()).union(self.Analytics.Names())))
				                                              )
		if destinations is None: return

		operation.destination = destinations
		operation.Caching()

		self.Application.DataCompleter.UpdateDestinationInDataOperations(operation.Ido().data)

		self.on_OperationChanged()

	def SetOperationColor(self, color: COLORS):
		""" Установка цвета операции """
		operation       = C90_Operation(self.processing_ido)
		operation.color = color
		operation.Caching()

		self.on_OperationChanged()

	def SplitOperation(self):
		""" Разделение операции """
		operation               = C90_Operation(self.processing_ido)
		operation.use_cache     = True

		subamounts : int        = int(sum([C90_Operation(ido).amount for ido in operation.virtual_idos]))
		amount     : int | None = RequestValue("Разделение операции", f"{operation.Information()}", int(operation.amount) - subamounts, -99999999, 99999999)
		if amount is None: return

		new_ido    : str        = operation.Split(amount)

		operation.CalcVirtualIdos()
		operation.Caching()
		self.on_OperationChanged()

		self.processing_ido = new_ido
		C90_Operation(self.processing_ido).Caching()

		self.on_OperationCreated()

	def CopyOperation(self):
		""" Копирование операции """
		self.processing_ido = C90_Operation(self.processing_ido).Copy()

		operation = C90_Operation(self.processing_ido)
		operation.Caching()

		self.on_OperationCreated()

	def SwitchOperationSkip(self):
		""" Смена учёта операции """
		operation           = C90_Operation(self.processing_ido)
		operation.use_cache = True
		operation.skip      = not operation.skip
		operation.Caching()

		self.on_OperationChanged()

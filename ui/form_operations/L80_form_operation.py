# ФОРМА ОПЕРАЦИИ: ЛОГИКА ДАННЫХ
# 11 мар 2025

from pathlib            import Path

from G10_list           import ClearList
from G11_convertor_data import AmountToString

from L00_colors         import COLORS
from L00_containers     import CONTAINERS
from L20_PySide6        import RequestConfirm, RequestItems, RequestMultipleText, RequestText, RequestValue, ShowMessage
from L70_form_operation import C70_FormOperation
from L90_operations     import C90_Operation


class C80_FormOperation(C70_FormOperation):
	""" Форма Операции: Логика данных """

	# Операции
	def ShowOperations(self):
		""" Отображение операций """
		dy, dm = self.Workspace.DyDm()

		for self.processing_dd  in self.Operations.Dds(dy, dm, use_cache=True)                             : self.LoadDdInModelData()
		for self.processing_ido in self.Operations.Idos(dy, dm, use_cache=True, exclude_suboperations=True): self.LoadOperationOnModelData()

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

		self.on_OperationCreated()

	def DeleteOperation(self):
		""" Удаление операции """
		operation = C90_Operation(self.processing_ido)
		if not RequestConfirm("Удаление операции", operation.Information()): return

		operation.DeleteSuboperations()

		operation.DeleteObject(CONTAINERS.DISK)
		operation.DeleteObject(CONTAINERS.CACHE)

		self.on_OperationDeleted()

	def EditOperationAmount(self):
		""" Редактирование суммы операции """
		operation           = C90_Operation(self.processing_ido)
		operation.use_cache = True

		amount : int | None = RequestValue("Редактирование операции", f"{operation.Information()}\n\nСумма:", int(operation.amount), -99999999, 99999999)
		if amount is None: return

		operation.amount = amount

		self.on_OperationChanged()

	def EditOperationAccounts(self):
		""" Редактирование счетов операции """
		dy, dm                           = self.Workspace.DyDm()
		operation                        = C90_Operation(self.processing_ido)
		operation.use_cache              = True

		account_names : list[str] | None = RequestItems( "Редактирование операции",
		                                                f"{operation.Information()}\n\nСчета",
		                                                 self.Accounts.Names(dy, dm),
		                                                 self.Accounts.IdosToNames(operation.account_idos))
		if account_names is None: return

		operation.account_idos = self.Accounts.NamesToIdos(dy, dm, account_names)

		self.on_OperationChanged()

	def EditOperationDestination(self):
		""" Редактирование назначения операции """
		operation                = C90_Operation(self.processing_ido)
		operation.use_cache      = True

		destination : str | None = RequestText( "Редактирование операции",
		                                       f"{operation.ShortInformation()}\n{operation.description}",
		                                         operation.destination or self.Application.DataCompleter.PredictDestination(operation.description) or operation.DestinationOrDescription(),
		                                         self.Application.DataCompleter.PredictDestinations(operation.description) or self.Operations.Destinations())
		if destination is None: return

		operation.destination    = destination

		self.Application.DataCompleter.UpdateDataOperations(operation.Ido().data)

		self.on_OperationChanged()

	def EditOperationLabels(self):
		""" Редактирование меток """
		operation                 = C90_Operation(self.processing_ido)
		operation.use_cache       = True

		processing_labels : set[str] = set(operation.labels).union(self.Application.DataCompleter.PredictLabels(operation.description, operation.destination))

		labels : list[str] | None = RequestMultipleText("Редактирование операции",
		                                                f"{operation.Information()}\n\nМетки:",
		                                                list(sorted(processing_labels)),
		                                                ClearList(self.Operations.Labels()))
		if labels is None: return

		operation.labels = labels

		self.Application.DataCompleter.UpdateDataOperations(operation.Ido().data)

		self.on_OperationChanged()

	def SetOperationColor(self, color: COLORS):
		""" Установка цвета операции """
		operation           = C90_Operation(self.processing_ido)
		operation.use_cache = True
		operation.color     = color

		self.on_OperationChanged()

	def SplitOperation(self):
		""" Разделение операции """
		operation               = C90_Operation(self.processing_ido)
		operation.use_cache     = True

		subammount : int        = int(sum([C90_Operation(oid).amount for oid in operation.suboids]))

		amount     : int | None = RequestValue("Разделение операции", f"{operation.Information()}", int(operation.amount) - subammount, -99999999, 99999999)
		if amount is None: return

		new_ido    : str        = operation.Split(amount)
		self.on_OperationChanged()

		self.processing_ido = new_ido
		C90_Operation(self.processing_ido).CopyToContainer(CONTAINERS.DISK, CONTAINERS.CACHE)

		self.on_OperationCreated()

	def CopyOperation(self):
		""" Копирование операции """
		self.processing_ido = C90_Operation(self.processing_ido).Copy()
		C90_Operation(self.processing_ido).CopyToContainer(CONTAINERS.DISK, CONTAINERS.CACHE)

		self.on_OperationCreated()

	def SwitchOperationSkip(self):
		""" Смена учёта операции """
		operation           = C90_Operation(self.processing_ido)
		operation.use_cache = True
		operation.skip      = not operation.skip

		self.on_OperationChanged()

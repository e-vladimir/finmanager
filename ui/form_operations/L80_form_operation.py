# ФОРМА ОПЕРАЦИИ: ЛОГИКА ДАННЫХ
# 11 мар 2025

from G11_convertor_data import AmountToString

from L00_colors         import COLORS
from L00_containers     import CONTAINERS
from L20_PySide6        import RequestConfirm, RequestItems, RequestText, RequestValue
from L70_form_operation import C70_FormOperation
from L90_operations     import C90_Operation


class C80_FormOperation(C70_FormOperation):
	""" Форма Операции: Логика данных """

	# Операции
	def ShowOperations(self):
		""" Отображение операций """
		dy, dm = self.Workspace.DyDm()

		for self.processing_dd  in self.Operations.Dds(dy, dm) : self.LoadDdInModelData()
		for self.processing_ido in self.Operations.Idos(dy, dm): self.LoadOperationOnModelData()

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

		self.on_OperationCreated()

	def DeleteOperation(self):
		""" Удаление операции """
		operation = C90_Operation(self.processing_ido)
		if not RequestConfirm("Удаление операции", operation.InfoToString()): return

		operation.DeleteObject(CONTAINERS.DISK)

		self.on_OperationDeleted()

	def EditAmountOperation(self):
		""" Редактирование суммы операции """
		operation           = C90_Operation(self.processing_ido)

		amount : int | None = RequestValue("Редактирование операции", f"{operation.InfoToString()}\n\nСумма:", int(operation.amount), -99999999, 99999999)
		if amount is None: return

		operation.amount = amount

		self.on_OperationChanged()

	def EditAccountsOperation(self):
		""" Редактирование счетов операции """
		dy, dm                           = self.Workspace.DyDm()
		operation                        = C90_Operation(self.processing_ido)

		account_names : list[str] | None = RequestItems( "Редактирование операции",
		                                                f"{operation.InfoToString()}\n\nСчета",
		                                                 self.Accounts.Names(dy, dm),
		                                                 self.Accounts.IdosToNames(operation.account_idos))
		if account_names is None: return

		operation.account_idos = self.Accounts.NamesToIdos(dy, dm, account_names)

		self.on_OperationChanged()

	def EditDescriptionOperation(self):
		""" Редактирование описания операции """
		operation                = C90_Operation(self.processing_ido)

		description : str | None = RequestText("Редактирование операции", f"{operation.InfoToString()}\n\nОписание:", operation.description)
		if description is None: return

		operation.description = description

		self.on_OperationChanged()

	def SetOperationColor(self, color: COLORS):
		""" Установка цвета операции """
		operation = C90_Operation(self.processing_ido)
		operation.color = color

		self.on_OperationChanged()

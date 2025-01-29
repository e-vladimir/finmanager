# ФОРМА ФИНАНСОВЫЕ ОПЕРАЦИИ: ЛОГИКА ДАННЫХ

from PySide6.QtCore      import  Qt
from PySide6.QtWidgets   import  QProgressDialog

from G11_convertor_data  import  AmountToString

from L00_containers      import  CONTAINERS
from L20_PySide6         import (RequestItems, RequestValue,
		                         RequestText,
		                         RequestConfirm)
from L70_form_operations import  C70_FormOperations
from L90_operations      import  C90_Operation


class C80_FormOperations(C70_FormOperations):
	""" Форма Финансовые операции: Логика данных """

	# Форма
	def UpdateData(self):
		""" Обновление данных """
		self.ShowOperations()

		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Size()
		self.AdjustTreeData_Color()
		self.AdjustTreeData_Sort()

	# Финансовые операции
	def ShowOperations(self):
		""" Отображение финансовых операций """
		dy, dm = self.workspace.DyDm()

		for self._processing_dd  in self.operations.DdsInDyDm(dy, dm)             : self.LoadDd()
		for self._processing_ido in self.operations.OperationsIdosInDyDmDd(dy, dm): self.LoadOperation()

	def UpdateDataPartial(self):
		""" Частичное обновление данных """
		operation = C90_Operation(self.workspace.IdoOperation())
		self._processing_ido = self.workspace.IdoOperation()
		self._processing_dd  = operation.Dd()

		self.CleanOperation()
		self.CleanDd()

		self.LoadDd()

		self.LoadOperation()

		self.on_UpdateDataPartial()

	def ResetData(self):
		""" Сброс данных """
		dy, dm           = self.workspace.DyDm()
		idos : list[str] = self.operations.OperationsIdosInDyDmDd(dy, dm)

		if not idos                                                                  : return
		if not RequestConfirm("Сброс данных", f"Будет удалено операций: {len(idos)}"): return

		dialog_progress  = QProgressDialog(self)
		dialog_progress.setWindowTitle("Финансовые операции: Сброс данных")
		dialog_progress.setLabelText("Осталось обработать: --")
		dialog_progress.setWindowModality(Qt.WindowModality.WindowModal)
		dialog_progress.setMaximum(len(idos))
		dialog_progress.setMinimumWidth(480)

		for ido in idos:
			dialog_progress.setValue(dialog_progress.value() + 1)
			dialog_progress.setLabelText(f"Осталось обработать: {dialog_progress.maximum() - dialog_progress.value()}")

			operation = C90_Operation(ido)
			operation.DeleteObject(CONTAINERS.DISK)

		dialog_progress.close()

	# Финансовая операция
	def CreateOperation(self):
		""" Создание операции """
		dd_dm_dy    : str        = f"{self._processing_dd:02d} {self.workspace.DmDyToString()}"

		amount      : int | None = RequestValue("Создание финансовой операции", f"Создание операции на {dd_dm_dy}", 0, -99999999, 99999999)
		if amount      is None: return

		destination : str | None = RequestText("Создание финансовой операции", f"{AmountToString(amount, flag_sign=True)} от {dd_dm_dy}")
		if destination is None: return

		operation                = C90_Operation()
		operation.GenerateIdo()
		operation.RegisterObject(CONTAINERS.DISK)
		operation.Dy(self.workspace.Dy())
		operation.Dm(self.workspace.Dm())
		operation.Dd(self._processing_dd)
		operation.Amount(amount)
		operation.Destination(destination)

		self._processing_ido = operation.Ido().data

	def DeleteOperation(self):
		""" Удаление операции """
		operation     = C90_Operation(self._processing_ido)
		text    : str = (f"{AmountToString(operation.Amount(), flag_sign=True)} от {operation.DdDmDyToString()}\n"
		                 f"{operation.Destination()}")

		if not RequestConfirm("Удаление операции", text): return

		operation.DeleteObject(CONTAINERS.DISK)

	def SetOperationAmount(self):
		""" Установка суммы операции """
		operation          = C90_Operation(self._processing_ido)
		text   : str       = (f"{AmountToString(operation.Amount(), flag_sign=True)} от {operation.DdDmDyToString()}\n"
		                      f"{operation.Destination()}\n\n"

		                      f"Сумма:")

		amount: int | None = RequestValue("Редактирование операции", text, int(operation.Amount()), -9999999, 9999999)
		if amount is None: return

		operation.Amount(amount)

	def SetOperationAccounts(self):
		""" Редактирование счетов """
		dy, dm                      = self.workspace.DyDm()
		accounts : list[str]        = self.accounts.AccountsNamesInDyDm(dy, dm)
		if not accounts: return

		operation                   = C90_Operation(self._processing_ido)
		selected : list[str]        = self.accounts.IdosToNames(operation.AccountsIdos())

		text     : str              = (f"{AmountToString(operation.Amount(), flag_sign=True)} от {operation.DdDmDyToString()}\n"
		                               f"{operation.Destination()}\n\n"

		                               f"Счета:")
		names    : list[str] | None = RequestItems("Редактирование операции", text, accounts, selected)
		if names is None: return

		operation.AccountsIdos(self.accounts.NamesToIdos(dy, dm, names))

	def SetOperationDestination(self):
		""" Установка описания операции """
		operation                = C90_Operation(self._processing_ido)
		text        : str        = (f"{AmountToString(operation.Amount(), flag_sign=True)} от {operation.DdDmDyToString()}\n\n"
		                            
		                            f"Назначение:")

		description : str | None = RequestText("Редактирование операции", text, operation.Destination(), self.operations.Destinations())
		if description is None: return

		operation.Destination(description)

	def SetOperationDetail(self):
		""" Установка уточнения операции """
		operation           = C90_Operation(self._processing_ido)
		text   : str        = (f"{AmountToString(operation.Amount(), flag_sign=True)} от {operation.DdDmDyToString()}\n\n"
		                        
		                       f"Уточнение:")

		detail : str | None = RequestText("Редактирование операции", text, operation.Detail(), self.operations.Details())
		if detail is None: return

		operation.Detail(detail)

	def SetOperationObjectInt(self):
		""" Установка объекта внутреннего """
		operation               = C90_Operation(self._processing_ido)
		text       : str        = (f"{AmountToString(operation.Amount(), flag_sign=True)} от {operation.DdDmDyToString()}\n\n"
		                            
		                            f"Объект внутренний:")

		object_int : str | None = RequestText("Редактирование операции", text, operation.ObjectInt(), self.operations.ObjectsInt())
		if object_int is None: return

		operation.ObjectInt(object_int)

	def SetOperationObjectExt(self):
		""" Установка объекта внешнего """
		operation               = C90_Operation(self._processing_ido)
		text       : str        = (f"{AmountToString(operation.Amount(), flag_sign=True)} от {operation.DdDmDyToString()}\n\n"
		                            
		                            f"Объект внешний:")

		object_ext : str | None = RequestText("Редактирование операции", text, operation.ObjectExt(), self.operations.ObjectsExt())
		if object_ext is None: return

		operation.ObjectExt(object_ext)

	def SetOperationColor(self):
		""" Установка цвета операции """
		operation = C90_Operation(self._processing_ido)
		operation.Color(self._processing_color)

	def SplitOperation(self):
		""" Разделение операции """
		operation           = C90_Operation(self._processing_ido)
		text   : str        = (f"{AmountToString(operation.Amount(), flag_sign=True)} от {operation.DdDmDyToString()}\n\n"
		                       f"{operation.Destination()}")

		amount : int | None = RequestValue("Разделение операции", text, int(operation.Amount()), -99999999, 99999999)
		if amount is None: return

		ido_new = operation.Split(amount)
		self.LoadOperation()

		self._processing_ido = ido_new

	def CloneOperation(self):
		""" Клонирование операции """
		operation     = C90_Operation(self._processing_ido)
		ido_new : str = operation.Clone()
		self._processing_ido = ido_new

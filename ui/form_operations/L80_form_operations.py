# ФОРМА ФИНАНСОВЫЕ ОПЕРАЦИИ: ЛОГИКА ДАННЫХ

from G11_convertor_data  import AmountToString

from L00_containers      import CONTAINERS
from L20_PySide6         import RequestValue, RequestText
from L70_form_operations import C70_FormOperations
from L90_operations      import C90_Operation


class C80_FormOperations(C70_FormOperations):
	""" Форма Финансовые операции: Логика данных """

	# Финансовые операции
	def ShowOperations(self):
		""" Отображение финансовых операций """
		dy, dm = self.workspace.DyDm()

		for self._processing_dd  in self.operations.DdsInDyDm(dy, dm)             : self.LoadDd()
		for self._processing_ido in self.operations.OperationsIdosInDyDmDd(dy, dm): self.LoadOperation()

	# Финансовая операция
	def CreateOperation(self):
		""" Создание операции """
		dd_dm_dy    : str        = f"{self._processing_dd:02d} {self.workspace.DmDyToString()}"

		amount      : int | None = RequestValue("Создание финансовой операции", f"Создание операции на {dd_dm_dy}", 0, -99999999, 99999999)
		if amount      is None: return

		description : str | None = RequestText("Создание финансовой операции", f"{AmountToString(amount, flag_sign=True)} от {dd_dm_dy}")
		if description is None: return

		operation                = C90_Operation()
		operation.GenerateIdo()
		operation.RegisterObject(CONTAINERS.DISK)
		operation.Dy(self.workspace.Dy())
		operation.Dm(self.workspace.Dm())
		operation.Dd(self._processing_dd)
		operation.SrcAmount(amount)
		operation.SrcDescription(description)
		operation.Amount(amount)
		operation.Description(description)

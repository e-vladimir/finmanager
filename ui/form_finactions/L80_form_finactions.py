# ФОРМА ФИНДЕЙСТВИЯ: ЛОГИКА ДАННЫХ

from G10_math_linear     import CalcBetween
from G11_convertor_data  import AmountToString

from L00_containers      import CONTAINER_LOCAL
from L00_months          import MONTHS_SHORT
from L20_PySide6         import RequestConfirm, RequestValue
from L70_form_finactions import C70_FormFinactions
from L90_finactions      import C90_FinactionsRecord


class C80_FormFinactions(C70_FormFinactions):
	""" Форма Финдействия: Логика данных """

	# Финдействия
	def LoadFinactions(self):
		""" Загрузка финдействий """
		dy, dm = self.workspace.DyDm()

		for self._processing_dd in self.finactions.DdsInDyDm(dy, dm):
			self.LoadDd()

			for self._processing_ido in self.finactions.IdosInDyDmDd(dy, dm, self._processing_dd): self.LoadFinactionsRecord()

	# Запись финдействий
	def CreateFinactionsRecord(self):
		""" Создание записи финдействий """
		dy, dm = self.workspace.DyDm()
		dd     = CalcBetween(1, self._processing_dd, 31)

		amount  : int | None = RequestValue("Создание записи финдействий", f"Запись финдействий от {dd:02d} {MONTHS_SHORT[dm]} {dy:04d}", 0.00, -99999999.00, 99999999.00)
		if amount is None: return

		self._processing_dd  = dd
		self._processing_ido = self.finactions.CreateRecord(dy, dm, dd, amount)

	def OpenFinactionsRecord(self):
		""" Открытие записи финдействий """
		self.SendProcessingIdoToWorkspace()

		self.application.form_finactions_record.Open()

	def DeleteFinactionsRecord(self):
		""" Удаление записи финдействий """
		record       = C90_FinactionsRecord(self._processing_ido)
		amount : str = AmountToString(record.Amount(), False, True)

		if not RequestConfirm("Финдействия", f"Удаление записи финдействий\n{amount} от {record.DdDmDyToString()}"): return

		record.DeleteObject(CONTAINER_LOCAL)

		self.CleanFinactionsRecord()

	def SplitFinactionsRecord(self):
		""" Разделение записи финдействий """
		record               = C90_FinactionsRecord(self._processing_ido)
		amount  : int | None = RequestValue("Разделение записи финдействий", f"{AmountToString(record.Amount(), False, True)} от {record.DdDmDyToString()}", int(record.Amount()), -99999999, 99999999)
		if amount is None: return

		ido_new : str        = record.SplitAmount(amount)

		self.LoadFinactionsRecord()

		self._processing_ido = ido_new
		self.LoadFinactionsRecord()

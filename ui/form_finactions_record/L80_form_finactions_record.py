# ФОРМА ЗАПИСЬ ФИНДЕЙСТВИЙ: ЛОГИКА ДАННЫХ

from G10_datetime               import CurrentDd

from L00_containers             import CONTAINER_LOCAL
from L70_form_finactions_record import C70_FormFinactionsRecord


class C80_FormFinactionsRecord(C70_FormFinactionsRecord):
	""" Форма Запись финдействий: Логика данных """

	# Запись финдействий
	def CreateFinactionsRecord(self):
		""" Создание записи финдействий """
		self.finactions_record.GenerateIdo()
		self.finactions_record.RegisterObject(CONTAINER_LOCAL)

		self.finactions_record.Dy(self.workspace.Dy())
		self.finactions_record.Dm(self.workspace.Dm())
		self.finactions_record.Dd(CurrentDd())
		self.finactions_record.SrcNote("")
		self.finactions_record.SrcAmount(0.00)
		self.finactions_record.Note("")
		self.finactions_record.Amount(0.00)
		self.finactions_record.Labels([])
		self.finactions_record.FinstructIdos([])

		self.Open()

	def LoadFinactionsRecord(self):
		""" Загрузка записи финдействий """
		pass

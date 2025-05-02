# ФИНАНСОВЫЕ ОПЕРАЦИИ: ЛОГИКА УПРАВЛЕНИЯ
# 11 мар 2025

from L80_operations import C80_Operation, C80_Operations


class C90_Operation(C80_Operation):
	""" Финансовая операция: Логика управления """

	def on_ObjectRegistered(self, container_name: str):
		""" Объект зарегистрирован """
		self.account_idos = []
		self.amount       = 0
		self.dd           = 0
		self.description  = ""
		self.destination  = ""
		self.dm           = 0
		self.dy           = 0
		self.labels       = []
		self.parent_ido   = ""
		self.skip         = False
		self.virtual_idos = []


class C90_Operations(C80_Operations):
	""" Финансовые операции: Логика управления """
	pass

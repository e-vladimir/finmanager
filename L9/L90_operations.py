# ФИНАНСОВЫЕ ОПЕРАЦИИ: ЛОГИКА УПРАВЛЕНИЯ

from L00_colors     import COLORS
from L80_operations import C80_Operation, C80_Operations


class C90_Operation(C80_Operation):
	""" Финансовая операция: Логика управления """

	def on_ObjectRegistered(self, container_name: str):
		""" Объект зарегистрирован """
		self.AccountsIdos([])
		self.Amount(0)
		self.Color(COLORS.BLACK)
		self.Crc("")
		self.Dd(0)
		self.Destination("")
		self.Detail("")
		self.Dm(0)
		self.Dy(0)
		self.ObjectExt("")
		self.ObjectInt("")


class C90_Operations(C80_Operations):
	""" Финансовые операции: Логика управления """
	pass

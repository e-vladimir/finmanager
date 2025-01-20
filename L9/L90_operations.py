# ФИНАНСОВЫЕ ОПЕРАЦИИ: ЛОГИКА УПРАВЛЕНИЯ

from L00_colors     import COLORS
from L80_operations import C80_Operation, C80_Operations


class C90_Operation(C80_Operation):
	""" Финансовая операция: Логика управления """

	def on_ObjectRegistered(self, container_name: str):
		""" Объект зарегистрирован """
		self.Dy(0)
		self.Dm(0)
		self.Dd(0)

		self.AccountsIdos([])

		self.Amount(0)
		self.Description("")
		self.Destination([])
		self.ObjectInt("")
		self.ObjectExt("")

		self.Color(COLORS.BLACK)
		self.Crc("")


class C90_Operations(C80_Operations):
	""" Финансовые операции: Логика управления """
	pass

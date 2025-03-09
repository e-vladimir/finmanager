# СЧЁТ: МОДЕЛЬ ДАННЫХ
# 14 фев 2025

from G20_meta_frame   import C20_MetaFrame
from G30_cactus_frame import C30_StructField
from G31_cactus_frame import C31_StructFrameWithEvents


class C40_Account(C31_StructFrameWithEvents):
	""" Счёт: Модель данных """

	_idc = "Счёт"

	def Init_10(self):
		self.FDm             = C30_StructField(self, "Месяц")
		self.FDy             = C30_StructField(self, "Год")
		self.FGroup          = C30_StructField(self, "Группа счетов")
		self.FInitialBalance = C30_StructField(self, "Баланс начальный")
		self.FName           = C30_StructField(self, "Название")


class C40_Accounts(C20_MetaFrame):
	""" Контроллер счетов: Модель данных """
	pass

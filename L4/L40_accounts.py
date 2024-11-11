# СЧЕТА: МОДЕЛЬ ДАННЫХ

from G20_meta_frame   import C20_MetaFrame
from G30_cactus_frame import C30_StructField
from G31_cactus_frame import C31_StructFrameWithEvents


class C40_Account(C31_StructFrameWithEvents):
	""" Счёт: Модель данных """

	_idc = "Счёт"

	def Init_10(self):
		super().Init_10()

		self.f_dy              = C30_StructField(self, "Год")
		self.f_dm              = C30_StructField(self, "Месяц")

		self.f_name            = C30_StructField(self, "Название счёта")
		self.f_group           = C30_StructField(self, "Группа счетов")

		self.f_balance_initial = C30_StructField(self, "Остаток начальный")


class C40_AccountGroup(C20_MetaFrame):
	""" Группа счетов: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._processing_group : str = ""


class C40_Accounts(C20_MetaFrame):
	""" Счета: Модель данных """
	pass

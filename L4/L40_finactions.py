# ФИНДЕЙСТВИЯ: МОДЕЛЬ ДАННЫХ

from G20_meta_frame   import C20_MetaFrame
from G30_cactus_frame import C30_StructFrame, C30_StructField


class C40_FinactionsRecord(C30_StructFrame):
	""" Запись финдействий: Модель данных """

	_idc = "Финдействия"

	def Init_10(self):
		super().Init_10()

		self.f_dy             = C30_StructField(self, "Год")
		self.f_dm             = C30_StructField(self, "Месяц")
		self.f_dd             = C30_StructField(self, "День")

		self.f_src_note       = C30_StructField(self, "Исходное примечание")
		self.f_src_amount     = C30_StructField(self, "Исходная сумма")

		self.f_note           = C30_StructField(self, "Примечание")
		self.f_amount         = C30_StructField(self, "Сумма")

		self.f_color          = C30_StructField(self, "Цветовая метка")

		self.f_labels         = C30_StructField(self, "Метки")

		self.f_finstruct_idos = C30_StructField(self, "Записи финструктуры")


class C40_Finactions(C20_MetaFrame):
	""" Финдействия: Модель данных """
	pass

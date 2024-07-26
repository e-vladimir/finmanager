# ФИНДАННЫЕ: МОДЕЛЬ ДАННЫХ

from G20_meta_frame   import C20_MetaFrame
from G30_cactus_frame import C30_StructFrame, C30_StructField


class C40_RecordFindata(C30_StructFrame):
	""" Запись финданных: Модель данных """

	_idc = "Финданные"

	def Init_10(self):
		""" Инициализация параметров """

		self.f_dd            = C30_StructField(self, "Число")
		self.f_dm            = C30_StructField(self, "Месяц")
		self.f_dy            = C30_StructField(self, "Год")

		self.f_amount        = C30_StructField(self, "Сумма")

		self.f_uid           = C30_StructField(self, "UID")

		self.f_finstruct_ido = C30_StructField(self, "Финструктура")

		self.f_note          = C30_StructField(self, "Примечание")


class C40_Findata(C20_MetaFrame):
	""" Финструктура: Модель данных """

	def Init_00(self):
		self._idc               : str = ""

		self._idp_dd            : str = ""
		self._idp_dm            : str = ""
		self._idp_dy            : str = ""

		self._idp_amount        : str = ""

		self._idp_uid           : str = ""

		self._idp_finstruct_ido : str = ""

		self._idp_note          : str = ""

	def Init_01(self):
		record_finstruct = C40_RecordFindata()

		self._idc               = record_finstruct.Idc().data

		self._idp_dd            = record_finstruct.f_dd.Idp().data
		self._idp_dm            = record_finstruct.f_dm.Idp().data
		self._idp_dy            = record_finstruct.f_dy.Idp().data

		self._idp_amount        = record_finstruct.f_amount.Idp().data

		self._idp_uid           = record_finstruct.f_uid.Idp().data

		self._idp_finstruct_ido = record_finstruct.f_finstruct_ido.Idp().data

		self._idp_note          = record_finstruct.f_note.Idp().data

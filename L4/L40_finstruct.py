# ФИНСТРУКТУРА: МОДЕЛЬ ДАННЫХ

from G20_meta_frame   import C20_MetaFrame
from G30_cactus_frame import C30_StructFrame, C30_StructField


class C40_RecordFinstruct(C30_StructFrame):
	""" Запись финструктуры: Модель данных """

	_idc = "Финструктура"

	def Init_10(self):
		""" Инициализация параметров """

		self.f_name       = C30_StructField(self, "Наименование")
		self.f_parent_oid = C30_StructField(self, "Корневой уровень")
		self.f_dm         = C30_StructField(self, "Месяц")
		self.f_dy         = C30_StructField(self, "Год")
		self.f_priority   = C30_StructField(self, "Приоритет")


class C40_Finstruct(C20_MetaFrame):
	""" Финструктура: Модель данных """

	def Init_00(self):
		self._idc            : str = ""

		self._idp_name       : str = ""
		self._idp_parent_oid : str = ""
		self._idp_dy         : str = ""
		self._idp_dm         : str = ""
		self._idp_priority   : str = ""

	def Init_01(self):
		record_finstruct = C40_RecordFinstruct()

		self._idc            = record_finstruct.Idc().data

		self._idp_name       = record_finstruct.f_name.Idp().data
		self._idp_parent_oid = record_finstruct.f_parent_oid.Idp().data
		self._idp_dy         = record_finstruct.f_dy.Idp().data
		self._idp_dm         = record_finstruct.f_dm.Idp().data
		self._idp_priority   = record_finstruct.f_priority.Idp().data

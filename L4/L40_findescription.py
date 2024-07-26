# ФИНСОСТАВ: МОДЕЛЬ ДАННЫХ

from G20_meta_frame   import C20_MetaFrame
from G30_cactus_frame import C30_StructFrame, C30_StructField


class C40_RecordFindescription(C30_StructFrame):
	""" Запись финсостава: Модель данных """

	_idc = "Финсостав"

	def Init_10(self):
		""" Инициализация параметров """
		self.f_categories = C30_StructField(self, "Категории")
		self.f_name       = C30_StructField(self, "Наименование")
		self.f_parent_ido = C30_StructField(self, "Корневая запись")


class C40_Findescription(C20_MetaFrame):
	""" Финсостав: Модель данных """

	def Init_00(self):
		self._idc            : str = ""

		self._idp_categories : str = ""
		self._idp_parent_ido : str = ""
		self._idp_name       : str = ""

	def Init_01(self):
		record_findescription = C40_RecordFindescription()

		self._idc             = record_findescription.Idc().data

		self._idp_categories  = record_findescription.f_categories.Idp().data
		self._idp_parent_ido  = record_findescription.f_parent_ido.Idp().data
		self._idp_name        = record_findescription.f_name.Idp().data

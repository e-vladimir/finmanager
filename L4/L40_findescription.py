# ФИНСОСТАВ: МОДЕЛЬ ДАННЫХ

from G20_meta_frame   import C20_MetaFrame
from G30_cactus_frame import C30_StructFrame, C30_StructField


class C40_RecordFindescription(C30_StructFrame):
	""" Запись финсостава: Модель данных """

	_oci = "Финсостав"

	def InitFields(self):
		""" Инициализация параметров """
		self.f_categories = C30_StructField(self, "Категории")
		self.f_name       = C30_StructField(self, "Наименование")
		self.f_parent_oid = C30_StructField(self, "Корневая запись")


class C40_Findescription(C20_MetaFrame):
	""" Финсостав: Модель данных """

	def Init_00(self):
		self._oci            : str = ""

		self._pid_categories : str = ""
		self._pid_parent_oid : str = ""
		self._pid_name       : str = ""

	def Init_01(self):
		record_findescription = C40_RecordFindescription()

		self._oci             = record_findescription.Oci().text

		self._pid_categories  = record_findescription.f_categories.Pid().text
		self._pid_parent_oid  = record_findescription.f_parent_oid.Pid().text
		self._pid_name        = record_findescription.f_name.Pid().text

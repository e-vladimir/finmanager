# ФИНСТРУКТУРА: МОДЕЛЬ ДАННЫХ

from G20_meta_frame   import C20_MetaFrame
from G30_cactus_frame import C30_StructFrame, C30_StructField


class C40_RecordFinstruct(C30_StructFrame):
	""" Запись финструктуры: Модель данных """

	_oci = "Финструктура"

	def InitFields(self):
		""" Инициализация параметров """

		self.f_name       = C30_StructField(self, "Наименование")
		self.f_parent_oid = C30_StructField(self, "Корневой уровень")
		self.f_dm         = C30_StructField(self, "Месяц")
		self.f_dy         = C30_StructField(self, "Год")
		self.f_priority   = C30_StructField(self, "Приоритет")


class C40_Finstruct(C20_MetaFrame):
	""" Финструктура: Модель данных """

	def Init_00(self):
		self._oci            : str = ""

		self._pid_name       : str = ""
		self._pid_parent_oid : str = ""
		self._pid_dy         : str = ""
		self._pid_dm         : str = ""
		self._pid_priority   : str = ""

	def Init_01(self):
		record_finstruct = C40_RecordFinstruct()

		self._oci            = record_finstruct.Oci().text

		self._pid_name       = record_finstruct.f_name.Pid().text
		self._pid_parent_oid = record_finstruct.f_parent_oid.Pid().text
		self._pid_dy         = record_finstruct.f_dy.Pid().text
		self._pid_dm         = record_finstruct.f_dm.Pid().text
		self._pid_priority   = record_finstruct.f_priority.Pid().text

# ФИНСОСТОЯНИЕ: МОДЕЛЬ ДАННЫХ

from G20_meta_frame   import C20_MetaFrame
from G30_cactus_frame import C30_StructFrame, C30_StructField


class C40_RecordFinstate(C30_StructFrame):
	""" Запись финсостояния: Модель данных """

	_oci = "Финсостояние"

	def InitFields(self):
		""" Инициализация параметров """

		self.f_finstruct_oid   = C30_StructField(self, "Финструктура")
		self.f_remains_initial = C30_StructField(self, "ОстНач",     0)


class C40_Finstate(C20_MetaFrame):
	""" Финсостояние: Модель данных """

	def Init_00(self):
		self._oci                : str = ""

		self._pid_finstruct_oid  : str = ""
		self._pid_remain_initial : str = ""

	def Init_01(self):
		record_finstate = C40_RecordFinstate()

		self._oci                = record_finstate.Oci().text

		self._pid_finstruct_oid  = record_finstate.f_finstruct_oid.Pid().text
		self._pid_remain_initial = record_finstate.f_remains_initial.Pid().text

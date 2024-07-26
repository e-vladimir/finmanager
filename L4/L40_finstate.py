# ФИНСОСТОЯНИЕ: МОДЕЛЬ ДАННЫХ

from G20_meta_frame   import C20_MetaFrame
from G30_cactus_frame import C30_StructFrame, C30_StructField


class C40_RecordFinstate(C30_StructFrame):
	""" Запись финсостояния: Модель данных """

	_idc = "Финсостояние"

	def Init_10(self):
		""" Инициализация параметров """

		self.f_finstruct_oid   = C30_StructField(self, "Финструктура")
		self.f_remains_initial = C30_StructField(self, "ОстНач",     0)


class C40_Finstate(C20_MetaFrame):
	""" Финсостояние: Модель данных """

	def Init_00(self):
		self._idc                : str = ""

		self._idp_finstruct_oid  : str = ""
		self._idp_remain_initial : str = ""

	def Init_01(self):
		record_finstate = C40_RecordFinstate()

		self._idc                = record_finstate.Idc().data

		self._idp_finstruct_oid  = record_finstate.f_finstruct_oid.Idp().data
		self._idp_remain_initial = record_finstate.f_remains_initial.Idp().data

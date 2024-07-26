# ФИНДЕЙСТВИЯ: МОДЕЛЬ ДАННЫХ

from G20_meta_frame     import C20_MetaFrame
from G30_cactus_frame   import C30_StructFrame, C30_StructField


class C40_RecordFinactions(C30_StructFrame):
	""" Запись финдействий: Модель данных """

	_idc = "Финдействия"

	def Init_10(self):
		""" Инициализация параметров """
		self.f_dd                  = C30_StructField(self, "Число")
		self.f_dm                  = C30_StructField(self, "Месяц")
		self.f_dy                  = C30_StructField(self, "Год")

		self.f_amount              = C30_StructField(self, "Сумма")

		self.f_findata_oid         = C30_StructField(self, "Финданные")
		self.f_finstruct_oids      = C30_StructField(self, "Финструктура")
		self.f_findescription_oids = C30_StructField(self, "Финсостав")

		self.f_note                = C30_StructField(self, "Примечание")

		self.f_color               = C30_StructField(self, "Цветовая метка")


class C40_Finactions(C20_MetaFrame):
	""" Финдействия: Модель данных """

	def Init_00(self):
		self._idc                     : str = ""

		self._idp_dd                  : str = ""
		self._idp_dm                  : str = ""
		self._idp_dy                  : str = ""

		self._idp_amount              : str = ""

		self._idp_findata_oid         : str = ""
		self._idp_finstruct_oids      : str = ""
		self._idp_findescription_oids : str = ""

		self._idp_note                : str = ""

	def Init_01(self):
		record_finaction = C40_RecordFinactions()

		self._idc                     = record_finaction.Idc().data

		self._idp_dd                  = record_finaction.f_dd.Idp().data
		self._idp_dm                  = record_finaction.f_dm.Idp().data
		self._idp_dy                  = record_finaction.f_dy.Idp().data

		self._idp_amount              = record_finaction.f_amount.Idp().data

		self._idp_findata_oid         = record_finaction.f_findata_oid.Idp().data
		self._idp_finstruct_oids      = record_finaction.f_finstruct_oids.Idp().data
		self._idp_findescription_oids = record_finaction.f_findescription_oids.Idp().data

		self._idp_note                = record_finaction.f_note.Idp().data

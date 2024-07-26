# ФИНСТАТИСТИКА: МОДЕЛЬ ДАННЫХ

from G20_meta_frame import C20_MetaFrame

from L40_finactions import C40_RecordFinactions


class C40_Finstatistic(C20_MetaFrame):
	""" Финстатистика: Структура данных """

	def Init_00(self):
		super().Init_00()

		self._idc                : str = ""

		self._idp_findescription : str = ""
		self._idp_dy             : str = ""
		self._idp_dm             : str = ""
		self._idp_amount         : str = ""

	def Init_01(self):
		super().Init_01()

		record_finactions = C40_RecordFinactions()

		self._idc                      = record_finactions.Idc().data
		self._idp_findescription       = record_finactions.f_findescription_oids.Idp().data
		self._idp_dy                   = record_finactions.f_dy.Idp().data
		self._idp_dm                   = record_finactions.f_dm.Idp().data
		self._idp_amount               = record_finactions.f_amount.Idp().data

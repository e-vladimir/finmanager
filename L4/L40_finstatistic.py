# ФИНСТАТИСТИКА: МОДЕЛЬ ДАННЫХ

from G20_meta_frame import C20_MetaFrame

from L40_finactions import C40_RecordFinactions


class C40_Finstatistic(C20_MetaFrame):
	""" Финстатистика: Структура данных """

	def Init_00(self):
		super().Init_00()

		self._oci                : str = ""

		self._pid_findescription : str = ""
		self._pid_dy             : str = ""
		self._pid_dm             : str = ""
		self._pid_amount         : str = ""

	def Init_01(self):
		super().Init_01()

		record_finactions = C40_RecordFinactions()

		self._oci                      = record_finactions.Oci().text
		self._pid_findescription       = record_finactions.f_findescription_oids.Pid().text
		self._pid_dy                   = record_finactions.f_dy.Pid().text
		self._pid_dm                   = record_finactions.f_dm.Pid().text
		self._pid_amount               = record_finactions.f_amount.Pid().text

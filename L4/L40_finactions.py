# ФИНДЕЙСТВИЯ: МОДЕЛЬ ДАННЫХ

from G20_meta_frame     import C20_MetaFrame
from G30_cactus_frame   import C30_StructFrame, C30_StructField


class C40_RecordFinactions(C30_StructFrame):
	""" Запись финдействий: Модель данных """

	_oci = "Финдействия"

	def InitFields(self):
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
		self._oci                     : str = ""

		self._pid_dd                  : str = ""
		self._pid_dm                  : str = ""
		self._pid_dy                  : str = ""

		self._pid_amount              : str = ""

		self._pid_findata_oid         : str = ""
		self._pid_finstruct_oids      : str = ""
		self._pid_findescription_oids : str = ""

		self._pid_note                : str = ""

	def Init_01(self):
		record_finaction = C40_RecordFinactions()

		self._oci                     = record_finaction.Oci().text

		self._pid_dd                  = record_finaction.f_dd.Pid().text
		self._pid_dm                  = record_finaction.f_dm.Pid().text
		self._pid_dy                  = record_finaction.f_dy.Pid().text

		self._pid_amount              = record_finaction.f_amount.Pid().text

		self._pid_findata_oid         = record_finaction.f_findata_oid.Pid().text
		self._pid_finstruct_oids      = record_finaction.f_finstruct_oids.Pid().text
		self._pid_findescription_oids = record_finaction.f_findescription_oids.Pid().text

		self._pid_note                = record_finaction.f_note.Pid().text

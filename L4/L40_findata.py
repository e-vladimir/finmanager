# ФИНДАННЫЕ: МОДЕЛЬ ДАННЫХ

from G20_meta_frame   import C20_MetaFrame
from G30_cactus_frame import C30_StructFrame, C30_StructField


class C40_RecordFindata(C30_StructFrame):
	""" Запись финданных: Модель данных """

	_oci = "Финданные"

	def InitFields(self):
		""" Инициализация параметров """

		self.f_dd            = C30_StructField(self, "Число")
		self.f_dm            = C30_StructField(self, "Месяц")
		self.f_dy            = C30_StructField(self, "Год")

		self.f_amount        = C30_StructField(self, "Сумма")

		self.f_uid           = C30_StructField(self, "UID")

		self.f_finstruct_oid = C30_StructField(self, "Финструктура")

		self.f_note          = C30_StructField(self, "Примечание")


class C40_Findata(C20_MetaFrame):
	""" Финструктура: Модель данных """

	def Init_00(self):
		self._oci               : str = ""

		self._pid_dd            : str = ""
		self._pid_dm            : str = ""
		self._pid_dy            : str = ""

		self._pid_amount        : str = ""

		self._pid_uid           : str = ""

		self._pid_finstruct_oid : str = ""

		self._pid_note          : str = ""

	def Init_01(self):
		record_finstruct = C40_RecordFindata()

		self._oci               = record_finstruct.Oci().text

		self._pid_dd            = record_finstruct.f_dd.Pid().text
		self._pid_dm            = record_finstruct.f_dm.Pid().text
		self._pid_dy            = record_finstruct.f_dy.Pid().text

		self._pid_amount        = record_finstruct.f_amount.Pid().text

		self._pid_uid           = record_finstruct.f_uid.Pid().text

		self._pid_finstruct_oid = record_finstruct.f_finstruct_oid.Pid().text

		self._pid_note          = record_finstruct.f_note.Pid().text

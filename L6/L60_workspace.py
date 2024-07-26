# РАБОЧЕЕ ПРОСТРАНСТВО: МЕХАНИКА ДАННЫХ

from L00_containers import CONTAINER_RAM

from L11_datetime   import *
from L50_workspace  import C50_Workspace


class C60_Workspace(C50_Workspace):
	""" Рабочее пространство: Механика данных """

	# Параметры
	def Dy(self, year: int = None) -> int:
		""" Год """
		if year is None: return self.f_dy.ToInteger(CONTAINER_RAM).data

		self.f_dy.FromInteger(CONTAINER_RAM, year)

	def Dm(self, month: int = None) -> int:
		""" Месяц """
		if month is None: return self.f_dm.ToInteger(CONTAINER_RAM).data

		self.f_dm.FromInteger(CONTAINER_RAM, month)

	def IdoRecordFindata(self, ido: int = None) -> int:
		""" OID записи финданных """
		if ido is None: return self.f_record_findata_ido.ToString(CONTAINER_RAM).data

		self.f_record_findata_ido.FromString(CONTAINER_RAM, ido)

	def IdoRecordFinactions(self, ido: int = None) -> int:
		""" OID записи финдействий """
		if ido is None: return self.f_record_finactions_ido.ToString(CONTAINER_RAM).data

		self.f_record_finactions_ido.FromString(CONTAINER_RAM, ido)

	def IdoRecordRules(self, ido: int = None) -> int:
		""" OID записи правил """
		if ido is None: return self.f_record_rules_ido.ToString(CONTAINER_RAM).data

		self.f_record_rules_ido.FromString(CONTAINER_RAM, ido)

	def ProcessingType(self, text: int = None) -> int:
		""" Тип обработки """
		if text is None: return self.f_processing_type.ToString(CONTAINER_RAM).data

		self.f_processing_type.FromString(CONTAINER_RAM, text)

	# Переключение
	def SwitchToMain(self):
		""" Переключение на основное рабочее пространство """
		self.Ido("MAIN_WORKSPACE")
		self.RegisterObject(CONTAINER_RAM)

	# Смещение
	def ShiftToCurrentDyDm(self):
		""" Смещение на текущий год и месяц """
		self.Dy(CurrentDy())
		self.Dm(CurrentDm())

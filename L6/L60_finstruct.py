# ФИНСТРУКТУРА: МЕХАНИКА ДАННЫХ

from L00_containers import CONTAINER_LOCAL
from L50_finstruct  import C50_FinstructRecord, C50_Finstruct


class C60_FinstructRecord(C50_FinstructRecord):
	""" Запись финструктуры: Механика данных """

	# Параметры
	def Dy(self, year: int = None) -> int:
		""" Год """
		if year is None: return self.f_dy.ToInteger(CONTAINER_LOCAL).data
		else           :        self.f_dy.FromInteger(CONTAINER_LOCAL, year)

	def Dm(self, month: int = None) -> int:
		""" Месяц """
		if month is None: return self.f_dm.ToInteger(CONTAINER_LOCAL).data
		else            :        self.f_dm.FromInteger(CONTAINER_LOCAL, month)

	def Name(self, text: str = None) -> str:
		""" Наименование """
		if text is None: return self.f_name.ToString(CONTAINER_LOCAL).data
		else           :        self.f_name.FromString(CONTAINER_LOCAL, text)


class C60_Finstruct(C50_Finstruct):
	""" Финструктура: Механика данных """
	pass

# ФИНСТРУКТУРА: МЕХАНИКА ДАННЫХ

from L00_containers import CONTAINER_LOCAL
from L50_finstruct  import C50_RecordFinstruct, C50_Finstruct


class C60_RecordFinstruct(C50_RecordFinstruct):
	""" Запись финструктуры: Механика данных """

	def ParentIdo(self, ido: str = None) -> str:
		""" OID родительского уровня """
		if ido is None  : return self.f_parent_ido.ToString(CONTAINER_LOCAL).data
		else            :        self.f_parent_ido.FromString(CONTAINER_LOCAL, ido)

	def Name(self, text: str = None) -> str:
		""" Наименование записи финструктуры """
		if text is None : return self.f_name.ToString(CONTAINER_LOCAL).data
		else            :        self.f_name.FromString(CONTAINER_LOCAL, text)

	def Dy(self, year: int = None) -> int:
		""" Год записи финструктуры """
		if year is None : return self.f_dy.ToInteger(CONTAINER_LOCAL).data
		else            :        self.f_dy.FromInteger(CONTAINER_LOCAL, year)

	def Dm(self, month: int = None) -> int:
		""" Месяц записи финструктуры """
		if month is None: return self.f_dm.ToInteger(CONTAINER_LOCAL).data
		else            :        self.f_dm.FromInteger(CONTAINER_LOCAL, month)

	def Priority(self, flag: bool = None) -> bool:
		""" Признак приоритета записи финструктуры """
		if flag is None : return self.f_priority.ToBoolean(CONTAINER_LOCAL).data
		else            :        self.f_priority.FromBoolean(CONTAINER_LOCAL, flag)


class C60_Finstruct(C50_Finstruct):
	""" Финструктура: Механика данных """
	pass

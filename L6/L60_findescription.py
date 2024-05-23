# ФИНСОСТАВ: МЕХАНИКА ДАННЫХ

from L00_containers     import CONTAINER_LOCAL
from L50_findescription import C50_RecordFindescription, C50_Findescription


class C60_RecordFindescription(C50_RecordFindescription):
	""" Запись финсостава: Механика данных """

	def Categories(self, names: list[str] = None) -> list[str]:
		""" Категории финсостава """
		if names is None: return self.f_categories.ToStrings(CONTAINER_LOCAL).items

		self.f_categories.FromStrings(CONTAINER_LOCAL, names)

	def ParentOid(self, oid: str = None) -> str:
		""" OID родительского уровня """
		if oid is None: return self.f_parent_oid.ToString(CONTAINER_LOCAL).text

		self.f_parent_oid.FromString(CONTAINER_LOCAL, oid)

	def Name(self, text: str = None) -> str:
		""" Наименование записи финсостава """
		if text is None: return self.f_name.ToString(CONTAINER_LOCAL).text

		self.f_name.FromString(CONTAINER_LOCAL, text)


class C60_Findescription(C50_Findescription):
	""" Финсостав: Механика данных """

	pass

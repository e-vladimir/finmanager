# ФИНСОСТАВ: МЕХАНИКА ДАННЫХ

from L00_containers     import CONTAINER_LOCAL
from L50_fincomposition import C50_Fincomposition


class C60_Fincomposition(C50_Fincomposition):
	""" Финсостав: Механика данных """

	def Name(self, text: str | None) -> str:
		""" Наименование """
		if text is None: return self.f_name.ToString(CONTAINER_LOCAL).data
		else           :        self.f_name.FromString(CONTAINER_LOCAL, text)

	def ParentIdo(self, ido: str | None) -> str:
		""" IDO родительского уровня """
		if ido is None: return self.f_parent_ido.ToString(CONTAINER_LOCAL).data
		else          :        self.f_parent_ido.FromString(CONTAINER_LOCAL, ido)

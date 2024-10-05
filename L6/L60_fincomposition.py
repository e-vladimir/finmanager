# ФИНСОСТАВ: МЕХАНИКА ДАННЫХ

from G30_cactus_datafilters import C30_FilterLinear1D

from L00_containers         import CONTAINER_LOCAL
from L00_fincomposition     import FINCOMPOSITION
from L50_fincomposition     import C50_Fincomposition, C50_FincompositionRecord


class C60_FincompositionRecord(C50_FincompositionRecord):
	""" Запись финсостава: Механика данных """

	# Параметры
	def Name(self, text: str = None) -> str:
		""" Наименование """
		if text is None: return self.f_name.ToString(CONTAINER_LOCAL).data
		else           :        self.f_name.FromString(CONTAINER_LOCAL, text)

	def ParentIdo(self, ido: str = None) -> str:
		""" IDO родительского уровня """
		if ido is None: return self.f_parent_ido.ToString(CONTAINER_LOCAL).data
		else          :        self.f_parent_ido.FromString(CONTAINER_LOCAL, ido)

	def Category(self, category: FINCOMPOSITION = None) -> FINCOMPOSITION:
		""" Категория финсостава """
		if category is None: return FINCOMPOSITION(self.f_category.ToString(CONTAINER_LOCAL).data)
		else               :                       self.f_category.FromString(category)

	def MarksInc(self, text: list[str] = None) -> list[str]:
		""" Признак усиления """
		if text is None: return self.f_marks_inc.ToStrings(CONTAINER_LOCAL).data
		else           :        self.f_marks_inc.FromStrings(CONTAINER_LOCAL, text)

	def MarksDec(self, text: list[str] = None) -> list[str]:
		""" Признак ослабления """
		if text is None: return self.f_marks_dec.ToStrings(CONTAINER_LOCAL).data
		else           :        self.f_marks_dec.FromStrings(CONTAINER_LOCAL, text)

	def Marks100(self, text: list[str] = None) -> list[str]:
		""" Признак подтверждения """
		if text is None: return self.f_marks_100.ToStrings(CONTAINER_LOCAL).data
		else           :        self.f_marks_100.FromStrings(CONTAINER_LOCAL, text)

	def Marks000(self, text: list[str] = None) -> list[str]:
		""" Признак отрицания """
		if text is None: return self.f_marks_000.ToStrings(CONTAINER_LOCAL).data
		else           :        self.f_marks_000.FromStrings(CONTAINER_LOCAL, text)

	# Переключение
	def SwitchByName(self, name: str) -> bool:
		""" Переключение по Наименованию """
		filter_select        = C30_FilterLinear1D(self.Idc().data)
		filter_select.FilterIdpVlpByEqual(self.f_name.Idp().data, name)
		filter_select.Capture(CONTAINER_LOCAL)

		idos     : list[str] = filter_select.Idos().data
		if not idos: return False

		self.Ido(idos[0])
		return True


class C60_Fincomposition(C50_Fincomposition):
	""" Финсостав: Механика данных """
	pass

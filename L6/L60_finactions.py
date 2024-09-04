# ФИНДЕЙСТВИЯ: МЕХАНИКА ДАННЫХ

from L00_containers import CONTAINER_LOCAL
from L50_finactions import C50_FinactionsRecord, C50_Finactions


class C60_FinactionsRecord(C50_FinactionsRecord):
	""" Запись финдействий: Механика данных """

	# Параметры
	def Dy(self, year: int = None) -> int:
		""" Год """
		if year   is None: return self.f_dy.ToInteger(CONTAINER_LOCAL).data
		else             :        self.f_dy.FromInteger(CONTAINER_LOCAL, year)

	def Dm(self, month: int = None) -> int:
		""" Месяц """
		if month  is None: return self.f_dm.ToInteger(CONTAINER_LOCAL).data
		else             :        self.f_dm.FromInteger(CONTAINER_LOCAL, month)

	def Dd(self, day: int = None) -> int:
		""" День """
		if day    is None: return self.f_dd.ToInteger(CONTAINER_LOCAL).data
		else             :        self.f_dd.FromInteger(CONTAINER_LOCAL, day)

	def SrcNote(self, text: str = None) -> str:
		""" Исходные данные: Примечание """
		if text   is None: return self.f_src_note.ToString(CONTAINER_LOCAL).data
		else             :        self.f_src_note.FromString(CONTAINER_LOCAL, text)

	def SrcAmount(self, amount: float = None) -> float:
		""" Исходные данные: Сумма """
		if amount is None: return self.f_src_amount.ToFloat(CONTAINER_LOCAL).data
		else             :        self.f_src_amount.FromFloat(CONTAINER_LOCAL, amount)

	def Note(self, text: str = None) -> str:
		""" Примечание """
		if text   is None: return self.f_note.ToString(CONTAINER_LOCAL).data
		else             :        self.f_note.FromString(CONTAINER_LOCAL, text)

	def Amount(self, amount: float = None) -> float:
		""" Сумма """
		if amount is None: return self.f_amount.ToFloat(CONTAINER_LOCAL).data
		else             :        self.f_amount.FromFloat(CONTAINER_LOCAL, amount)

	def Labels(self, items: list[str] = None) -> list[str]:
		""" Метки """
		if items  is None: return sorted(self.f_labels.ToStrings(CONTAINER_LOCAL).data)
		else             :               self.f_labels.FromStrings(CONTAINER_LOCAL, sorted(items))

	def FinstructIdos(self, items: list[str] = None) -> list[str]:
		""" Список записей финструктуры """
		if items  is None: return self.f_finstruct_idos.ToStrings(CONTAINER_LOCAL).data
		else             :        self.f_finstruct_idos.FromStrings(CONTAINER_LOCAL, items)


class C60_Finactions(C50_Finactions):
	""" Финдействия: Механика данных """
	pass

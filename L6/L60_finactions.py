# ФИНДЕЙСТВИЯ: МЕХАНИКА ДАННЫХ

from L00_containers import CONTAINER_LOCAL
from L50_finactions import C50_RecordFinactions, C50_Finactions


class C60_RecordFinactions(C50_RecordFinactions):
	""" Запись финдействий: Механика данных """

	# Параметры
	def Dy(self, year: int = None) -> int:
		""" Год """
		if year is None: return self.f_dy.ToInteger(CONTAINER_LOCAL).data

		self.f_dy.FromInteger(CONTAINER_LOCAL, year)

	def Dm(self, month: int = None) -> int:
		""" Месяц """
		if month is None: return self.f_dm.ToInteger(CONTAINER_LOCAL).data

		self.f_dm.FromInteger(CONTAINER_LOCAL, month)

	def Dd(self, day: int = None) -> int:
		""" Число """
		if day is None: return self.f_dd.ToInteger(CONTAINER_LOCAL).data

		self.f_dd.FromInteger(CONTAINER_LOCAL, day)

	def Amount(self, amount: float = None) -> int:
		""" Сумма """
		if amount is None: return self.f_amount.ToInteger(CONTAINER_LOCAL).data

		self.f_amount.FromInteger(CONTAINER_LOCAL, amount)

	def FindataIdo(self, oid: str = None) -> str:
		""" OID записи финданных """
		if oid is None: return self.f_findata_oid.ToString(CONTAINER_LOCAL).data

		self.f_findata_oid.FromString(CONTAINER_LOCAL, oid)

	def FinstructIdos(self, oids: list[str] = None) -> list[str]:
		""" Список OID записей финструктуры """
		if oids is None: return self.f_finstruct_oids.ToStrings(CONTAINER_LOCAL).data

		self.f_finstruct_oids.FromStrings(CONTAINER_LOCAL, oids)

	def FindescriptionIdos(self, oids: list[str] = None) -> list[str]:
		""" Список OID записей финсостава """
		if oids is None: return self.f_findescription_oids.ToStrings(CONTAINER_LOCAL).data

		self.f_findescription_oids.FromStrings(CONTAINER_LOCAL, oids)

	def Note(self, text: str = None) -> str:
		""" Примечание """
		if text is None: return self.f_note.ToString(CONTAINER_LOCAL).data

		self.f_note.FromString(CONTAINER_LOCAL, text)

	def Color(self, text: str = None) -> str:
		""" Цветовая метка """
		if text is None: return self.f_color.ToString(CONTAINER_LOCAL).data

		self.f_color.FromString(CONTAINER_LOCAL, text)


class C60_Finactions(C50_Finactions):
	""" Финдействия: Механика данных """
	pass

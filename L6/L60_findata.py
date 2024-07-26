# ФИНДАННЫЕ: МЕХАНИКА ДАННЫХ

from L00_containers import CONTAINER_LOCAL

from L50_findata    import C50_RecordFindata, C50_Findata


class C60_RecordFindata(C50_RecordFindata):
	""" Запись финданные: Механика данных """

	# Параметры
	def Dy(self, year: int = None) -> int:
		""" Год """
		if year is None  : return self.f_dy.ToInteger(CONTAINER_LOCAL).data
		else             :        self.f_dy.FromInteger(CONTAINER_LOCAL, year)

	def Dm(self, month: int = None) -> int:
		""" Месяц """
		if month is None : return self.f_dm.ToInteger(CONTAINER_LOCAL).data
		else             :        self.f_dm.FromInteger(CONTAINER_LOCAL, month)

	def Dd(self, day: int = None) -> int:
		""" Число """
		if day is None   : return self.f_dd.ToInteger(CONTAINER_LOCAL).data
		else             :        self.f_dd.FromInteger(CONTAINER_LOCAL, day)

	def Amount(self, amount: float = None) -> float:
		""" Сумма """
		if amount is None: return self.f_amount.ToFloat(CONTAINER_LOCAL).data
		else             :        self.f_amount.FromFloat(CONTAINER_LOCAL, amount)

	def UID(self, text: str = None) -> str:
		""" UID записи """
		if text is None  : return self.f_uid.ToString(CONTAINER_LOCAL).data
		else             :        self.f_uid.FromString(CONTAINER_LOCAL, text)

	def FinstructIdo(self, ido: str = None) -> str:
		""" OID записи финструктуры """
		if ido is None   : return self.f_finstruct_ido.ToString(CONTAINER_LOCAL).data
		else             :        self.f_finstruct_ido.FromString(CONTAINER_LOCAL, ido)

	def Note(self, text: str = None) -> str:
		""" Примечание """
		if text is None  : return self.f_note.ToString(CONTAINER_LOCAL).data
		else             :        self.f_note.FromString(CONTAINER_LOCAL, text)


class C60_Findata(C50_Findata):
	""" Финданные: Механика данных """
	pass

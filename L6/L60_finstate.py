# ФИНСОСТОЯНИЕ: МЕХАНИКА ДАННЫХ

from L00_containers import CONTAINER_LOCAL

from L50_finstate   import C50_RecordFinstate, C50_Finstate


class C60_RecordFinstate(C50_RecordFinstate):
	""" Запись финсостояния: Механика данных """

	def FinstructIdo(self, ido: str = None) -> str:
		""" OID записи финструктуры """
		if ido is None: return self.f_finstruct_ido.ToString(CONTAINER_LOCAL).data

		self.f_finstruct_ido.FromString(CONTAINER_LOCAL, ido)

	def RemainsInitial(self, amount: int = None) -> int:
		""" Остаток начальный """
		if amount is None: return self.f_remains_initial.ToInteger(CONTAINER_LOCAL).data

		self.f_remains_initial.FromInteger(CONTAINER_LOCAL, amount)


class C60_Finstate(C50_Finstate):
	""" Финсостояние: Механика данных """
	pass

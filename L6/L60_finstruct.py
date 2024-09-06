# ФИНСТРУКТУРА: МЕХАНИКА ДАННЫХ
from G30_cactus_datafilters import C30_FilterLinear1D
from L00_containers import CONTAINER_LOCAL
from L50_finstruct  import C50_FinstructRecord, C50_Finstruct


class C60_FinstructRecord(C50_FinstructRecord):
	""" Запись финструктуры: Механика данных """

	# Параметры
	def Dy(self, year: int = None) -> int:
		""" Год """
		if year  is None: return self.f_dy.ToInteger(CONTAINER_LOCAL).data
		else            :        self.f_dy.FromInteger(CONTAINER_LOCAL, year)

	def Dm(self, month: int = None) -> int:
		""" Месяц """
		if month is None: return self.f_dm.ToInteger(CONTAINER_LOCAL).data
		else            :        self.f_dm.FromInteger(CONTAINER_LOCAL, month)

	def Name(self, text: str = None) -> str:
		""" Наименование """
		if text  is None: return self.f_name.ToString(CONTAINER_LOCAL).data
		else            :        self.f_name.FromString(CONTAINER_LOCAL, text)

	def Group(self, text: str = None) -> str:
		""" Группа счетов """
		if text  is None: return self.f_group.ToString(CONTAINER_LOCAL).data
		else            :        self.f_group.FromString(CONTAINER_LOCAL, text)

	def BalanceStart(self, value: float = None) -> float:
		""" Баланс начальный """
		if value is None: return self.f_balance_start.ToFloat(CONTAINER_LOCAL).data
		else            :        self.f_balance_start.FromFloat(CONTAINER_LOCAL, value)

	# Переключение
	def SwitchByName(self, dy: int, dm: int, name: str) -> bool:
		""" Переключение по Наименованию """
		filter_select        = C30_FilterLinear1D(self.Idc().data)
		filter_select.FilterIdpVlpByEqual(self.f_name.Idp().data, name)
		filter_select.FilterIdpVlpByEqual(self.f_dy.Idp().data, dy)
		filter_select.FilterIdpVlpByEqual(self.f_dm.Idp().data, dm)
		filter_select.Capture(CONTAINER_LOCAL)

		idos     : list[str] = filter_select.Idos().data
		if not idos: return False

		self.Ido(idos[0])
		return True


class C60_Finstruct(C50_Finstruct):
	""" Финструктура: Механика данных """
	pass

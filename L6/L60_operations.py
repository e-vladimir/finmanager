# ФИНАНСОВЫЕ ОПЕРАЦИИ: МЕХАНИКА ДАННЫХ
from L00_colors import COLORS
from L00_containers import CONTAINERS
from L50_operations import C50_Operation, C50_Operations


class C60_Operation(C50_Operation):
	""" Финансовая операция: Механика данных """

	# Параметры
	def Dy(self, year: int = None) -> int:
		""" Год """
		if year is None  : return self.f_dy.ToInteger(CONTAINERS.DISK).data
		else             :        self.f_dy.FromInteger(CONTAINERS.DISK, year)

	def Dm(self, month: int = None) -> int:
		""" Месяц """
		if month is None : return self.f_dm.ToInteger(CONTAINERS.DISK).data
		else             :        self.f_dm.FromInteger(CONTAINERS.DISK, month)

	def Dd(self, day: int = None) -> int:
		""" День """
		if day is None   : return self.f_dd.ToInteger(CONTAINERS.DISK).data
		else             :        self.f_dd.FromInteger(CONTAINERS.DISK, day)

	def Crc(self, data: str = None) -> str:
		""" CRC """
		if data is None  : return self.f_crc.ToString(CONTAINERS.DISK).data
		else             :        self.f_crc.FromString(CONTAINERS.DISK, data)

	def Amount(self, value: int = None) -> int:
		""" Сумма """
		if value is None : return self.f_amount.ToInteger(CONTAINERS.DISK).data
		else             :        self.f_amount.FromInteger(CONTAINERS.DISK, value)

	def SrcAmount(self, value: int = None) -> int:
		""" Исходная сумма """
		if value is None : return self.f_src_amount.ToInteger(CONTAINERS.DISK).data
		else             :        self.f_src_amount.FromInteger(CONTAINERS.DISK, value)

	def Description(self, text: str = None) -> str:
		""" Описание """
		if text is None  : return self.f_description.ToString(CONTAINERS.DISK).data
		else             :        self.f_description.FromString(CONTAINERS.DISK, text)

	def SrcDescription(self, text: str = None) -> str:
		""" Исходное описание """
		if text is None  : return self.f_src_description.ToString(CONTAINERS.DISK).data
		else             :        self.f_src_description.FromString(CONTAINERS.DISK, text)

	def Labels(self, labels: list[str] = None) -> list[str]:
		""" Метки """
		if labels is None: return list(sorted(self.f_labels.ToStrings(CONTAINERS.DISK).data))
		else             :        self.f_labels.FromStrings(CONTAINERS.DISK, sorted(labels))

	def AccountsIdos(self, idos: list[str] = None) -> list[str]:
		""" Список IDO счетов """
		if idos is None  : return self.f_accounts_idos.ToStrings(CONTAINERS.DISK).data
		else             :        self.f_accounts_idos.FromString(CONTAINERS.DISK, idos)

	def Color(self, color: COLORS = None) -> COLORS:
		""" Цветовая метка """
		if color is None : return COLORS(self.f_color.ToString(CONTAINERS.DISK).data)
		else             :        self.f_color.FromString(CONTAINERS.DISK, color)


class C60_Operations(C50_Operations):
	""" Финансовые операции: Механика данных """
	pass

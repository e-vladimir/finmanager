# ФИНДЕЙСТВИЯ: ЛОГИКА ДАННЫХ

from G30_cactus_datafilters import C30_FilterLinear1D

from L00_colors             import *
from L00_containers         import CONTAINER_LOCAL
from L00_months             import MONTHS_SHORT
from L00_rules_types        import *

from L60_findata            import C60_RecordFindata
from L70_finactions         import C70_RecordFinactions, C70_Finactions
from L90_findescription     import C90_RecordFindescription
from L90_finstruct          import C90_RecordFinstruct
from L90_processing_rules   import C90_ProcessingRules, C90_RecordProcessingRules


class C80_RecordFinactions(C70_RecordFinactions):
	""" Запись финданные: Логика данных """

	# Цветовая метка
	def Color_Black(self, flag: bool = None) -> bool:
		""" Цветовая метка: Черный """
		if flag is None: return self.Color() == COLOR_BLACK

		self.Color(COLOR_BLACK)

	def Color_Gray(self, flag: bool = None) -> bool:
		""" Цветовая метка: Серый """
		if flag is None: return self.Color() == COLOR_GRAY

		self.Color(COLOR_GRAY)

	def Color_Red(self, flag: bool = None) -> bool:
		""" Цветовая метка: Красный """
		if flag is None: return self.Color() == COLOR_RED

		self.Color(COLOR_RED)

	def Color_Green(self, flag: bool = None) -> bool:
		""" Цветовая метка: Зелёный """
		if flag is None: return self.Color() == COLOR_GREEN

		self.Color(COLOR_GREEN)

	def Color_Blue(self, flag: bool = None) -> bool:
		""" Цветовая метка: Синий """
		if flag is None: return self.Color() == COLOR_BLUE

		self.Color(COLOR_BLUE)

	# Вывод информации
	def DdDmDyToString(self) -> str:
		""" Преобразование числа, месяца, года в строку """
		return f"{self.Dd():02d} {MONTHS_SHORT[self.Dm()]} {self.Dy()}"

	def DdDmToString(self) -> str:
		""" Преобразование числа, месяца в строку """
		return f"{self.Dd():02d} {MONTHS_SHORT[self.Dm()]}"

	def DmDyToString(self) -> str:
		""" Преобразование месяца, числа в строку """
		return f"{MONTHS_SHORT[self.Dm()]} {self.Dy()}"

	# Управление финструктурой
	def ExcludeFinstructByName(self, text: str):
		""" Исключение финструктуры из записи """
		dy             : int       = self.Dy()
		dm             : int       = self.Dm()

		record_finstruct = C90_RecordFinstruct()
		if not record_finstruct.SwitchByName(dy, dm, text): return

		finstruct_ido  : str       = record_finstruct.Ido().data
		finstruct_idos : list[str] = self.FinstructIdos()

		if finstruct_ido not in finstruct_idos: return

		finstruct_idos.remove(finstruct_ido)

		self.FinstructIdos(finstruct_idos)

	def IncludeFinstructByName(self, text: str):
		""" Включение финструктуры в запись """
		dy             : int       = self.Dy()
		dm             : int       = self.Dm()

		record_finstruct = C90_RecordFinstruct()
		if not record_finstruct.SwitchByName(dy, dm, text): return

		finstruct_ido  : str       = record_finstruct.Ido().data
		finstruct_idos : list[str] = self.FinstructIdos()

		if finstruct_ido in finstruct_idos: return

		finstruct_idos.append(finstruct_ido)

		self.FinstructIdos(finstruct_idos)

	# Управление финсоставом
	def ExcludeFindescriptionByName(self, text: str):
		""" Исключение финсостава из записи """
		record_findescription = C90_RecordFindescription()
		if not record_findescription.SwitchByName(text): return

		findescription_ido  : str       = record_findescription.Ido().data
		findescription_idos : list[str] = self.FindescriptionIdos()

		if findescription_ido not in findescription_idos: return

		findescription_idos.remove(findescription_ido)

		self.FindescriptionIdos(findescription_idos)

	def IncludeFindescriptionByName(self, text: str):
		""" Включение финструктуры в запись """
		record_findescription = C90_RecordFindescription()
		if not record_findescription.SwitchByName(text): return

		findescription_ido  : str       = record_findescription.Ido().data
		findescription_idos : list[str] = self.FindescriptionIdos()

		if findescription_ido in findescription_idos: return

		findescription_idos.append(findescription_ido)

		self.FindescriptionIdos(findescription_idos)

	# Правила обработки данных
	def ApplyRulesDetectFindescription(self):
		""" Применить правила определения финсостава """
		result : list[str] = self.FindescriptionIdos()

		rules        = C90_ProcessingRules()
		for ido in rules.IdosByType(RULE_DETECT_FINDESCRIPTION_BY_TEXT):
			record_rule              = C90_RecordProcessingRules(ido)
			ido_findescription : str = record_rule.ExecDetectFindescription(self.Note())
			if not ido_findescription: continue

			result.append(ido_findescription)

		result = list(set(result))

		self.FindescriptionIdos(result)


class C80_Finactions(C70_Finactions):
	""" Финданные: Логика данных """

	# Выборка данных
	def IdosInDyDmDd(self, dy: int, dm: int, dd: int = None) -> list[str]:
		""" Выборка OID записей финданных """
		filter_findata = C30_FilterLinear1D(self._idc)
		filter_findata.FilterIdpVlpByEqual(self._idp_dy, dy)
		filter_findata.FilterIdpVlpByEqual(self._idp_dm, dm)

		if dd is not None:
			filter_findata.FilterIdpVlpByEqual(self._idp_dd, dd)

		filter_findata.Capture(CONTAINER_LOCAL)

		return filter_findata.Idos(self._idp_amount).data

	def Dds(self, dy: int, dm: int) -> list[int]:
		""" Выборка OID записей финданных """
		filter_findata = C30_FilterLinear1D(self._idc)
		filter_findata.FilterIdpVlpByEqual(self._idp_dy, dy)
		filter_findata.FilterIdpVlpByEqual(self._idp_dm, dm)

		filter_findata.Capture(CONTAINER_LOCAL)

		return filter_findata.ToIntegers(self._idp_dd, True, True).data

	# Преобразование записей
	def CreateFinactionsFromFindata(self, ido: str, amount: int = None) -> str:
		""" Создание записи финдействий из записи финданных """
		record_findata    = C60_RecordFindata(ido)
		record_finactions = C80_RecordFinactions()

		dy : int          = record_findata.Dy()
		dm : int          = record_findata.Dm()
		dd : int          = record_findata.Dd()

		if not dy: return ""
		if not dm: return ""
		if not dd: return ""

		record_finactions.GenerateIdo()
		record_finactions.RegisterObject(CONTAINER_LOCAL)

		record_finactions.FindataIdo(ido)

		record_finactions.Dy(dy)
		record_finactions.Dm(dm)
		record_finactions.Dd(dd)

		record_finactions.Note(record_findata.Note())

		record_finactions.ApplyRulesDetectFindescription()

		if amount is not None:
			record_finactions.Amount(amount)

		return record_finactions.Ido().data

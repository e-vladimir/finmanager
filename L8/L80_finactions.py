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

		finstruct_oid  : str       = record_finstruct.Oid().text
		finstruct_oids : list[str] = self.FinstructOids()

		if finstruct_oid not in finstruct_oids: return

		finstruct_oids.remove(finstruct_oid)

		self.FinstructOids(finstruct_oids)

	def IncludeFinstructByName(self, text: str):
		""" Включение финструктуры в запись """
		dy             : int       = self.Dy()
		dm             : int       = self.Dm()

		record_finstruct = C90_RecordFinstruct()
		if not record_finstruct.SwitchByName(dy, dm, text): return

		finstruct_oid  : str       = record_finstruct.Oid().text
		finstruct_oids : list[str] = self.FinstructOids()

		if finstruct_oid in finstruct_oids: return

		finstruct_oids.append(finstruct_oid)

		self.FinstructOids(finstruct_oids)

	# Управление финсоставом
	def ExcludeFindescriptionByName(self, text: str):
		""" Исключение финсостава из записи """
		record_findescription = C90_RecordFindescription()
		if not record_findescription.SwitchByName(text): return

		findescription_oid  : str       = record_findescription.Oid().text
		findescription_oids : list[str] = self.FindescriptionOids()

		if findescription_oid not in findescription_oids: return

		findescription_oids.remove(findescription_oid)

		self.FindescriptionOids(findescription_oids)

	def IncludeFindescriptionByName(self, text: str):
		""" Включение финструктуры в запись """
		record_findescription = C90_RecordFindescription()
		if not record_findescription.SwitchByName(text): return

		findescription_oid  : str       = record_findescription.Oid().text
		findescription_oids : list[str] = self.FindescriptionOids()

		if findescription_oid in findescription_oids: return

		findescription_oids.append(findescription_oid)

		self.FindescriptionOids(findescription_oids)

	# Правила обработки данных
	def ApplyRulesDetectFindescription(self):
		""" Применить правила определения финсостава """
		result : list[str] = self.FindescriptionOids()

		rules        = C90_ProcessingRules()
		for oid in rules.OidsByType(RULE_DETECT_FINDESCRIPTION_BY_TEXT):
			record_rule              = C90_RecordProcessingRules(oid)
			oid_findescription : str = record_rule.ExecDetectFindescription(self.Note())
			if not oid_findescription: continue

			result.append(oid_findescription)

		result = list(set(result))

		self.FindescriptionOids(result)


class C80_Finactions(C70_Finactions):
	""" Финданные: Логика данных """

	# Выборка данных
	def OidsInDyDmDd(self, dy: int, dm: int, dd: int = None) -> list[str]:
		""" Выборка OID записей финданных """
		filter_findata = C30_FilterLinear1D(self._oci)
		filter_findata.FilterPidCvlByEqual(self._pid_dy, dy)
		filter_findata.FilterPidCvlByEqual(self._pid_dm, dm)

		if dd is not None:
			filter_findata.FilterPidCvlByEqual(self._pid_dd, dd)

		filter_findata.Capture(CONTAINER_LOCAL)

		return filter_findata.Oids(self._pid_amount).items

	def Dds(self, dy: int, dm: int) -> list[int]:
		""" Выборка OID записей финданных """
		filter_findata = C30_FilterLinear1D(self._oci)
		filter_findata.FilterPidCvlByEqual(self._pid_dy, dy)
		filter_findata.FilterPidCvlByEqual(self._pid_dm, dm)

		filter_findata.Capture(CONTAINER_LOCAL)

		return filter_findata.ToIntegers(self._pid_dd, True, True).items

	# Преобразование записей
	def CreateFinactionsFromFindata(self, oid: str, amount: int = None) -> str:
		""" Создание записи финдействий из записи финданных """
		record_findata    = C60_RecordFindata(oid)
		record_finactions = C80_RecordFinactions()

		dy : int          = record_findata.Dy()
		dm : int          = record_findata.Dm()
		dd : int          = record_findata.Dd()

		if not dy: return ""
		if not dm: return ""
		if not dd: return ""

		record_finactions.GenerateOid()
		record_finactions.RegisterObject(CONTAINER_LOCAL)

		record_finactions.FindataOid(oid)

		record_finactions.Dy(dy)
		record_finactions.Dm(dm)
		record_finactions.Dd(dd)

		record_finactions.Note(record_findata.Note())

		record_finactions.ApplyRulesDetectFindescription()

		if amount is not None:
			record_finactions.Amount(amount)

		return record_finactions.Oid().text

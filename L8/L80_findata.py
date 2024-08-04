# ФИНДАННЫЕ: ЛОГИКА ДАННЫХ

from hashlib                import md5

from G10_convertor_format import StringToFloat
from G30_cactus_datafilters import C30_FilterLinear1D

from L00_containers         import CONTAINER_LOCAL
from L00_formats            import *
from L00_months             import MONTHS_SHORT
from L00_rules_types        import RULE_REPLACE_TEXT

from L40_finactions         import C40_RecordFinactions
from L70_findata            import C70_RecordFindata, C70_Findata
from L90_processing_rules   import C90_ProcessingRules, C90_RecordProcessingRules


class C80_RecordFindata(C70_RecordFindata):
	""" Запись финданные: Логика данных """

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

	# Контроль
	def CheckRecordIsManual(self) -> bool:
		""" Запись является ручной """
		return not bool(self.UID())

	# Выборки данных
	def LinkedFinactionsIdos(self) -> list[str]:
		""" Взаимосвязи с финдействиями """
		record_finactions = C40_RecordFinactions()
		oci         : str = record_finactions.Idc().data
		idp_findata : str = record_finactions.f_findata_ido.Idp().data
		idp_amount  : str = record_finactions.f_amount.Idp().data

		filter_findata    = C30_FilterLinear1D(oci)
		filter_findata.FilterIdpVlpByEqual(idp_findata, self.Ido().data)

		filter_findata.Capture(CONTAINER_LOCAL)

		return filter_findata.Idos(idp_amount).data

	def CalcAmountDeviationByLinks(self) -> int:
		""" Расчёт суммы взаимосвязанных записей """
		record_finactions = C40_RecordFinactions()
		oci         : str = record_finactions.Idc().data
		idp_findata : str = record_finactions.f_findata_ido.Idp().data
		idp_amount  : str = record_finactions.f_amount.Idp().data

		filter_findata    = C30_FilterLinear1D(oci)
		filter_findata.FilterIdpVlpByEqual(idp_findata, self.Ido().data)

		filter_findata.Capture(CONTAINER_LOCAL)

		amounts : list[int] = filter_findata.ToIntegers(idp_amount).data

		return int(self.Amount() - sum(amounts))

	# Экспорт в формат CSV Финорганайзер
	def ExportToCsv(self) -> str:
		""" Экспорт в формат Финорганайзер CSV """
		data : list[str] = []
		data.append(f"{self.Dy():04d}-{self.Dm():02d}-{self.Dd():02d}")
		data.append(f"{self.Amount():0.2f}")
		data.append(f"{self.Note()}")

		return ';'.join(data)

	# Правила обработки данных
	def ApplyRulesReplaceText(self):
		""" Применение правила замены текстовых фрагментов """
		result : str = self.Note()

		rules        = C90_ProcessingRules()
		for ido in rules.IdosByType(RULE_REPLACE_TEXT):
			record_rule = C90_RecordProcessingRules(ido)
			result      = record_rule.ExecReplaceText(result)

		self.Note(result)


class C80_Findata(C70_Findata):
	""" Финданные: Логика данных """

	# Выборка данных
	def IdosInDyDmDd(self, dy: int, dm: int = None, dd: int = None) -> list[str]:
		""" Выборка OID записей финданных """
		filter_findata = C30_FilterLinear1D(self._idc)
		filter_findata.FilterIdpVlpByEqual(self._idp_dy, dy)

		if dm is not None:
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

	# Запросы
	def CheckFindataByUid(self, uid: str) -> bool:
		""" Проверка наличия записи финданных по UID """
		filter_findata = C30_FilterLinear1D(self._idc)
		filter_findata.FilterIdpVlpByEqual(self._idp_uid, uid)

		filter_findata.Capture(CONTAINER_LOCAL)

		return not (filter_findata.Idos().data == [])

	# Импорт финданных
	def ImportFindataFromCsvTinkoff(self, data_raw: str, finstruct_ido: str, dy: int, dm: int, dd: int = None) -> bool:
		""" Импорт записи финданных из формата Тинькофф CSV """
		items_raw        : list[str] = data_raw.replace('"', '').split(';')

		raw_dydmddthtmts : str       = items_raw[ 0]
		raw_card         : str       = items_raw[ 2]
		raw_state        : str       = items_raw[ 3]
		raw_amount       : str       = items_raw[ 4]
		raw_note         : str       = items_raw[11]

		uid_record       : str       = f"{finstruct_ido} {raw_dydmddthtmts} {raw_card} {raw_amount}"
		uid_record                   = uid_record.replace('.', '')
		uid_record                   = uid_record.replace(',', '')
		uid_record                   = uid_record.replace(':', '')
		uid_record                   = uid_record.replace(' ', '')
		uid_record                   = md5(uid_record.encode()).hexdigest()

		if not raw_state == "OK"                 : return False
		if     self.CheckFindataByUid(uid_record): return False

		raw_dydmdd       : list[str] = raw_dydmddthtmts.split(' ')[0].split('.')
		raw_dy           : int       = int(raw_dydmdd[2])
		raw_dm           : int       = int(raw_dydmdd[1])
		raw_dd           : int       = int(raw_dydmdd[0])
		raw_amount       : float     = StringToFloat(raw_amount)

		if not dy == raw_dy                      : return False
		if not dm == raw_dm                      : return False
		if dd is not None:
			if not dd == raw_dd                  : return False

		findata_record               = C80_RecordFindata()
		findata_record.GenerateIdo()
		findata_record.RegisterObject(CONTAINER_LOCAL)

		findata_record.UID(uid_record)
		findata_record.Dy(raw_dy)
		findata_record.Dm(raw_dm)
		findata_record.Dd(raw_dd)
		findata_record.Amount(raw_amount)
		findata_record.FinstructIdo(finstruct_ido)
		findata_record.Note(raw_note)

		findata_record.ApplyRulesReplaceText()

		return True

	def ImportFindataFromCsvSberbank(self, data_raw: str, finstruct_ido: str, dy: int, dm: int, dd: int = None) -> bool:
		""" Импорт записи финданных из формата Сбербанк CSV """
		items_raw        : list[str] = data_raw.split(';')

		raw_number       : str       = items_raw[ 0]
		raw_dydmddthtm   : str       = items_raw[ 1]
		raw_type         : str       = items_raw[ 2]
		raw_amount       : str       = items_raw[ 4]
		raw_note         : str       = items_raw[ 7]
		raw_code         : str       = items_raw[ 8]

		uid_record       : str       = f"{raw_number}{raw_dydmddthtm}{raw_amount}"
		uid_record                   = uid_record.replace('.', '')
		uid_record                   = uid_record.replace(':', '')
		uid_record                   = uid_record.replace(' ', '')

		if     self.CheckFindataByUid(uid_record): return False
		if not raw_code == "Активная"            : return False

		months : dict[str, int] = {"января"  :  1,
		                           "февраля" :  2,
		                           "марта"   :  3,
		                           "апреля"  :  4,
		                           "мая"     :  5,
		                           "июня"    :  6,
		                           "июля"    :  7,
		                           "августа" :  8,
		                           "сентября":  9,
		                           "октября" : 10,
		                           "ноября"  : 11,
		                           "декабря" : 12}

		raw_dddmdy       : list[str] = raw_dydmddthtm.split(',')[0].split(' ')
		raw_dd           : int       = int(raw_dddmdy[0])
		raw_dm           : int       = months.get(raw_dddmdy[1], 0)
		raw_dy           : int       = int(raw_dddmdy[2])

		if     raw_dm == 0                       : return False

		raw_amount       : float     = StringToFloat(raw_amount) * (-1 if raw_type == "Расходы" else 1)

		if not dy == raw_dy                      : return False
		if not dm == raw_dm                      : return False
		if dd is not None:
			if not dd == raw_dd                  : return False

		findata_record               = C80_RecordFindata()
		findata_record.GenerateIdo()
		findata_record.RegisterObject(CONTAINER_LOCAL)

		findata_record.UID(uid_record)
		findata_record.Dy(raw_dy)
		findata_record.Dm(raw_dm)
		findata_record.Dd(raw_dd)
		findata_record.Amount(raw_amount)
		findata_record.FinstructIdo(finstruct_ido)
		findata_record.Note(raw_note)

		findata_record.ApplyRulesReplaceText()

		return True

	def ImportFindataFromCsv(self, data_raw: str, format_csv: str, finstruct_ido: str, dy: int, dm: int, dd: int = None) -> bool:
		""" Импорт финданных из формата CSV """
		if   format_csv == FORMAT_TINKOFF : return self.ImportFindataFromCsvTinkoff(data_raw, finstruct_ido, dy, dm, dd)
		elif format_csv == FORMAT_SBERBANK: return self.ImportFindataFromCsvSberbank(data_raw, finstruct_ido, dy, dm, dd)

		return False

	# Удаление записей
	def DeleteRecordsFindata(self, idos: list[str]):
		""" Удаление записей финданных с зависимостями """
		for ido in idos:
			record_findata = C80_RecordFindata(ido)
			record_findata.DeleteObject(CONTAINER_LOCAL)

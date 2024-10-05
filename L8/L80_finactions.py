# ФИНДЕЙСТВИЯ: ЛОГИКА ДАННЫХ

from G30_cactus_datafilters import C30_FilterLinear1D

from L00_containers         import CONTAINER_LOCAL
from L00_months             import MONTHS_SHORT
from L00_rules              import RULES
from L70_finactions         import C70_FinactionsRecord, C70_Finactions
from L90_rules              import C90_ProcessingRules, C90_ProcessingRulesRecord


class C80_FinactionsRecord(C70_FinactionsRecord):
	""" Запись финдействий: Логика данных """

	# Генерация данных
	def DdDmDyToString(self) -> str:
		""" Число Месяц Год в строку """
		return f"{self.Dd():02d} {MONTHS_SHORT[self.Dm()]} {self.Dy()}"

	# Действия
	def SplitAmount(self, amount: int) -> str:
		""" Разделение записи финдействий """
		self.Amount(self.Amount() - amount)

		record = C80_FinactionsRecord()
		record.GenerateIdo()
		record.RegisterObject(CONTAINER_LOCAL)

		record.Dy(self.Dy())
		record.Dm(self.Dm())
		record.Dd(self.Dd())

		record.SrcAmount(self.SrcAmount())
		record.SrcDescription(self.SrcDescription())

		record.Amount(amount)

		record.Description(self.Description())
		record.FinstructIdos(self.FinstructIdos())

		return record.Ido().data

	# Правила обработки данных
	def ApplyProcessingRulesReplaceText(self):
		""" Применить правила замены текстовых фрагментов """
		description : str = self.Description()
		rules      = C90_ProcessingRules()

		for ido_rule in rules.IdosByType(RULES.REPLACE_TEXT):
			rule                        = C90_ProcessingRulesRecord(ido_rule)
			fragment_output : str       = rule.OptionsOutputAsString()
			fragments_input : list[str] = rule.OptionsInputAsStrings()
			fragments_input.sort(key=len)

			for fragment_input in fragments_input:
				if not fragment_input            : continue
				if     fragment_input not in description: continue

				description = description.replace(fragment_input, fragment_output)

		if description == self.Description(): return

		self.Description(description)


class C80_Finactions(C70_Finactions):
	""" Финдействия: Логика данных """

	# Выборки данных
	def IdosInDyDmDd(self, dy: int, dm: int = None, dd: int = None, finstruct_ido: str = None) -> list[str]:
		""" Список IDO в указанном периоде """
		record            = C80_FinactionsRecord()

		filter_finactions = C30_FilterLinear1D(record.Idc().data)
		filter_finactions.FilterIdpVlpByEqual(record.f_dy.Idp().data, dy)

		if dm            is not None: filter_finactions.FilterIdpVlpByEqual(record.f_dm.Idp().data, dm)
		if dd            is not None: filter_finactions.FilterIdpVlpByEqual(record.f_dd.Idp().data, dd)
		if finstruct_ido is not None: filter_finactions.FilterIdpVlpByInclude(record.f_finstruct_idos.Idp().data, finstruct_ido)

		filter_finactions.Capture(CONTAINER_LOCAL)

		return filter_finactions.Idos(record.f_amount.Idp().data).data

	def DdsInDyDm(self, dy: int, dm: int) -> list[int]:
		""" Список дней в периоде """
		record            = C80_FinactionsRecord()

		filter_finactions = C30_FilterLinear1D(record.Idc().data)
		filter_finactions.FilterIdpVlpByEqual(record.f_dy.Idp().data, dy)
		filter_finactions.FilterIdpVlpByEqual(record.f_dm.Idp().data, dm)

		filter_finactions.Capture(CONTAINER_LOCAL)

		return filter_finactions.ToIntegers(record.f_dd.Idp().data, flag_distinct=True, flag_sort=True).data

	def AvailableDys(self) -> list[int]:
		""" Список годов для записей финдействий """
		record      = C80_FinactionsRecord()

		filter_data = C30_FilterLinear1D(record.Idc().data)
		filter_data.Capture(CONTAINER_LOCAL)

		return filter_data.ToIntegers(record.f_dy.Idp().data, True, True).data

	# Запись финданных
	def CreateRecord(self, dy: int, dm: int, dd: int, amount: float = 0.00) -> str:
		""" Создание записи финдействий """
		record = C80_FinactionsRecord()
		record.GenerateIdo()
		record.RegisterObject(CONTAINER_LOCAL)

		record.Dy(dy)
		record.Dm(dm)
		record.Dd(dd)
		record.SrcDescription("")
		record.SrcAmount(0.00)
		record.Description("")
		record.Amount(amount)
		record.FinstructIdos([])
		record.Color("")

		return record.Ido().data

	def ImportRecord(self, finstruct_ido: str, src_date_time: str, src_amount: str, src_description: str, src_control: str, control_dy: int = 0, control_dm: int = 0, control_dd: int = 0):
		""" Импорт записи финдействий """
		if not src_date_time: return

		dy     : int   = 0
		dm     : int   = 0
		dd     : int   = 0

		amount : float = 0.00

		try   : amount = float(src_amount.replace(',', '.'))
		except: pass

		try:
			raw   : str    = src_date_time.lower()
			raw            = raw.replace(',', '')
			raw            = raw.replace('.', ' ')
			raw            = raw.replace('ё', 'е')

			months         = []
			months.append(["январь",   "января",   "янв"])
			months.append(["февраль",  "февраля",  "фев"])
			months.append(["марта",    "март",     "мар"])
			months.append(["апрель",   "апреля",   "апр"])
			months.append(["май",      "мая",      "май"])
			months.append(["июнь",     "июня",     "июн"])
			months.append(["июль",     "июля",     "июл"])
			months.append(["августа",  "август",   "авг"])
			months.append(["сентябрь", "сентября", "сен"])
			months.append(["октябрь",  "октября",  "окт"])
			months.append(["ноябрь",   "ноября",   "ноя"])
			months.append(["декабрь",  "декабря",  "дек"])

			for index_month, submonths in enumerate(months):
				for month in submonths: raw = raw.replace(month, f"{index_month + 1:02d}")

			dddmdy : list[str] = raw.split(' ')
			dddmdy             = list(filter(lambda subraw: len(subraw) < 5, dddmdy))

			dd                 = int(dddmdy[0])
			dm                 = int(dddmdy[1])
			dy                 = int(dddmdy[2])

			if   dy <  50: dy += 2000
			elif dy < 100: dy += 1900
		except: pass

		if not dy           : return
		if not dm           : return
		if not dd           : return

		if control_dy and not (control_dy == dy): return
		if control_dm and not (control_dm == dm): return
		if control_dd and not (control_dm == dd): return

		control_text = src_control.lower()

		if   "err"    in control_text: return
		elif "ошибка" in control_text: return
		elif "отказ"  in control_text: return

		record         = C80_FinactionsRecord()
		record.GenerateIdo()
		record.RegisterObject(CONTAINER_LOCAL)

		description = src_description.replace('  ', ' ')

		record.Dy(dy)
		record.Dm(dm)
		record.Dd(dd)
		record.SrcDescription(description)
		record.SrcAmount(amount)
		record.Description(description)
		record.Amount(amount)
		record.FinstructIdos([finstruct_ido])
		record.Color("")

		record.ApplyProcessingRulesReplaceText()

# ФИНДЕЙСТВИЯ: ЛОГИКА ДАННЫХ

from G30_cactus_datafilters import C30_FilterLinear1D

from L00_containers         import CONTAINER_LOCAL
from L00_months             import MONTHS_SHORT
from L70_finactions         import C70_FinactionsRecord, C70_Finactions


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
		record.SrcNote(self.SrcNote())

		record.Uid(self.Uid())

		record.Amount(amount)

		record.Note(self.Note())
		record.FinstructIdos(self.FinstructIdos())
		record.Labels(self.Labels())

		return record.Ido().data


class C80_Finactions(C70_Finactions):
	""" Финдействия: Логика данных """

	# Выборки данных
	def IdosInDyDmDd(self, dy: int, dm: int = None, dd: int = None) -> list[str]:
		""" Список IDO в указанном периоде """
		record            = C80_FinactionsRecord()

		filter_finactions = C30_FilterLinear1D(record.Idc().data)
		filter_finactions.FilterIdpVlpByEqual(record.f_dy.Idp().data, dy)

		if dm is not None: filter_finactions.FilterIdpVlpByEqual(record.f_dm.Idp().data, dm)
		if dd is not None: filter_finactions.FilterIdpVlpByEqual(record.f_dd.Idp().data, dd)

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

	# Запись финданных
	def CreateRecord(self, dy: int, dm: int, dd: int, amount: float = 0.00) -> str:
		""" Создание записи финдействий """
		record = C80_FinactionsRecord()
		record.GenerateIdo()
		record.RegisterObject(CONTAINER_LOCAL)

		record.Dy(dy)
		record.Dm(dm)
		record.Dd(dd)
		record.SrcNote("")
		record.SrcAmount(0.00)
		record.Note("")
		record.Amount(amount)
		record.Labels([])
		record.FinstructIdos([])

		return record.Ido().data

	def ImportRecord(self, finstruct_ido: str, src_date_time: str, src_amount: str, src_note: str, src_control: str, control_dy: int = 0, control_dm: int = 0, control_dd: int = 0):
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

		record         = C80_FinactionsRecord()
		record.GenerateIdo()
		record.RegisterObject(CONTAINER_LOCAL)

		record.Dy(dy)
		record.Dm(dm)
		record.Dd(dd)
		record.SrcNote(src_note)
		record.SrcAmount(amount)
		record.Note("")
		record.Amount(amount)
		record.Labels([])
		record.FinstructIdos([finstruct_ido])

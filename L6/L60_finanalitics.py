# ФИНАНАЛИТИКА: МЕХАНИКА ДАННЫХ

from statistics             import mean

from G30_cactus_datafilters import C30_FilterLinear1D

from L00_containers         import CONTAINER_LOCAL
from L00_finanalitics       import FINANALITICS
from L50_finanalitics       import C50_Finanalitics
from L90_finactions         import C90_FinactionsRecord


class C60_Finanalitics(C50_Finanalitics):
	""" Финаналитика: Механика данных """

	# Параметры
	def LabelsInclude(self, items: list[str] = None) -> list[str]:
		""" Метки выборки """
		if items is None: return self._labels_include.copy()
		else            :        self._labels_include = items.copy()

	def LabelsExclude(self, items: list[str] = None) -> list[str]:
		""" Метки фильтрации """
		if items is None: return self._labels_exclude.copy()
		else            :        self._labels_exclude = items.copy()

	def ProcessingDy(self, year: int = None) -> int:
		""" Год """
		if year is None : return self._processing_dy
		else            :        self._processing_dy = year

	def ProcessingDm(self, month: int = None) -> int:
		""" Месяц """
		if month is None: return self._processing_dm
		else            :        self._processing_dm = month

	def DataDm(self, data_key: FINANALITICS, data: any = None) -> any:
		""" Данные """
		key : str = f"{self._processing_dy:04d}_{self._processing_dm:02d}_{data_key.value}"

		if data is None: return self._data.get(key, None)
		else           :        self._data[key] = data

	# Сбор данных
	def ReadIdosFinactionsInDm(self):
		""" Сбор IDO записей финдействий в месяце """
		finactions_record = C90_FinactionsRecord()

		filter_finactions = C30_FilterLinear1D(finactions_record.Idc().data)
		filter_finactions.FilterIdpVlpByEqual(finactions_record.f_dm.Idp().data, self._processing_dm)
		filter_finactions.FilterIdpVlpByEqual(finactions_record.f_dy.Idp().data, self._processing_dy)

		for label in self._labels_include: filter_finactions.FilterIdpVlpByInclude(finactions_record.f_labels.Idp().data, label, False)
		for label in self._labels_exclude: filter_finactions.FilterIdpVlpByInclude(finactions_record.f_labels.Idp().data, label, True)

		filter_finactions.Capture(CONTAINER_LOCAL)

		self.DataDm(FINANALITICS.IDOS, filter_finactions.Idos().data)

	def ReadAmountsInDm(self):
		idos    : list[str] | None = self.DataDm(FINANALITICS.IDOS)
		if idos is None: return

		amounts : list[float]      = [C90_FinactionsRecord(ido).Amount() for ido in idos]

		self.DataDm(FINANALITICS.AMOUNTS, amounts)

	def CalcIncomeInDm(self):
		""" Расчёт общего объёма поступления """
		amounts    : list[float] | None = self.DataDm(FINANALITICS.AMOUNTS)
		if amounts is None: return

		amounts                         = list(filter(lambda amount: amount > 0, amounts))
		amount_sum                      = sum(amounts)
		amount_min                      = min(amounts) if amounts else 0
		amount_avg                      = amount_sum / len(amounts) if amounts else 0
		amount_max                      = max(amounts) if amounts else 0
		amount_count                    = len(amounts)

		self.DataDm(FINANALITICS.INCOME_AMOUNT_SUM, amount_sum)
		self.DataDm(FINANALITICS.INCOME_AMOUNT_MIN, amount_min)
		self.DataDm(FINANALITICS.INCOME_AMOUNT_AVG, amount_avg)
		self.DataDm(FINANALITICS.INCOME_AMOUNT_MAX, amount_max)
		self.DataDm(FINANALITICS.INCOME_COUNT,      amount_count)

	def CalcOutcomeInDm(self):
		""" Расчёт общего объёма выбытия """
		amounts        : list[float] | None = self.DataDm(FINANALITICS.AMOUNTS)
		if amounts is None: return

		amounts                         = list(filter(lambda amount: amount < 0, amounts))
		amount_sum                      = sum(amounts)
		amount_min                      = min(amounts) if amounts else 0
		amount_avg                      = amount_sum / len(amounts) if amounts else 0
		amount_max                      = max(amounts) if amounts else 0
		amount_count                    = len(amounts)

		self.DataDm(FINANALITICS.OUTCOME_AMOUNT_SUM, amount_sum)
		self.DataDm(FINANALITICS.OUTCOME_AMOUNT_MIN, amount_min)
		self.DataDm(FINANALITICS.OUTCOME_AMOUNT_AVG, amount_avg)
		self.DataDm(FINANALITICS.OUTCOME_AMOUNT_MAX, amount_max)
		self.DataDm(FINANALITICS.OUTCOME_COUNT,      amount_count)

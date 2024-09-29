# ФИНАНАЛИТИКА: ЛОГИКА ДАННЫХ

from G30_cactus_datafilters import C30_FilterLinear1D

from L00_containers         import CONTAINER_LOCAL
from L70_finanalitics       import C70_Finanalitics
from L90_finactions         import C90_FinactionsRecord


class C80_Finanalitics(C70_Finanalitics):
	""" Финаналитика: Логика данных """

	# Выборки данных
	def Labels(self) -> list[str]:
		""" Метки """
		finactions_record    = C90_FinactionsRecord()
		filter_finactions    = C30_FilterLinear1D(finactions_record.Idc().data)
		filter_finactions.Capture(CONTAINER_LOCAL)

		raw_data : list[str] = filter_finactions.ToStrings(finactions_record.f_labels.Idp().data).data
		labels   : list[str] = []

		for raw_item in raw_data: labels.extend(raw_item.split('\n'))
		labels               = list(sorted(set(labels)))

		return labels

	# Анализ данных
	def ExecProcessingDm(self):
		""" Выполнение анализа месяца """
		self.ReadIdosFinactionsInDm()
		self.ReadAmountsInDm()

		self.CalcIncomeInDm()
		self.CalcOutcomeInDm()

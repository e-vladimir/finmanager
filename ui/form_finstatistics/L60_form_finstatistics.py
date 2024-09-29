# ФОРМА ФИНСТАТИСТИКА: МЕХАНИКА ДАННЫХ

from G11_convertor_data     import AmountToString

from L50_form_finstatistics import C50_FormFinstatistics
from L90_finstructs         import C90_FinstructRecord


class C60_FormFinstatistics(C50_FormFinstatistics):
	""" Форма Финстатистика: Механика данных """

	# Модель данных
	def InitModelData(self):
		""" Инициализация модели данных """
		self.model_data.removeAll()

		header_labels : list[str] = []
		header_labels.append("Показатель")

		header_labels.append(f"Поступило")
		header_labels.append(f"Списано")
		header_labels.append(f"Баланс")

		self.model_data.setHorizontalHeaderLabels(header_labels)

	def LoadFinstatisticsByFinstruct(self):
		""" Загрузка финстатистики из финструктуры """
		self.model_data.fastAppendRow(["СТАТИСТИКА ПО СЧЕТАМ", "", "", ""])

		dy, dm = self.workspace.DyDm()

		for finstruct_ido in self.finstruct.IdosInDyDm(dy, dm):
			finstruct_record = C90_FinstructRecord(finstruct_ido)

			income  = finstruct_record.AmountIncome()
			outcome = finstruct_record.AmountOutcome()
			delta   = abs(income) - abs(outcome)

			self.model_data.fastAppendRow([f"{finstruct_record.Name()}", AmountToString(income, False, True), AmountToString(outcome, False, True), AmountToString(delta, False, True)])

		self.model_data.fastAppendRow(["", "", "", ""])

	def LoadFinstatisticsByLabels(self):
		""" Загрузка финстатистики из меток """
		self.model_data.fastAppendRow(["СТАТИСТИКА ПО МЕТКАМ", "", "", ""])

		dy, dm = self.workspace.DyDm()

		statistics = self.finstatistics.CaptureStatistic(dy, dm)

		for statistics_label in sorted(statistics.keys()):
			statistics_item = statistics[statistics_label]

			income          = statistics_item.income
			outcome         = statistics_item.outcome
			delta           = abs(income) - abs(outcome)

			self.model_data.fastAppendRow([f"{statistics_label}", AmountToString(income, False, True), AmountToString(outcome, False, True), AmountToString(delta, False, True)])

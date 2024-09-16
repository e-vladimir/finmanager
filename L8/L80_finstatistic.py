# ФИНСТАТИСТИКА: ЛОГИКА ДАННЫХ

from L20_stucts       import T20_FinstatisticItem
from L70_finstatistic import C70_Finstatistic
from L90_finactions   import C90_FinactionsRecord


class C80_Finstatistic(C70_Finstatistic):
	""" Финстатистика: Логика данных """

	def CaptureStatistic(self, dy: int, dm: int) -> dict[str, T20_FinstatisticItem]:
		""" Захват поступлений """
		result : dict[str, T20_FinstatisticItem] = dict()

		for ido in self.finactions.IdosInDyDmDd(dy, dm):
			finactions_record = C90_FinactionsRecord(ido)

			amount            = int(finactions_record.Amount())
			amount_income     = max(0, amount)
			amount_outcome    = min(0, amount)

			for label in finactions_record.Labels():
				item          = result.get(label, T20_FinstatisticItem())
				item.income  += amount_income
				item.outcome += amount_outcome

				result[label] = item

		return result

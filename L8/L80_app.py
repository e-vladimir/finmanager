# ПРИЛОЖЕНИЕ: ЛОГИКА ДАННЫХ

from L00_containers     import CONTAINER_LOCAL

from L40_finactions     import C40_FinactionsRecord
from L40_finstruct      import C40_FinstructRecord
from L40_rules          import C40_ProcessingRulesRecord

from L70_app            import C70_Application


class C80_Application(C70_Application):
	""" Приложение: Логика данных """

	def SetupContainerLocal(self):
		""" Настройка локального контейнера """
		C40_FinstructRecord.RegisterClass(CONTAINER_LOCAL)
		C40_FinactionsRecord.RegisterClass(CONTAINER_LOCAL)
		C40_ProcessingRulesRecord.RegisterClass(CONTAINER_LOCAL)

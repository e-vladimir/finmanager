# ПРИЛОЖЕНИЕ: ЛОГИКА ДАННЫХ

from L00_containers     import CONTAINER_LOCAL
from L40_fincomposition import C40_FincompositionRecord
from L70_app            import C70_Application


class C80_Application(C70_Application):
	""" Приложение: Логика данных """

	def SetupContainerLocal(self):
		""" Настройка локального контейнера """
		C40_FincompositionRecord.RegisterClass(CONTAINER_LOCAL)

# РАБОЧЕЕ ПРОСТРАНСТВО: ЛОГИКА ДАННЫХ
# 12 фев 2025

from G30_cactus_controller_containers import controller_containers

from L00_containers                   import CONTAINERS
from L00_months                       import MONTHS_SHORT
from L70_workspace                    import C70_Workspace
from L90_operations                   import C90_Operation, C90_Operations


class C80_Workspace(C70_Workspace):
	""" Рабочее пространство: Логика данных """

	# Обмен данными
	def DyDm(self) -> (int, int):
		""" Упаковка Год-Месяц в кортеж """
		return self.dy, self.dm

	def DmDyToString(self) -> str:
		""" Месяц-Год в текстовом формате """
		return f"{MONTHS_SHORT[self.dm]} {self.dy}"


	# Кеширование данных
	def CachingData(self):
		""" Кеширование данных """
		container = controller_containers.Container(CONTAINERS.CACHE)
		container.Clear()

		operation = C90_Operation()

		for ido in C90_Operations.Idos(self.dy, self.dm, use_cache=False):
			operation.Ido(ido)
			operation.CopyToContainer(CONTAINERS.DISK, CONTAINERS.CACHE)

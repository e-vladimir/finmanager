# ПРИЛОЖЕНИЕ: МЕХАНИКА ДАННЫХ
# 12 фев 2025

from G30_cactus_controller_containers import controller_containers

from L00_containers                   import CONTAINERS
from L50_application                  import C50_Application


class C60_Application(C50_Application):
	""" Приложение: Механика данных """

	# Контейнеры
	def InitContainers(self):
		""" Инициализация контейнеров """
		controller_containers.RegisterContainerRAM(CONTAINERS.MEMORY)

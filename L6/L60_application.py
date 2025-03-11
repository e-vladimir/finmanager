# ПРИЛОЖЕНИЕ: МЕХАНИКА ДАННЫХ
# 12 фев 2025
import os
from pathlib import Path

from G30_cactus_controller_containers import controller_containers

from L00_containers                   import CONTAINERS
from L40_account                      import C40_Account
from L40_operations import C40_Operation
from L50_application                  import C50_Application


class C60_Application(C50_Application):
	""" Приложение: Механика данных """

	# Контейнеры
	def InitContainers(self):
		""" Инициализация контейнеров """
		controller_containers.RegisterContainerRAM(CONTAINERS.MEMORY)
		controller_containers.RegisterContainerSQLite(CONTAINERS.DISK)

		container_disk = controller_containers.Container(CONTAINERS.DISK)
		container_disk.OptionsFilename("data")
		container_disk.ConnectMode_Auto(True)

		C40_Account.RegisterClass(CONTAINERS.DISK)
		C40_Operation.RegisterClass(CONTAINERS.DISK)

	# Директории
	def InitDirectories(self):
		""" Инициализация директорий """
		directories : list[str] = ["reports"]

		for directory in directories:
			try   : os.mkdir(Path("./") / directory)
			except: pass

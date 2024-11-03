# ПРИЛОЖЕНИЕ: МЕХАНИКА ДАННЫХ

import datetime

from   os                               import  mkdir
from   pathlib                          import  Path

from   G10_convertor_format             import  UTimeToDTime
from   G10_datetime                     import (CurrentUTime,
                                                CurrentDy,
		  	                                    CurrentDm,
			                                    CurrentDd)
from   G10_files                        import  FileNamesInDirectory
from   G10_shell_os                     import  ExecSingleCmdInShell
from   G30_cactus_controller_containers import  controller_containers

from   L00_containers                   import  CONTAINERS
from   L40_accounts                     import C40_Account
from   L50_app                          import  C50_Application


class C60_Application(C50_Application):
	""" Приложение: Механика данных """

	# Контейнеры
	def InitContainers(self):
		""" Инициализация контейнеров """
		controller_containers.RegisterContainerRAM(CONTAINERS.MEMORY)
		controller_containers.RegisterContainerSQLite(CONTAINERS.DISK)

	def SetupContainers(self):
		""" Настройка контейнеров """
		container_disk = controller_containers.Container(CONTAINERS.DISK)
		container_disk.OptionsFilename("data")
		container_disk.Connect()

	# Структура данных
	def InitData(self):
		""" Инициализация данных """
		C40_Account.RegisterClass(CONTAINERS.DISK)

	# Архивы данных
	def InitArchives(self):
		""" Инициализация архива данных """
		path_archives : Path = self._path_common.joinpath("archives")

		if path_archives.exists(): return

		mkdir(path_archives)

	def CopyDataToArchive(self, flag_skip_by_dd: bool = False):
		""" Создание архива данных """
		path_data     : Path = self._path_common.joinpath("data.sqlite")
		path_archives : Path = self._path_common.joinpath("archives")
		path_archive  : Path = path_archives.joinpath(f"{CurrentUTime()}.7z")

		if not path_data.exists(): return

		cmd          : str  = f"7z a {path_archive} {path_data}"
		result_skip  : bool = False and flag_skip_by_dd

		if flag_skip_by_dd:
			current_dy : int = CurrentDy()
			current_dm : int = CurrentDm()
			current_dd : int = CurrentDd()

			for archive_name in FileNamesInDirectory(path_archives):
				try   :
					archive_utime : int               = int(archive_name.split('.')[0])
					archive_dtime : datetime.datetime = UTimeToDTime(archive_utime)
					archive_dy    : int               = archive_dtime.year
					archive_dm    : int               = archive_dtime.month
					archive_dd    : int               = archive_dtime.day

					if not archive_dy == current_dy: continue
					if not archive_dm == current_dm: continue
					if not archive_dd == current_dd: continue

					result_skip = True

				except: continue

		if result_skip: return

		ExecSingleCmdInShell(cmd)

	def CopyDataFromArchive(self, filename: str) -> bool:
		""" Восстановление из архива данных """
		if not filename: return False

		container = controller_containers.Container(CONTAINERS.DISK)
		container.Disconnect()

		path_archives : Path = self._path_common.joinpath("archives")
		path_archive  : Path = path_archives.joinpath(filename)

		if not path_archive.exists(): return False

		cmd          : str  = f"7z x -y -o{self._path_common} {path_archive}"

		ExecSingleCmdInShell(cmd)

		container.Connect()

		return True

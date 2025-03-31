# ПРИЛОЖЕНИЕ: ЛОГИКА ДАННЫХ
# 12 фев 2025

import os

from   datetime                         import datetime
from   pathlib                          import Path

from   G10_convertor_format             import UTimeToDTime
from   G10_datetime                     import CurrentDd, CurrentDm, CurrentDy, CurrentUTime
from   G10_shell_os                     import ExecSingleCmdInShell
from   G30_cactus_controller_containers import controller_containers

from   L00_containers                   import CONTAINERS
from   L40_account                      import C40_Account
from   L40_operations                   import C40_Operation
from   L40_rules                        import C40_ProcessingRule
from   L70_application                  import C70_Application


class C80_Application(C70_Application):
	""" Приложение: Логика данных """

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
		C40_ProcessingRule.RegisterClass(CONTAINERS.DISK)

	# Директории
	def InitDirectories(self):
		""" Инициализация директорий """
		directories : list[str] = ["reports",
		                           "backups"
		                           ]

		for directory in directories:
			try   : os.mkdir(self._path_common / directory)
			except: pass

	# Копии архива данных
	def CreateBackup(self, flag_skip_by_dd: bool = False):
		""" Создание копии архива данных """
		path_data    : Path = self._path_common / "data.sqlite"
		path_archives: Path = self._path_common / "backups"
		path_archive : Path = path_archives / f"{CurrentUTime()}.7z"

		if not path_data.exists(): return

		cmd          : str  = f"7z a {path_archive} {path_data}"
		result_skip  : bool = False and flag_skip_by_dd

		if flag_skip_by_dd:
			current_dy: int = CurrentDy()
			current_dm: int = CurrentDm()
			current_dd: int = CurrentDd()

			for archive_name in self.backup_names:
				try:
					archive_utime : int      = int(archive_name.split('.')[0])
					archive_dtime : datetime = UTimeToDTime(archive_utime)
					archive_dy    : int      = archive_dtime.year
					archive_dm    : int      = archive_dtime.month
					archive_dd    : int      = archive_dtime.day

					if not archive_dy == current_dy: continue
					if not archive_dm == current_dm: continue
					if not archive_dd == current_dd: continue

					result_skip              = True

				except: continue

		if     result_skip       : return

		ExecSingleCmdInShell(cmd)

	def RestoreBackup(self, filename: str) -> bool:
		""" Восстановление архива данных из копии """
		if not filename             : return False

		container            = controller_containers.Container(CONTAINERS.DISK)
		container.Disconnect()

		path_archives : Path = self._path_common / "backups"
		path_archive  : Path = path_archives / filename

		if not path_archive.exists(): return False

		cmd: str = f"7z x -y -o{self._path_common} {path_archive}"

		ExecSingleCmdInShell(cmd)

		container.Connect()

		return True

	def DeleteBackup(self, filename: str) -> bool:
		""" Удаление копии архива данных """
		path_archives : Path = self._path_common / "backups"
		path_archive  : Path = path_archives / filename

		try   :	os.remove(path_archive)
		except: return False

		return True

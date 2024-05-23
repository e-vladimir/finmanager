# ФИНОРГАНАЙЗЕР: ЛОГИКА ДАННЫХ

import os
import shutil

from   pathlib                          import Path

from   G10_datetime                     import CurrentUTime
from   G30_cactus_controller_containers import controller_containers

from   L00_containers                   import *

from   L10_files                        import FileNamesInDirectory
from   L11_datetime                     import CurrentDTime, UTimeToDTime
from   L40_finactions                   import C40_RecordFinactions
from   L40_findata                      import C40_RecordFindata
from   L40_findescription               import C40_RecordFindescription
from   L40_finstate                     import C40_RecordFinstate
from   L40_finstruct                    import C40_RecordFinstruct
from   L40_processing_rules             import C40_RecordProcessingRules
from   L70_finmanager                   import C70_Finmanager


class C80_Finmanager(C70_Finmanager):
	""" Финорганайзер: Логика данных """

	# Контейнеры
	def InitContainerRam(self):
		""" Инициализация контейнера RAM """
		controller_containers.RegisterContainerRAM(CONTAINER_RAM)

	def InitContainerLocal(self):
		""" Инициализация контейнера SQLite """
		container_local = controller_containers.RegisterContainerSQLite(CONTAINER_LOCAL)
		container_local.OptionsFilename("./data.sqlite")
		container_local.Connect()

		C40_RecordFindescription.RegisterClass(CONTAINER_LOCAL)
		C40_RecordFinstruct.RegisterClass(CONTAINER_LOCAL)
		C40_RecordFindata.RegisterClass(CONTAINER_LOCAL)
		C40_RecordFinactions.RegisterClass(CONTAINER_LOCAL)
		C40_RecordFinstate.RegisterClass(CONTAINER_LOCAL)
		C40_RecordProcessingRules.RegisterClass(CONTAINER_LOCAL)

	# Резервное копирование
	def InitBackups(self):
		""" Инициализация резервного копирования """
		if self._path_backups.exists(): return

		os.mkdir(self._path_backups)

	def AutoCreateBackup(self):
		""" Автоматическое создание резервной копии """
		current_dtime    = CurrentDTime()

		current_dy : int = current_dtime.year
		current_dm : int = current_dtime.month
		current_dd : int = current_dtime.day

		for filename in self.Backups():
			backup_dtime    = UTimeToDTime(int(filename))

			backup_dy : int = backup_dtime.year
			backup_dm : int = backup_dtime.month
			backup_dd : int = backup_dtime.day

			if not current_dy == backup_dy: continue
			if not current_dm == backup_dm: continue
			if not current_dd == backup_dd: continue

			return

		self.CreateBackup()

	def CreateBackup(self):
		""" Создание резервной копии """
		path_data_src : Path = Path("./data.sqlite")
		path_data_dst : Path = self._path_backups.joinpath(f"{CurrentUTime()}")

		shutil.copyfile(path_data_src, path_data_dst)

	def RestoreBackup(self, filename: str):
		""" Восстановление из резервной копии """
		path_data_dst : Path = Path("./data.sqlite")
		path_data_src : Path = self._path_backups.joinpath(filename)
		if not path_data_src.exists(): return

		container_local = controller_containers.GetContainer(CONTAINER_LOCAL)
		container_local.Disconnect()

		shutil.copyfile(path_data_src, path_data_dst)

		container_local.Connect()

	def DeleteBackup(self, filename: str):
		""" Удаление резервной копии """
		path_backup : Path = self._path_backups.joinpath(filename)
		if not path_backup.exists(): return

		os.remove(path_backup)

	def Backups(self) -> list[str]:
		""" Получение списка резервных копий """
		return sorted(FileNamesInDirectory(self._path_backups))

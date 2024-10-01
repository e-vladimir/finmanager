# ПРИЛОЖЕНИЕ: МЕХАНИКА ДАННЫХ

import datetime

from   os                               import mkdir, remove
from   pathlib                          import Path
from   shutil                           import copy

from   G10_convertor_format             import UTimeToDTime
from   G10_datetime                     import CurrentUTime, CurrentDy, CurrentDm, CurrentDd
from   G10_files                        import FileNamesInDirectory
from   G30_cactus_controller_containers import controller_containers

from   L00_containers                   import CONTAINER_LOCAL
from   L50_app                          import C50_Application


class C60_Application(C50_Application):
	""" Приложение: Механика событий """

	# Управление БД
	def InitBackup(self):
		""" Инициализация директории резервных копий """
		if not self._path_backup.exists(): mkdir(self._path_backup)

	def AutoCreateBackup(self):
		""" Создание резервной копии БД в автоматическом режиме """
		current_dy          = CurrentDy()
		current_dm          = CurrentDm()
		current_dd          = CurrentDd()

		result_exist : bool = False

		for filename in self.Backups():
			try   :
				dtime_backup : datetime.datetime = UTimeToDTime(int(filename))

				if not dtime_backup.year  == current_dy: continue
				if not dtime_backup.month == current_dm: continue
				if not dtime_backup.day   == current_dd: continue

				result_exist = True
				break
			except: pass

		if result_exist: return

		self.CreateBackup()

	def CreateBackup(self):
		""" Создание резервной копии БД """
		filename  : str = f"{CurrentUTime()}.backup"

		path_file : Path = self._path_backup.joinpath(filename)
		db_path   : Path = self._path_common.joinpath("data.sqlite")

		if not db_path.exists(): return

		copy(db_path, path_file)

	def RestoreBackup(self, filename: str) -> bool:
		""" Восстановление резервной копии """
		path_file : Path = self._path_backup.joinpath(f"{filename}.backup")
		path_db   : Path = self._path_common.joinpath("data.sqlite")

		if not path_file.exists(): return False

		container_local = controller_containers.Container(CONTAINER_LOCAL)
		container_local.Disconnect()

		copy(path_file, path_db)

		return True

	def DeleteBackup(self, filename: str) -> bool:
		""" Удаление резервной копии """
		path_file : Path = self._path_backup.joinpath(f"{filename}.backup")

		if not path_file.exists(): return False

		remove(path_file)

		return True

	def Backups(self) -> list[str]:
		""" Список резервных копий """
		return [file_name.split('.')[0] for file_name in FileNamesInDirectory(self._path_backup)]

	# Отчётность
	def InitReports(self):
		""" Инициализация директории отчётности """
		if not self._path_reports.exists(): mkdir(self._path_reports)

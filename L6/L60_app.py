# ПРИЛОЖЕНИЕ: МЕХАНИКА ДАННЫХ

from os                               import mkdir, remove
from pathlib                          import Path
from shutil                           import copy

from G10_datetime                     import CurrentUTime
from G10_files                        import FileNamesInDirectory
from G30_cactus_controller_containers import controller_containers

from L00_containers                   import CONTAINER_LOCAL
from L50_app                          import C50_Application


class C60_Application(C50_Application):
	""" Приложение: Механика событий """

	# Управление БД
	def InitBackup(self):
		""" Инициализация директории резервных копий """
		if not self._path_backup.exists(): mkdir(self._path_backup)

	def CreateBackup(self):
		""" Создание резервной копии БД """
		filename  : str = f"{CurrentUTime()}.backup"

		path_file : Path = self._path_backup.joinpath(filename)
		db_path   : Path = self._path_common.joinpath("data.sqlite")

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

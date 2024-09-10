# ПРИЛОЖЕНИЕ: МЕХАНИКА ДАННЫХ

from os           import mkdir
from pathlib      import Path
from shutil       import copy

from G10_datetime import CurrentUTime
from G10_files    import FileNamesInDirectory

from L50_app      import C50_Application


class C60_Application(C50_Application):
	""" Приложение: Механика событий """

	# Управление БД
	def InitBackup(self):
		""" Инициализация директории резервных копий """
		if not self._path_backup.exists(): mkdir(self._path_backup)

	def CreateBackup(self):
		""" Создание резервной копии БД """
		file_name : str = f"{CurrentUTime()}.backup"
		file_path : Path = self._path_backup.joinpath(file_name)

		db_path   : Path = self._path_common.joinpath("data.sqlite")

		copy(db_path, file_path)

	def Backups(self) -> list[str]:
		""" Список резервных копий """
		return [file_name.split('.')[0] for file_name in FileNamesInDirectory(self._path_backup)]

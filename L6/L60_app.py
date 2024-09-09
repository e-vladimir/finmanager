# ПРИЛОЖЕНИЕ: МЕХАНИКА ДАННЫХ

from os           import mkdir
from pathlib      import Path
from shutil       import copy

from G10_datetime import CurrentDy, CurrentDm, CurrentDd, CurrentTh, CurrentTm
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
		file_name : str = f"{CurrentDy():04d}_{CurrentDm():02d}_{CurrentDd():02d}-{CurrentTh():02d}_{CurrentTm():02d}.backup"
		file_path : Path = self._path_backup.joinpath(file_name)

		db_path   : Path = self._path_common.joinpath("data.sqlite")

		copy(db_path, file_path)

	def Backups(self) -> list[str]:
		""" Список резервных копий """
		return FileNamesInDirectory(self._path_backup)

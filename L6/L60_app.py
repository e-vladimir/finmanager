# ПРИЛОЖЕНИЕ: МЕХАНИКА ДАННЫХ

from os           import mkdir
from pathlib      import Path

from G10_datetime import CurrentUTime
from G10_shell_os import ExecSingleCmdInShell

from L50_app      import C50_Application


class C60_Application(C50_Application):
	""" Приложение: Механика данных """

	# Каталоги
	def InitArchives(self):
		""" Инициализация архива данных """
		path_archives : Path = self._path_common.joinpath("archives")

		if path_archives.exists(): return

		mkdir(path_archives)

	def CopyDataToArchive(self):
		""" Создание архива данных """
		path_data    : Path = self._path_common.joinpath("data.sqlite")
		path_archives : Path = self._path_common.joinpath("archives")
		path_archive  : Path = path_archives.joinpath(f"{CurrentUTime()}.7z")

		if not path_data.exists(): return

		cmd          : str  = f"7z a {path_archive} {path_data}"

		ExecSingleCmdInShell(cmd)

	def CopyDataFromArchive(self, filename: str) -> bool:
		""" Восстановление из архива данных """
		if not filename: return False

		path_archives : Path = self._path_common.joinpath("archives")
		path_archive  : Path = path_archives.joinpath(filename)

		if not path_archive.exists(): return False

		cmd          : str  = f"7z x -y -o{self._path_common} {path_archive}"

		ExecSingleCmdInShell(cmd)

		return True

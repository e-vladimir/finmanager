# ПРИЛОЖЕНИЕ: МЕХАНИКА ДАННЫХ

from os           import mkdir
from pathlib      import Path

from G10_datetime import CurrentUTime
from G10_shell_os import ExecSingleCmdInShell

from L50_app      import C50_Application


class C60_Application(C50_Application):
	""" Приложение: Механика данных """

	# Каталоги
	def InitBackups(self):
		""" Инициализация архива данных """
		path_backups : Path = self._path_common.joinpath("backups")

		if path_backups.exists(): return

		mkdir(path_backups)

	def CreateBackup(self):
		""" Создание архива данных """
		path_data    : Path = self._path_common.joinpath("data.sqlite")
		path_backups : Path = self._path_common.joinpath("backups")
		path_backup  : Path = path_backups.joinpath(f"{CurrentUTime()}.7z")

		if not path_data.exists(): return

		cmd          : str  = f"7z a {path_backup} {path_data}"

		ExecSingleCmdInShell(cmd)

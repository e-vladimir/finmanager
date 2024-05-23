# ФИНОРГАНАЙЗЕР: МЕХАНИКА ДАННЫХ

import os

from   pathlib            import Path

from   L50_finmanager     import C50_Finmanager


class C60_Finmanager(C50_Finmanager):
	""" Финорганайзер: Механика данных """

	# Параметры
	def SetupPathBackups(self):
		""" Настройка директории резервных копий """
		path_finmanager : Path = Path(os.getcwd())
		self._path_backups = path_finmanager.joinpath("backups")

# ПРИЛОЖЕНИЕ: МЕХАНИКА ДАННЫХ
# 12 фев 2025

from G10_files       import FileNamesInDirectory

from L50_application import C50_Application


class C60_Application(C50_Application):
	""" Приложение: Механика данных """

	# Список копий архива данных
	@property
	def backup_names(self) -> list[str]:
		return FileNamesInDirectory(self._path_common / "backups")

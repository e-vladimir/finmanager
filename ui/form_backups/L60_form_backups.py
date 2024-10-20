# ФОРМА АРХИВ ДАННЫХ: МЕХАНИКА ДАННЫХ

from pathlib              import Path

from G10_convertor_format import UTimeToDTime
from G10_files            import FileNamesInDirectory

from L20_PySide6          import C20_StandardItem, ROLES
from L50_form_backups     import C50_FormBackups


class C60_FormBackups(C50_FormBackups):
	""" Форма Архив данных: Механика данных """

	# Модель данных
	def InitModelData(self):
		""" Инициализация модели данных """
		self.model_data.removeAll()

	def LoadModelData(self):
		""" Загрузка модели данных """
		path_backups : Path = self.application._path_common.joinpath("backups")
		for filename in FileNamesInDirectory(path_backups):
			try:
				backup_utime  : int = int(filename.split('.')[0])
				backup_dydmdd : str = f"{UTimeToDTime(backup_utime):%d %b %Y (%X)}"

				item_backup         = C20_StandardItem(backup_dydmdd, filename, ROLES.IDO)

				self.model_data.appendRow(item_backup)
			except: pass

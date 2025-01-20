# ФОРМА АРХИВЫ ДАННЫХ: МЕХАНИКА ДАННЫХ

from pathlib              import Path

from PySide6.QtCore       import QModelIndex

from G10_convertor_format import UTimeToDTime
from G10_files            import FileNamesInDirectory

from L20_PySide6          import C20_StandardItem, ROLES
from L50_form_backups     import C50_FormArchives


class C60_FormArchives(C50_FormArchives):
	""" Форма Архив данных: Механика данных """

	# Модель данных
	def InitModelData(self):
		""" Инициализация модели данных """
		self.model_data.removeAll()

	def LoadModelData(self):
		""" Загрузка модели данных """
		path_backups : Path = self.application._path_common.joinpath("archives")
		for filename in FileNamesInDirectory(path_backups):
			try:
				file_utime  : int = int(filename.split('.')[0])
				file_dydmdd : str = f"{UTimeToDTime(file_utime):%d %b %Y (%X)}"

				item_archive      = C20_StandardItem(file_dydmdd, filename, ROLES.FILENAME)

				self.model_data.appendRow(item_archive)
			except: pass

	# Параметры
	def ReadProcessingFilenameFromListData(self):
		""" Чтение текущего имени файла из списка архива данных """
		current_index : QModelIndex = self.list_data.currentIndex()
		self._processing_filename = current_index.data(ROLES.FILENAME)

	def ReadProcessingNameFromListData(self):
		""" Чтение текущего наименования из списка данных """
		current_index : QModelIndex = self.list_data.currentIndex()
		self._processing_name = current_index.data(ROLES.TEXT)

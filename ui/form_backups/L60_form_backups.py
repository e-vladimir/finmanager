# ФОРМА КОПИИ АРХИВА ДАННЫХ: МЕХАНИКА ДАННЫХ
# 18 мар 2025

from datetime             import datetime

from G10_convertor_format import UTimeToDTime

from L00_months           import MONTHS_SHORT
from L20_PySide6          import C20_StandardItem, ROLES
from L50_form_backups     import C50_FormBackups


class C60_FormBackups(C50_FormBackups):
	""" Форма Копии архива данных: Механика данных """

	# Рабочее имя файла
	@property
	def processing_filename(self) -> str:
		return self._processing_filename

	def ReadProcessingFilenameFromListData(self):
		"""  """
		self._processing_filename = self.ListData.currentIndex().data(ROLES.FILENAME)


	@property
	def processing_name(self) -> str:
		return self._processing_name

	def ReadProcessingNameFromListData(self):
		"""  """
		self._processing_name = self.ListData.currentIndex().data(ROLES.TEXT)


	# Модель данных
	def InitModelData(self):
		""" Инициализация модели данных """
		self.ModelData.removeAll()

		self.ModelData.setHorizontalHeaderLabels(["Копия архива данных"])

	def LoadModelData(self):
		""" Загрузка данных в модель данных """
		for filename in self.Application.backup_names:
			backup_name : str      = filename.split('.')[0]
			if not backup_name.isnumeric(): continue

			dtime       : datetime = UTimeToDTime(int(backup_name))

			item_backup            = C20_StandardItem("")
			item_backup.setText(f"{dtime.day:02d} {MONTHS_SHORT[dtime.month]} {dtime.year} {dtime.hour:02d}:{dtime.minute:02d}")
			item_backup.setData(filename, ROLES.FILENAME)

			self.ModelData.appendRow(item_backup)

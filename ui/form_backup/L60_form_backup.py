# ФОРМА РЕЗЕРВНОЕ КОПИРОВАНИЕ: МЕХАНИКА ДАННЫХ
from PySide6.QtCore import Qt

from G11_convertor_data   import UTimeToDdDmDyThTmTs

from L20_PySide6          import C20_StandardItem, ROLES
from L50_form_backup      import C50_FormBackup


class C60_FormBackup(C50_FormBackup):
	""" Форма Резервное копирование: Механика данных """

	# Параметры
	def ReadProcessingFilename(self):
		""" Чтение имени файла обработки """
		current_index = self.list_data.currentIndex()
		self._processing_filename = current_index.data(ROLES.ROLE_IDO)

	def ReadProcessingName(self):
		""" Чтение наименования обработки """
		current_index = self.list_data.currentIndex()
		self._processing_name = current_index.data(Qt.ItemDataRole.DisplayRole)

	# Модель данных
	def LoadModelData(self):
		""" Загрузка данных в модель """
		self.model_data.removeAll()

		for name_utime in self.application.Backups():
			try   :
				item_name = C20_StandardItem(UTimeToDdDmDyThTmTs(int(name_utime)), name_utime, ROLES.ROLE_IDO)
				self.model_data.appendRow(item_name)
			except:
				pass

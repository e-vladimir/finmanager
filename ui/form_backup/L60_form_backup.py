# ФОРМА РЕЗЕРВНОЕ КОПИРОВАНИЕ: МЕХАНИКА ДАННЫХ

from G11_convertor_data   import UTimeToDdDmDyThTmTs

from L20_PySide6          import C20_StandardItem
from L50_form_backup      import C50_FormBackup


class C60_FormBackup(C50_FormBackup):
	""" Форма Резервное копирование: Механика данных """

	# Модель данных
	def LoadModelData(self):
		""" Загрузка данных в модель """
		self.model_data.removeAll()

		for name_utime in self.application.Backups():
			try   :
				item_name = C20_StandardItem(UTimeToDdDmDyThTmTs(int(name_utime)))
				self.model_data.appendRow(item_name)
			except:
				pass

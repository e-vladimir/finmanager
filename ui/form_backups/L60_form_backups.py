# ФОРМА РЕЗЕРВНЫЕ КОПИИ: МЕХАНИКА ДАННЫХ

from PySide6.QtCore   import QModelIndex, Qt

from L00_months       import MONTHS_SHORT

from L11_datetime     import UTimeToDTime
from L20_PySide6      import C20_StandardItem, ROLE_OID
from L50_form_backups import C50_FormBackups


class C60_FormBackups(C50_FormBackups):
	""" Форма Резервные копии: Механика данных """

	# Параметры
	def ReadFilenameProcessingFromSelected(self):
		""" Считывание имени файла из выделенной записи """
		self._filename_processing = ""

		indexes_selected : list[QModelIndex] = self.lst_backups.selectedIndexes()
		if not indexes_selected: return

		index_selected                       = indexes_selected[0]

		self._filename_processing = index_selected.data(ROLE_OID)

	# Модель
	def SetupModelBackups(self):
		""" Настройка модели """
		self.model_backups.removeAll()

		self.model_backups.setHorizontalHeaderLabels(["Резервная копия"])

	def LoadBackup(self):
		""" Загрузка резервной копии """
		if not self._filename_processing: return

		dtime_backup = UTimeToDTime(int(self._filename_processing))

		dy : int     = dtime_backup.year
		dm : int     = dtime_backup.month
		dd : int     = dtime_backup.day

		hh : int     = dtime_backup.hour
		hm : int     = dtime_backup.minute

		item_backup  = C20_StandardItem(f"{dd:02d} {MONTHS_SHORT[dm]} {dy} - {hh:02d}:{hm:02d}", self._filename_processing)

		self.model_backups.appendRow(item_backup)

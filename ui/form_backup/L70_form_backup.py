# ФОРМА РЕЗЕРВНОЕ КОПИРОВАНИЕ: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtGui   import QCursor

from L60_form_backup import C60_FormBackup


class C70_FormBackup(C60_FormBackup):
	""" Форма Резервное копирование: Механика управления """

	# Меню резервных копий
	def AdjustMenuBackupText(self):
		""" Меню резервных копий: Настойка текста """
		self.menu_backup_header.setTitle("Резервная копия")

		if not self._processing_name: return

		self.menu_backup_header.setTitle(self._processing_name)

	def AdjustMenuBackupEnable(self):
		""" Меню резервных копий: Настройка доступности """
		flag_selected : bool = bool(self._processing_filename)

		self.menu_backup_restore.setEnabled(flag_selected)
		self.menu_backup_delete.setEnabled(flag_selected)

	def ShowMenuBackup(self):
		""" Отображение меню резервных копий """
		self.menu_backup.exec_(QCursor().pos())

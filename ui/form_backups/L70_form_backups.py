# ФОРМА РЕЗЕРВНЫЕ КОПИИ: МЕХАНИКА УПРАВЛЕНИЯ
from PySide6.QtCore import Qt
from PySide6.QtGui    import QCursor, QStandardItem

from L20_PySide6      import ROLE_OID
from L60_form_backups import C60_FormBackups


class C70_FormBackups(C60_FormBackups):
	""" Форма Резервные копии: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка окна """
		self.setWindowTitle("Резервное копирование данных")

	# Меню резервных копий
	def ShowMenuBackups(self):
		""" Отображение меню резервных копий """
		self.mnu_backups.exec_(QCursor().pos())

	def SetupMenuBackups(self):
		""" Настройка меню резервных копий """
		self.mnu_backups_backup_header.setText("Резервная копия")

		if not self._filename_processing: return

		item_selected : QStandardItem | None = self.model_backups.itemByData(self._filename_processing, ROLE_OID)
		if item_selected is None: return

		self.mnu_backups_backup_header.setText(item_selected.data(Qt.ItemDataRole.DisplayRole))

	def SetupEnabledMenuBackups(self):
		""" Настройка доступности элементов меню """
		flag_selected : bool = bool(self._filename_processing)

		self.mnu_backups_backup_restore.setEnabled(flag_selected)
		self.mnu_backups_backup_delete.setEnabled(flag_selected)

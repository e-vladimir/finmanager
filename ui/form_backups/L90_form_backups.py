# ФОРМА РЕЗЕРВНЫЕ КОПИИ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_backups import C80_FormBackups


class C90_FormBackups(C80_FormBackups):
	""" Форма Резервные копии: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Список резервных копий
		self.lst_backups.customContextMenuRequested.connect(self.on_RequestMenuBackups)

		# Меню резервных копий
		self.mnu_backups_create_backup.triggered.connect(self.on_RequestCreateBackup)
		self.mnu_backups_backup_restore.triggered.connect(self.on_RequestRestoreFromBackup)
		self.mnu_backups_backup_delete.triggered.connect(self.on_RequestDeleteBackup)

	# Форма
	def on_Open(self):
		""" Открытие формы """
		self.ShowTitle()

		self.on_RequestShowBackups()

	# Меню резервных копий
	def on_RequestMenuBackups(self):
		""" Запрос отображения меню резервных копий """
		self.ReadFilenameProcessingFromSelected()

		self.SetupMenuBackups()
		self.SetupEnabledMenuBackups()
		self.ShowMenuBackups()

	def on_RequestCreateBackup(self):
		""" Создание резервной копии """
		self.application.CreateBackup()
		self.on_RequestShowBackups()

	def on_RequestRestoreFromBackup(self):
		""" Восстановление из резервной копии """
		self.application.RestoreBackup(self._filename_processing)

	def on_RequestDeleteBackup(self):
		""" Удаление резервной копии """
		self.DeleteBackup()

	# Модель резервных копий
	def on_RequestShowBackups(self):
		""" Запрос отображения списка резервных копий """
		self.SetupModelBackups()
		self.ShowBackups()

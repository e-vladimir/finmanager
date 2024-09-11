# ФОРМА РЕЗЕРВНОЕ КОПИРОВАНИЕ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_backup import C80_FormBackup


class C90_FormBackup(C80_FormBackup):
	""" Форма Резервное копирование: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Список данных
		self.list_data.customContextMenuRequested.connect(self.on_RequestMenuBackup)

		# Меню резервных копий
		self.menu_backups_create.triggered.connect(self.on_RequestCreateBackup)

		self.menu_backup_restore.triggered.connect(self.on_RequestRestoreBackup)
		self.menu_backup_delete.triggered.connect(self.on_RequestDeleteBackup)

	def on_Open(self):
		""" Открытие формы """
		self.LoadModelData()

	# Меню резервных копий
	def on_RequestMenuBackup(self):
		""" Запрос на отображение меню резервных копий """
		self.ReadProcessingName()
		self.ReadProcessingFilename()

		self.AdjustMenuBackupText()
		self.AdjustMenuBackupEnable()

		self.ShowMenuBackup()

	# Резервное копирование
	def on_RequestCreateBackup(self):
		""" Запрос создания резервной копии """
		self.application.CreateBackup()

		self.LoadModelData()

	def on_RequestRestoreBackup(self):
		""" Запрос восстановления резервной копии """
		self.RestoreBackup()

	def on_RequestDeleteBackup(self):
		""" Запрос удаления резервной копии """
		self.DeleteBackup()

		self.LoadModelData()

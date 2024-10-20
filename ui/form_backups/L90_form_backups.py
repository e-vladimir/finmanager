# ФОРМА АРХИВ ДАННЫХ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_backups import C80_FormBackups


class C90_FormBackups(C80_FormBackups):
	""" Форма Архив данных: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Список архивов
		self.list_data.customContextMenuRequested.connect(self.on_RequestShowMenuBackups)

		# Меню архива данных
		self.menu_backups_create_backup.triggered.connect(self.on_RequestCreateBackup)

	# Форма
	def on_Open(self):
		""" Открытие формы """
		self.ShowTitle()

		self.InitModelData()
		self.LoadModelData()

	# Меню архива данных
	def on_RequestShowMenuBackups(self):
		""" Запрос на отображение меню архива данных """
		self.AdjustMenuBackups_Text()
		self.AdjustMenuBackups_Enable()

		self.ShowMenuBackups()

	# Архив данных
	def on_RequestCreateBackup(self):
		""" Запрос на создание архива данных """
		self.application.CreateBackup()

		self.InitModelData()
		self.LoadModelData()

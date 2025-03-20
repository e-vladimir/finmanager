# ФОРМА КОПИИ АРХИВА ДАННЫХ: ЛОГИКА УПРАВЛЕНИЯ
# 18 мар 2025

from L80_form_backups import C80_FormBackups


class C90_FormBackups(C80_FormBackups):
	""" Форма Копии архива данных: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Список данных
		self.ListData.customContextMenuRequested.connect(self.on_RequestShowMenuBackups)

		# Меню Копии архива данных
		self.ActionCreateBackup.triggered.connect(self.on_RequestCreateBackup)
		self.ActionDeleteBackup.triggered.connect(self.on_RequestDeleteBackup)
		self.ActionRestoreFromBackup.triggered.connect(self.on_RequestRestoreFromBackup)

	# Форма
	def on_Opened(self):
		self.InitModelData()
		self.LoadModelData()

		self.ShowTitle()

	# Меню Копии архива данных
	def on_RequestShowMenuBackups(self):
		""" Запрос отображения меню Копии архива данных """
		self.ReadProcessingFilenameFromListData()
		self.ReadProcessingNameFromListData()

		self.AdjustMenuBackups()
		self.ShowMenuBackups()

	# Копии архива данных
	def on_BackupsChanged(self):
		""" Список копий архива данных изменился """
		self.InitModelData()
		self.LoadModelData()

	# Копии архива данных
	def on_RequestCreateBackup(self):
		""" Создание копии архива данных """
		self.Application.CreateBackup()

		self.on_BackupsChanged()

	def on_RequestRestoreFromBackup(self):
		""" Запрос восстановления архива данных из копии """
		self.RestoreFromBackup()

	def on_RequestDeleteBackup(self):
		""" Запрос удаления копии архива данных """
		self.DeleteBackup()

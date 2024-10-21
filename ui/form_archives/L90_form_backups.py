# ФОРМА АРХИВЫ ДАННЫХ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_backups import C80_FormArchives


class C90_FormArchives(C80_FormArchives):
	""" Форма Архив данных: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Список архивов
		self.list_data.customContextMenuRequested.connect(self.on_RequestShowMenuArchives)

		# Меню архива данных
		self.menu_archives_copy_to_archive.triggered.connect(self.on_RequestCopyDataToArchive)
		self.menu_archive_copy_from_archive.triggered.connect(self.on_RequestCopyDataFromArchive)
		self.menu_archive_delete.triggered.connect(self.on_RequestDeleteArchive)

	# Форма
	def on_Open(self):
		""" Открытие формы """
		self.ShowTitle()

		self.InitModelData()
		self.LoadModelData()

	# Меню архива данных
	def on_RequestShowMenuArchives(self):
		""" Запрос на отображение меню архива данных """
		self.ReadProcessingFilenameFromListData()
		self.ReadProcessingNameFromListData()

		self.AdjustMenuArchives_Text()
		self.AdjustMenuArchives_Enable()

		self.ShowMenuArchives()

	# Архив данных
	def on_RequestCopyDataToArchive(self):
		""" Запрос на создание архива данных """
		self.application.CopyDataToArchive()

		self.InitModelData()
		self.LoadModelData()

	def on_RequestCopyDataFromArchive(self):
		self.CopyDataFromArchive()

	def on_RequestDeleteArchive(self):
		""" Запрос на удаление архива данных """
		self.DeleteArchive()

		self.InitModelData()
		self.LoadModelData()

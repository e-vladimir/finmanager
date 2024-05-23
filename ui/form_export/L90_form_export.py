# ФОРМА ЭКСПОРТА: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_export import C80_FormExport


class C90_FormExport(C80_FormExport):
	""" Форма экспорта: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Панель Финданных
		self.cbb_findata_dy.currentTextChanged.connect(self.on_RequestReadFindataDyDm)
		self.cbb_findata_dm.currentTextChanged.connect(self.on_RequestReadFindataDyDm)

		self.cbb_findata_finstruct.currentTextChanged.connect(self.on_RequestReadFindataFinstruct)

		self.btn_findata_directory.clicked.connect(self.on_RequestSetFindataDirectory)

		# Панель Статистика
		self.btn_exec_export.clicked.connect(self.on_RequestStartStopExport)

		# Таймеры
		self.timer_statistic.timeout.connect(self.on_ExportProcessing)

	def on_Open(self):
		self.SwitchFlagLoadingOn()

		self.LoadFindataDy()
		self.LoadFindataDm()

		self.LoadDyDmFromWorkspace()

		self.SwitchFlagLoadingOff()

		self.ReadFindataDyDm()

		self.SetFindataFolderToCurrent()
		self.ShowFindataFolder()

		self.ShowTitle()

	def on_RequestReadFindataDyDm(self):
		""" Запрос на чтение параметров периода финданных """
		self.ReadFindataDyDm()

	def on_FindataDyDmChanged(self):
		""" Изменились параметры периода финданных """
		self.LoadFindataFinstruct()

	def on_RequestReadFindataFinstruct(self):
		""" Запрос на чтение финструктуры """
		self.ReadFindataFinstruct()

	def on_FindataOptionsChanged(self):
		""" Изменились параметры экспорта финданных """
		self.GenerateFindataFilename()

		self.ShowFindataFilename()
		self.ShowFindataFolder()

	def on_RequestSetFindataDirectory(self):
		""" Запрос на изменение директории экспорта финданных """
		self.SetFindataFolder()

	def on_RequestStartStopExport(self):
		""" Запрос Запуска/Остановки экспорта """
		self.StartStopExport()

	def on_ExportStarted(self):
		""" Экспорт начался """
		self.ResetStatistic()

		self.MemoryTimeStart()

		self.SwitchFlagExportingOn()
		self.ShowExportState()

		self.CalcStatistic()

		self.timer_statistic.start()

	def on_ExportFinished(self):
		""" Экспорт завершен """
		self.timer_statistic.stop()

		self.SwitchFlagExportingOff()
		self.ShowExportState()

		self.ShowExportStatistic()

	def on_ExportProcessing(self):
		""" Процесс экспорта """
		self.CalcStatistic()
		self.ShowExportStatistic()
		self.application.processEvents()

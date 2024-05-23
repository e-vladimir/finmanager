# ФОРМА ИМПОРТА ДАННЫХ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_import import C80_FormImport


class C90_FormImport(C80_FormImport):
	""" Форма импорта данных: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Вкладка Финданные
		self.btn_findata_file.clicked.connect(self.on_FindataRequestSelectFile)

		# Вкладка Статистика
		self.timer_statistic.timeout.connect(self.on_RequestShowStatistic)
		self.btn_exec_import.clicked.connect(self.on_StartStopImport)

	def on_Open(self):
		self.ShowTitle()

		self.FillFindataFinstruct()
		self.FillFindataFormats()

	def on_FindataRequestSelectFile(self):
		""" Запрос на выбор файла для импорта финданных """
		self.RequestFindataFilename()

	def on_FindataSelectedFile(self):
		""" Выбран файл для импорта финданных """
		self.ShowFindata()

	def on_ImportStarted(self):
		""" Начало импорта """
		self.ResetStatistic()
		self.ReadStatisticUtimeStart()

		self.timer_statistic.start()

	def on_ImportFinished(self):
		""" Завершение импорта """
		self.timer_statistic.stop()

		self._flag_processing = False

		self.CalcStatistic()

		self.ShowStateProcessing()
		self.ShowStatistics()

	def on_RequestShowStatistic(self):
		""" Запрос на отображение статистики """
		self.CalcStatistic()
		self.ShowStatistics()

	def on_StartStopImport(self):
		""" Запрос на выполнение импорта """
		self.ReadFindataFormat()
		self.ReadFindataFinstructName()

		self.StartStopImport()

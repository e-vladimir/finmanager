# ПРИЛОЖЕНИЕ: ЛОГИКА УПРАВЛЕНИЯ

from L80_app import C80_Application


class C90_Application(C80_Application):
	""" Приложение: Логика управления """

	def on_Inited(self):
		""" Инициализация приложения """
		super().on_Inited()

		self.InitReports()

		self.InitArchives()
		self.CopyDataToArchive(True)

		self.InitContainers()
		self.SetupContainers()

		self.InitData()

	def on_Start(self):
		""" Запуск приложения """
		super().on_Start()

		self.form_main.Open()

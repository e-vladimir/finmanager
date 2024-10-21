# ПРИЛОЖЕНИЕ: ЛОГИКА УПРАВЛЕНИЯ

from L80_app import C80_Application


class C90_Application(C80_Application):
	""" Приложение: Логика управления """

	def on_Init(self):
		""" Инициализация приложения """
		super().on_Init()

		self.InitArchives()
		self.CopyDataToArchive(True)

	def on_Start(self):
		""" Запуск приложения """
		super().on_Start()

		self.form_main.Open()

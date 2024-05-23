# ФИНОРГАНАЙЗЕР: ЛОГИКА УПРАВЛЕНИЯ

from L80_finmanager import C80_Finmanager


class C90_Finmanager(C80_Finmanager):
	""" Финорганайзер: Логика управления """

	def on_Start(self):
		""" Запуск приложения """
		super().on_Start()

		self.InitContainerRam()
		self.InitContainerLocal()

		self.SetupPathBackups()
		self.InitBackups()
		self.AutoCreateBackup()

		self.form_main.Open()

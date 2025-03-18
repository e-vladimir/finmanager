# ПРИЛОЖЕНИЕ: ЛОГИКА УПРАВЛЕНИЯ
# 12 фев 2025

from L80_application import C80_Application


class C90_Application(C80_Application):
	""" Приложение: Логика управления """

	def on_Inited(self):
		super().on_Inited()

		self.InitDirectories()

		self.CreateBackup(True)

		self.InitContainers()

	def on_Start(self):
		super().on_Start()

		self.FormMain.Open()

# ПРИЛОЖЕНИЕ: МОДЕЛЬ ДАННЫХ

from G30_cactus_controller_containers import controller_containers

from L00_containers                   import CONTAINER_RAM, CONTAINER_LOCAL
from L20_PySide6                      import C20_PySideApplication
from L90_form_main                    import C90_FormMain
from L90_form_fincomposition          import C90_FormFincomposition


class C40_Application(C20_PySideApplication):
	""" Приложение: Модель данных """

	def Init_10(self):
		super().Init_10()

		controller_containers.RegisterContainerRAM(CONTAINER_RAM)
		controller_containers.RegisterContainerSQLite(CONTAINER_LOCAL)

		self.form_main           = C90_FormMain(self)
		self.form_fincomposition = C90_FormFincomposition(self)

	def Init_11(self):
		super().Init_11()

		container_local = controller_containers.Container(CONTAINER_LOCAL)
		container_local.OptionsFilename("./data.sqlite")
		container_local.ConnectMode_Auto(True)

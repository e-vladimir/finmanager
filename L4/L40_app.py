# ПРИЛОЖЕНИЕ: МОДЕЛЬ ДАННЫХ

from pathlib                          import Path

from G30_cactus_controller_containers import controller_containers

from L00_containers                   import CONTAINER_RAM, CONTAINER_LOCAL

from L20_PySide6                      import C20_PySideApplication

from L90_form_backup                  import C90_FormBackup
from L90_form_export                  import C90_FormExport
from L90_form_finactions              import C90_FormFinactions
from L90_form_finactions_record       import C90_FormFinactionsRecord
from L90_form_finstruct               import C90_FormFinstruct
from L90_form_import                  import C90_FormImport
from L90_form_main                    import C90_FormMain
from L90_form_fincomposition          import C90_FormFincomposition
from L90_form_rules                   import C90_FormRules


class C40_Application(C20_PySideApplication):
	""" Приложение: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._path_backup : Path = self._path_common.joinpath("backups")

	def Init_10(self):
		super().Init_10()

		controller_containers.RegisterContainerRAM(CONTAINER_RAM)
		controller_containers.RegisterContainerSQLite(CONTAINER_LOCAL)

		self.form_main              = C90_FormMain(self)
		self.form_fincomposition    = C90_FormFincomposition(self)
		self.form_finstruct         = C90_FormFinstruct(self)
		self.form_finactions        = C90_FormFinactions(self)
		self.form_finactions_record = C90_FormFinactionsRecord(self)
		self.form_import            = C90_FormImport(self)
		self.form_rules             = C90_FormRules(self)
		self.form_backup            = C90_FormBackup(self)
		self.form_export            = C90_FormExport(self)

	def Init_11(self):
		super().Init_11()

		container_local = controller_containers.Container(CONTAINER_LOCAL)
		container_local.OptionsFilename("./data.sqlite")
		container_local.ConnectMode_Auto(True)

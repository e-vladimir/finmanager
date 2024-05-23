# ФИНОРГАНАЙЗЕР: МОДЕЛЬ ДАННЫХ

from pathlib                    import Path

from L20_PySide6                import C20_PySideApplication
from L90_form_backups           import C90_FormBackups
from L90_form_export            import C90_FormExport
from L90_form_finanalytics      import C90_FormFinanalytics
from L90_form_findata           import C90_FormFindata
from L90_form_findescription    import C90_FormFindescription
from L90_form_finstatistic      import C90_FormFinstatistic
from L90_form_finstruct         import C90_FormFinstruct
from L90_form_import            import C90_FormImport
from L90_form_main              import C90_FormMain
from L90_form_record_finactions import C90_FormRecordFinactions
from L90_form_record_findata    import C90_FormRecordFindata
from L90_form_reset             import C90_FormReset
from L90_form_rules             import C90_FormRules


class C40_Finmanager(C20_PySideApplication):
	""" Финорганайзер: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._path_backups : Path = Path()

	def Init_10(self):
		super().Init_10()

		self.form_cleaner           = C90_FormReset(self)
		self.form_export            = C90_FormExport(self)
		self.form_finanalytics      = C90_FormFinanalytics(self)
		self.form_findata           = C90_FormFindata(self)
		self.form_findescription    = C90_FormFindescription(self)
		self.form_finstatistic      = C90_FormFinstatistic(self)
		self.form_finstruct         = C90_FormFinstruct(self)
		self.form_import            = C90_FormImport(self)
		self.form_main              = C90_FormMain(self)
		self.form_record_finactions = C90_FormRecordFinactions(self)
		self.form_record_findata    = C90_FormRecordFindata(self)
		self.form_rules             = C90_FormRules(self)
		self.form_backups           = C90_FormBackups(self)

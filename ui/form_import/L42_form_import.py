# ФОРМА ИМПОРТ ДАННЫХ: МОДЕЛЬ ДАННЫХ
# 14 мар 2025

from pathlib         import Path

from L20_PySide6     import C20_StandardItemModel
from L20_form_import import T20_OperationsStruct
from L41_form_import import C41_FormImport
from L90_workspace   import C90_Workspace


class C42_FormImport(C41_FormImport):
	""" Форма Импорт данных: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._operations_data     : list                       = []
		self._operations_filepath : Path | None                = None
		self._operations_struct   : list[T20_OperationsStruct] = []

	def Init_10(self):
		super().Init_10()

		self.ModelDataOperations = C20_StandardItemModel()

		self.Workspace           = C90_Workspace()

	def Init_11(self):
		super().Init_11()

		self.Workspace.SwitchToMain()

	def Init_20(self):
		super().Init_20()

		self.TableDataOperations.setModel(self.ModelDataOperations)

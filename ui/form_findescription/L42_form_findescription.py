# ФОРМА ФИНСОСТАВА: МОДЕЛЬ ДАННЫХ

from PySide6.QtGui           import QStandardItemModel, QStandardItem

from L41_form_findescription import C41_FormFindescription
from L90_findescription      import C90_Findescription


class C42_FormFindescription(C41_FormFindescription):
	""" Форма Финсостав: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._ido_processing      : str  = ""
		self._ido_memory          : str  = ""

		self._category_processing : str  = ""

		self._item_processing     : QStandardItem | None = None

		self._flag_loading        : bool = False
		self._flag_checked        : bool = False

	def Init_10(self):
		super().Init_10()

		self.findescription       = C90_Findescription()

		self.model_findescription = QStandardItemModel(None)

	def Init_20(self):
		super().Init_20()

		self.tre_findescription.setModel(self.model_findescription)

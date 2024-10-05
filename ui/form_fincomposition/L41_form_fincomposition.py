# ФОРМА ФИНСОСТАВ: МОДЕЛЬ UI

from PySide6.QtGui           import QAction, QIcon
from PySide6.QtWidgets       import QMenu

from L20_PySide6             import C20_PySideForm
from L40_form_fincomposition import Ui_frm_fincomposition


class C41_FormFincomposition(C20_PySideForm, Ui_frm_fincomposition):
	""" Форма Финсостав: Модель UI """

	def InitUi(self): self.setupUi(self)

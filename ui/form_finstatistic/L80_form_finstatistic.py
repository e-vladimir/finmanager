# ФОРМА ФИНСТАТИСТИКА: ЛОГИКА ДАННЫХ

from PySide6.QtWidgets     import QProgressDialog

from L70_form_finstatistic import C70_FormFinstatistic


class C80_FormFinstatistic(C70_FormFinstatistic):
	""" Форма Финстатистика: Логика данных """

	# Финстатистика
	def ShowFinstatistic(self):
		""" Отображение финстатистики за финпериод """
		self.model_finstatistic.removeAll()

		oids : list[str] = self.findescription.SubOids()

		dialog_progress = QProgressDialog("Загрузка финстатистики", "Отмена", 0, len(oids))
		dialog_progress.setMinimumWidth(480)
		dialog_progress.setMinimumHeight(120)
		dialog_progress.setWindowTitle("Финстатистика")

		for self._oid_processing in oids:
			dialog_progress.setValue(dialog_progress.value() + 1)
			dialog_progress.forceShow()
			self.application.processEvents()

			self.LoadRecordFinstatistic()

	def ExpandRecordFinstatistic(self):
		""" Фрагментация записи финстатистики """
		oids : list[str] = self.findescription.Oids()

		dialog_progress = QProgressDialog("Загрузка финстатистики", "Отмена", 0, len(oids))
		dialog_progress.setMinimumWidth(480)
		dialog_progress.setMinimumHeight(120)
		dialog_progress.setWindowTitle("Финстатистика")

		for self._oid_processing in oids:
			dialog_progress.setValue(dialog_progress.value() + 1)
			dialog_progress.forceShow()
			self.application.processEvents()

			self.LoadSubRecordFinstatistic()

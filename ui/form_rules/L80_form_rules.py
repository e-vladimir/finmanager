# ФОРМА ПРАВИЛА ОБРАБОТКИ ДАННЫХ: ЛОГИКА ДАННЫХ

from PySide6.QtCore    import Qt
from PySide6.QtWidgets import QProgressDialog

from L00_containers    import CONTAINERS
from L20_PySide6       import RequestConfirm
from L70_form_rules    import C70_FormRules
from L90_rules         import C90_ProcessingRule


class C80_FormRules(C70_FormRules):
	""" Форма Правила обработки данных: Логика данных """

	# Правила обработки данных
	def ShowRules(self):
		""" Загрузка правил обработки данных """
		for self._processing_ido in self.rules.IdosByType(self._processing_type): self.LoadRule()

	# Тип правил обработки данных
	def CreateRule(self):
		""" Создание правила обработки данных """
		pass

	def ResetData(self):
		""" Сброс данных """
		idos : list[str] = self.rules.IdosByType(self._processing_type)
		if not idos: return

		if not RequestConfirm("Правила обработки данных", f"{self._processing_type.value}\n\nБудет удалено правил: {len(idos)}"): return

		dialog_progress  = QProgressDialog(self)
		dialog_progress.setWindowTitle("Правила обработки данных: Сброс данных")
		dialog_progress.setLabelText("Осталось обработать: --")
		dialog_progress.setWindowModality(Qt.WindowModality.WindowModal)
		dialog_progress.setMaximum(len(idos))

		for ido in idos:
			dialog_progress.setValue(dialog_progress.value() + 1)
			dialog_progress.setLabelText(f"Осталось обработать: {dialog_progress.maximum() - dialog_progress.value()}")

			rule = C90_ProcessingRule(ido)
			rule.DeleteObject(CONTAINERS.DISK)

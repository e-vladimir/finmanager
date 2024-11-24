# ФОРМА ПРАВИЛА ОБРАБОТКИ ДАННЫХ: ЛОГИКА ДАННЫХ

from PySide6.QtCore    import Qt
from PySide6.QtWidgets import QProgressDialog

from L00_containers    import CONTAINERS
from L00_rules         import RULES
from L20_PySide6       import RequestMultipleText, RequestText, RequestConfirm
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
		data_output : list[str] | None = None

		match self._processing_type:
			case RULES.REPLACE_TEXT:
				data : str | None       = RequestText("Создание правила обработки данных",         f"{self._processing_type.value}\n\nНа что заменить", "")
				if data is None: return

				data_output = [data]

			case RULES.DETECT_LABEL_BY_TEXT:
				data : list[str] | None = RequestMultipleText("Создание правила обработки данных", f"{self._processing_type.value}\n\nМетки",           [])
				if data is None: return

				data_output = data.copy()

		if data_output is None: return

		rule                           = C90_ProcessingRule()
		rule.GenerateIdo()
		rule.RegisterObject(CONTAINERS.DISK)

		rule.Type(self._processing_type)
		rule.InputAsString("")
		rule.OutputAsStrings(data_output)

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

	# Правило обработки данных
	def EditInputData(self):
		""" Редактирование входных данных """
		rule                   = C90_ProcessingRule(self._processing_ido)
		data_input : list[str] = []

		match self._processing_type:
			case RULES.REPLACE_TEXT:
				data : list[str] | None = RequestMultipleText(self._processing_type.value, f"Замена на {rule.OutputAsString()}", rule.InputAsStrings())
				if data is None: return

				data_input = data.copy()

			case RULES.DETECT_LABEL_BY_TEXT:
				data: list[str] | None = RequestMultipleText(self._processing_type.value, f"{'\n'.join(rule.OutputAsStrings())}\n\nОпределяется по признакам...", rule.InputAsStrings())
				if data is None: return

				data_input = data.copy()

		rule.InputAsStrings(data_input)

	def EditOutputData(self):
		""" Редактирование выходных данных """
		rule                    = C90_ProcessingRule(self._processing_ido)
		data_output : list[str] = []

		match self._processing_type:
			case RULES.REPLACE_TEXT:
				data : str | None = RequestText(self._processing_type.value, f"{'\n'.join(rule.InputAsStrings())}\n\nЗамена на...", rule.OutputAsString())
				if data is None: return

				data_output.append(data)

			case RULES.DETECT_LABEL_BY_TEXT:
				data: list[str] | None = RequestMultipleText(self._processing_type.value, f"{'\n'.join(rule.InputAsStrings())}\n\nСопоставление с...", rule.OutputAsStrings())
				if data is None: return

				data_output = data.copy()

		rule.OutputAsStrings(data_output)

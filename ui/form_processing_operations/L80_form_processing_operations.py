# ФОРМА ОБРАБОТКА ОПЕРАЦИЙ: ЛОГИКА ДАННЫХ

from PySide6.QtCore                 import Qt
from PySide6.QtWidgets              import QProgressDialog

from G30_cactus_datafilters         import C30_FilterLinear1D

from L00_containers                 import CONTAINERS
from L00_form_processing_operations import MODES
from L00_rules                      import RULES

from L20_PySide6 import RequestConfirm, RequestItems, RequestMultipleText, RequestText
from L70_form_processing_operations import C70_FormProcessingOperations
from L90_operations                 import C90_Operation, C90_Operations
from L90_rules                      import C90_ProcessingRule


class C80_FormProcessingOperations(C70_FormProcessingOperations):
	""" Форма Обработка операций: Логика данных """

	# Форма
	def UpdateDataPartial(self):
		""" Частичное обновление данных """
		self.ReadProcessingIdoFromWorkspace()
		self.LoadRuleToModel()

		self.AdjustTableRules_Size()

	# Правила обработки
	def ShowRules(self):
		""" Отображение правил обработки """
		for self._processing_ido in self.rules.IdosByType(self._processing_rule_types, True): self.LoadRuleToModel()

	def ApplyRules(self):
		""" Применение правил обработки """
		dy, dm           = self.workspace.DyDm()
		operations       = C90_Operations()

		idos : list[str] = operations.OperationsIdosInDyDmDd(dy, dm)

		dialog_progress  = QProgressDialog(self)
		dialog_progress.setWindowTitle("Обработка операций")
		dialog_progress.setMaximum(len(idos))
		dialog_progress.setWindowModality(Qt.WindowModality.WindowModal)
		dialog_progress.setLabelText(f"Осталось обработать: {dialog_progress.maximum()} записей")
		dialog_progress.setMinimumWidth(480)
		dialog_progress.forceShow()

		for ido in idos:
			dialog_progress.setValue(dialog_progress.value() + 1)
			dialog_progress.setLabelText(f"Осталось обработать: {dialog_progress.maximum() - dialog_progress.value()} записей")

			operation = C90_Operation(ido)

			match self._processing_rule_types:
				case RULES.REPLACE_DESCRIPTION: operation.ApplyAutoreplaceDescription()
				case RULES.MATCH_DESTINATION  : operation.ApplyMatchDestination()
				case RULES.DETECT_LABEL       : operation.ApplyDetectLabels()

		dialog_progress.close()

	# Правило обработки
	def CreateRule(self):
		""" Создание правила обработки """
		rule = C90_ProcessingRule()
		rule.GenerateIdo()
		rule.RegisterObject(CONTAINERS.DISK)

		rule.RuleType(self._processing_rule_types)

		self.workspace.IdoRule(rule.Ido().data)

	def DeleteRule(self):
		""" Удаление правила обработки """
		rule = C90_ProcessingRule(self._processing_ido)

		if not RequestConfirm("Правило обработки", f"Удаление правила обработки.\n\n{'\n'.join(rule.OutputAsStrings())}"): return

		rule.DeleteObject(CONTAINERS.DISK)

	# Инструменты обработки описания
	def EditToolsDescriptionInclude(self):
		""" Редактирование обработки описания: Содержит """
		text : str | None = RequestText("Обработка описания", "Описание содержит:", self._tools_description_include)
		if text is None: return

		self._tools_description_include = text

	def SelectToolsDescriptionInclude(self):
		""" Выбор обработки описания: Содержит """
		dy, dm                       = self.workspace.DyDm()

		operation                    = C90_Operation()
		idc             : str        = operation.Idc().data
		idp_dy          : str        = operation.f_dy.Idp().data
		idp_dm          : str        = operation.f_dm.Idp().data
		idp_description : str        = operation.f_description.Idp().data

		filter_data                  = C30_FilterLinear1D(idc)
		filter_data.FilterIdpVlpByEqual(idp_dy, dy)
		filter_data.FilterIdpVlpByEqual(idp_dm, dm)
		filter_data.Capture(CONTAINERS.DISK)

		raw_data        : list[str]  = filter_data.ToStrings(idp_description, True).data
		data            : set[str]   = set()

		for raw_subdata in raw_data:
			data.add(raw_subdata)
			data = data.union(set(raw_subdata.split(' ')))

		text            : str | None = RequestText("Обработка описания", "Описание содержит:", self._tools_description_include, list(sorted(data)))
		if text is None: return

		self._tools_description_include = text

	def EditToolsDescriptionApplies(self):
		""" Редактирование обработки описания: Применяется """
		text : str | None = RequestText("Обработка описания", "Применяется:", self._tools_description_applies)
		if text is None: return

		self._tools_description_applies = text

	def ProcessingDescription(self):
		""" Обработка описания """
		dy, dm           = self.workspace.DyDm()
		operations       = C90_Operations()

		idos : list[str] = operations.OperationsIdosInDyDmDd(dy, dm)

		dialog_progress  = QProgressDialog(self)
		dialog_progress.setWindowTitle("Обработка описания")
		dialog_progress.setMaximum(len(idos))
		dialog_progress.setWindowModality(Qt.WindowModality.WindowModal)
		dialog_progress.setLabelText(f"Осталось обработать: {dialog_progress.maximum()} записей")
		dialog_progress.setMinimumWidth(480)
		dialog_progress.forceShow()

		for ido in idos:
			dialog_progress.setValue(dialog_progress.value() + 1)
			dialog_progress.setLabelText(f"Осталось обработать: {dialog_progress.maximum() - dialog_progress.value()} записей")

			operation         = C90_Operation(ido)
			description : str = operation.Description().replace(self._tools_description_include, self._tools_description_applies)
			operation.Description(description)

		dialog_progress.close()

	# Инструменты обработки назначения
	def EditToolsDestinationInclude(self):
		""" Редактирование обработки назначения: Содержит """
		text : str | None = RequestText("Обработка назначения", "Назначение содержит:", self._tools_destination_include)
		if text is None: return

		self._tools_destination_include = text

	def SelectToolsDestinationInclude(self):
		""" Выбор обработки назначения: Содержит """
		dy, dm                       = self.workspace.DyDm()

		operation                    = C90_Operation()
		idc             : str        = operation.Idc().data
		idp_dy          : str        = operation.f_dy.Idp().data
		idp_dm          : str        = operation.f_dm.Idp().data
		idp_destination : str        = operation.f_destination.Idp().data

		filter_data                  = C30_FilterLinear1D(idc)
		filter_data.FilterIdpVlpByEqual(idp_dy, dy)
		filter_data.FilterIdpVlpByEqual(idp_dm, dm)
		filter_data.Capture(CONTAINERS.DISK)

		raw_data        : list[str]  = filter_data.ToStrings(idp_destination, True).data
		data            : set[str]   = set()

		for raw_subdata in raw_data:
			data.add(raw_subdata)
			data = data.union(set(raw_subdata.split(' ')))

		text            : str | None = RequestText("Обработка назначения", "Назначение содержит:", self._tools_destination_include, list(sorted(data)))
		if text is None: return

		self._tools_destination_include = text

	def EditToolsDestinationApplies(self):
		""" Редактирование обработки назначения: Применяется """
		text : str | None = RequestText("Обработка назначения", "Применяется:", self._tools_destination_applies)
		if text is None: return

		self._tools_destination_applies = text

	def ProcessingDestination(self):
		""" Обработка назначения """
		dy, dm           = self.workspace.DyDm()
		operations       = C90_Operations()

		idos : list[str] = operations.OperationsIdosInDyDmDd(dy, dm)

		dialog_progress  = QProgressDialog(self)
		dialog_progress.setWindowTitle("Обработка описания")
		dialog_progress.setMaximum(len(idos))
		dialog_progress.setWindowModality(Qt.WindowModality.WindowModal)
		dialog_progress.setLabelText(f"Осталось обработать: {dialog_progress.maximum()} записей")
		dialog_progress.setMinimumWidth(480)
		dialog_progress.forceShow()

		for ido in idos:
			dialog_progress.setValue(dialog_progress.value() + 1)
			dialog_progress.setLabelText(f"Осталось обработать: {dialog_progress.maximum() - dialog_progress.value()} записей")

			operation          = C90_Operation(ido)
			destinations : str = operation.Destination().replace(self._tools_destination_include, self._tools_destination_applies)
			operation.Destination(destinations)

		dialog_progress.close()

	# Инструменты обработки меток
	def EditToolsLabelsInclude(self):
		""" Редактирование параметра Содержит обработки меток """
		caption  : str = ""

		match self._tools_labels_mode:
			case MODES.REPLACE: caption = "Метки содержат:"
			case MODES.APPEND : caption = "Описание или назначение содержит:"
			case MODES.EXPAND : caption = "Метки содержат:"

		texts : list[str] | None = RequestMultipleText("Обработка меток", caption, self._tools_labels_include)
		if texts is None: return

		self._tools_labels_include = list(filter(bool, sorted(texts)))

	def SelectToolsLabelsInclude(self):
		""" Выбор обработки назначения: Содержит """
		dy, dm                       = self.workspace.DyDm()

		operation                    = C90_Operation()
		idc             : str        = operation.Idc().data
		idp_dy          : str        = operation.f_dy.Idp().data
		idp_dm          : str        = operation.f_dm.Idp().data
		idp_description : str        = operation.f_description.Idp().data
		idp_destination : str        = operation.f_destination.Idp().data
		idp_labels      : str        = operation.f_labels.Idp().data

		filter_data                  = C30_FilterLinear1D(idc)
		filter_data.FilterIdpVlpByEqual(idp_dy, dy)
		filter_data.FilterIdpVlpByEqual(idp_dm, dm)
		filter_data.Capture(CONTAINERS.DISK)

		raw_data        : list[str]  = []

		match self._tools_labels_mode:
			case MODES.REPLACE:
				raw_data = filter_data.ToStrings(idp_labels, True).data

			case MODES.APPEND :
				raw_data = filter_data.ToStrings(idp_description, True).data
				raw_data.extend(filter_data.ToStrings(idp_destination, True).data)

			case MODES.EXPAND :
				raw_data = filter_data.ToStrings(idp_labels, True).data

		data            : set[str]   = set()

		for raw_subdata in raw_data:
			match self._tools_labels_mode:
				case MODES.REPLACE:
					data = data.union(set(raw_subdata.split('\n')))

				case MODES.APPEND:
					data = data.union(set(raw_subdata.split(' ')))

				case MODES.EXPAND:
					data = data.union(set(raw_subdata.split('\n')))

		try   : data.remove('')
		except: pass

		caption         : str        = ""

		match self._tools_labels_mode:
			case MODES.REPLACE: caption = "Метки содержат:"
			case MODES.APPEND : caption = "Описание или назначение содержит:"
			case MODES.EXPAND : caption = "Метки содержат:"

		texts           : list[str] | None = RequestItems("Обработка меток", caption, list(sorted(data)), self._tools_labels_include)
		if texts is None: return

		self._tools_labels_include = texts

	def EditToolsLabelsApplies(self):
		""" Редактирование параметра Применяется обработки меток """
		texts : list[str] | None = RequestMultipleText("Обработка меток", "Применяются метки:", self._tools_labels_applies)
		if texts is None: return

		self._tools_labels_applies = list(filter(bool, sorted(texts)))

	def ProcessingLabels(self):
		""" Обработка меток """
		pass

# ФОРМА ОБРАБОТКА ДАННЫХ: МЕХАНИКА ДАННЫХ
# 22 мар 2025

from PySide6.QtCore      import Qt

from G10_list            import ClearList

from L00_form_processing import OBJECTS_TYPE, PROCESSING_FIELDS
from L00_rules           import RULES
from L20_PySide6         import C20_StandardItem, ROLES, RequestMultipleText, RequestText
from L50_form_processing import C50_FormProcessing
from L90_rules import C90_ProcessingRule


class C60_FormProcessing(C50_FormProcessing):
	""" Форма Обработка данных: Механика данных """

	# Объект обработки данных
	@property
	def processing_objects_type(self) -> OBJECTS_TYPE:
		return self._processing_object_type

	@processing_objects_type.setter
	def processing_objects_type(self, objects_type: OBJECTS_TYPE):
		self._processing_object_type = objects_type

	def SwitchProcessingObjectsTypeToOperations(self):
		""" Смена типа объектов на операции """
		self.processing_objects_type = OBJECTS_TYPE.OPERATIONS

		self.on_ProcessingObjectsTypeChanged()


	# Тип правил обработки данных
	@property
	def processing_rules_type(self) -> RULES:
		return self._processing_rules_type

	@processing_rules_type.setter
	def processing_rules_type(self, rules_type: RULES):
		self._processing_rules_type = rules_type

	def SwitchProcessingRulesTypeToReplaceDescription(self):
		""" Смена типа правил на замену фрагмента описания """
		self.processing_rules_type = RULES.REPLACE_DESCRIPTION

		self.on_ProcessingRulesTypeChanged()


	# Рабочее поле
	@property
	def processing_field(self) -> PROCESSING_FIELDS:
		return self._processing_field

	@processing_field.setter
	def processing_field(self, field: PROCESSING_FIELDS):
		self._processing_field = field

	def ReadProcessingFieldFromTreeDataManual(self):
		"""  Чтение из дерева данных ручной обработки """
		self.processing_field = PROCESSING_FIELDS(self.TreeDataManual.currentIndex().data(ROLES.IDO))


	# Рабочее IDO
	@property
	def processing_ido(self) -> str:
		return self._processing_ido

	@processing_ido.setter
	def processing_ido(self, ido: str):
		self._processing_ido = ido


	# Параметр ручной обработки: Описание включает
	def ReadManualDescriptionInclude(self):
		""" Чтение параметра из дерева данных """
		item : C20_StandardItem | None = self.ModelDataManual.itemByData(PROCESSING_FIELDS.DESCRIPTION_INCLUDE,
		                                                                 ROLES.IDO)

		self._manual_description_include.enable = False if item is None else item.checkState() == Qt.CheckState.Checked

	def SetManualDescriptionInclude(self):
		""" Установка параметра """
		dy, dm                   = self.Workspace.DyDm()

		words : list[str] | None = RequestMultipleText("Обработка данных",
						                               "Описание включает:",
						                               self._manual_description_include.data,
						                               ClearList(' '.join(self.Operations.Descriptions(dy, dm)).split(' ')))
		if words is None: return

		self._manual_description_include.data = ClearList(words, clear_simbols=False, clear_short=False, clear_numbers=False)

		self.on_OptionsManualChanged()


	# Параметр ручной обработки: Описание исключает
	def ReadManualDescriptionExclude(self):
		""" Чтение параметра из дерева данных """
		item : C20_StandardItem | None = self.ModelDataManual.itemByData(PROCESSING_FIELDS.DESCRIPTION_EXCLUDE,
		                                                                 ROLES.IDO)

		self._manual_description_exclude.enable = False if item is None else item.checkState() == Qt.CheckState.Checked

	def SetManualDescriptionExclude(self):
		""" Установка параметра """
		dy, dm                   = self.Workspace.DyDm()

		words : list[str] | None = RequestMultipleText("Обработка данных",
						                               "Описание исключает:",
						                               self._manual_description_exclude.data,
						                               ClearList(' '.join(self.Operations.Descriptions(dy, dm)).split(' ')))
		if words is None: return

		self._manual_description_exclude.data = ClearList(words, clear_simbols=False, clear_short=False, clear_numbers=False)

		self.on_OptionsManualChanged()


	# Параметр ручной обработки: Замена фрагмента описания
	def ReadManualDescriptionReplace(self):
		""" Чтение параметра из дерева данных """
		item : C20_StandardItem | None = self.ModelDataManual.itemByData(PROCESSING_FIELDS.DESCRIPTION_REPLACE,
		                                                                 ROLES.IDO)

		self._manual_description_replace.enable = False if item is None else item.checkState() == Qt.CheckState.Checked

	def SetManualDescriptionReplace(self):
		""" Установка параметра """
		text : str | None = RequestText("Обработка данных",
		                                "Замена фрагментов описания: " +', '.join(self._manual_description_include.data),
		                                self._manual_description_replace.data,
		                                ClearList(' '.join(self.Operations.Descriptions()).split(' ')))
		if text is None: return

		self._manual_description_replace.data = text

		self.on_OptionsManualChanged()


	# Параметр ручной обработки: Дополнение описания
	def ReadManualDescriptionAdd(self):
		""" Чтение параметра из дерева данных """
		item : C20_StandardItem | None = self.ModelDataManual.itemByData(PROCESSING_FIELDS.DESCRIPTION_ADD,
		                                                                 ROLES.IDO)

		self._manual_description_add.enable = False if item is None else item.checkState() == Qt.CheckState.Checked

	def SetManualDescriptionAdd(self):
		""" Установка параметра """
		text : str | None = RequestText("Обработка данных",
		                                "Дополнение описания:",
		                                self._manual_description_add.data,
		                                ClearList(' '.join(self.Operations.Descriptions()).split(' ')))
		if text is None: return

		self._manual_description_add.data = text

		self.on_OptionsManualChanged()


	# Параметр ручной обработки: Замена описания
	def ReadManualDescriptionSet(self):
		""" Чтение параметра из дерева данных """
		item : C20_StandardItem | None = self.ModelDataManual.itemByData(PROCESSING_FIELDS.DESCRIPTION_SET,
		                                                                 ROLES.IDO)

		self._manual_description_set.enable = False if item is None else item.checkState() == Qt.CheckState.Checked

	def SetManualDescriptionSet(self):
		""" Установка параметра """
		text : str | None = RequestText("Обработка данных",
		                                "Замена описания:",
		                                self._manual_description_set.data,
		                                self.Operations.Descriptions())
		if text is None: return

		self._manual_description_set.data = text

		self.on_OptionsManualChanged()


	# Параметр ручной обработки: Добавление метки
	def ReadManualLabelsAdd(self):
		""" Чтение параметра из дерева данных """
		item : C20_StandardItem | None = self.ModelDataManual.itemByData(PROCESSING_FIELDS.LABELS_ADD,
		                                                                 ROLES.IDO)

		self._manual_labels_add.enable = False if item is None else item.checkState() == Qt.CheckState.Checked

	def SetManualLabelsAdd(self):
		""" Установка параметра """
		labels : list[str] | None = RequestMultipleText("Обработка операций",
		                                                "Добавление меток",
		                                                self._manual_labels_add.data,
		                                                ClearList(self.Operations.Labels()))
		if labels is None: return

		self._manual_labels_add.data = ClearList(labels, clear_short=False)

		self.on_OptionsManualChanged()


	# Параметр ручной обработки: Метки не содержат
	def ReadManualLabelsExclude(self):
		""" Чтение параметра из дерева данных """
		item : C20_StandardItem | None = self.ModelDataManual.itemByData(PROCESSING_FIELDS.LABELS_EXCLUDE,
		                                                                 ROLES.IDO)

		self._manual_labels_exclude.enable = False if item is None else item.checkState() == Qt.CheckState.Checked

	def SetManualLabelsExclude(self):
		""" Установка параметра """
		dy, dm                    = self.Workspace.DyDm()
		labels : list[str] | None = RequestMultipleText("Обработка операций",
		                                                "Метки не содержат",
		                                                self._manual_labels_exclude.data,
		                                                ClearList(self.Operations.Labels(dy, dm)))
		if labels is None: return

		self._manual_labels_exclude.data = ClearList(labels, clear_short=False)

		self.on_OptionsManualChanged()


	# Параметр ручной обработки: Метки содержат
	def ReadManualLabelsInclude(self):
		""" Чтение параметра из дерева данных """
		item : C20_StandardItem | None = self.ModelDataManual.itemByData(PROCESSING_FIELDS.LABELS_INCLUDE,
		                                                                 ROLES.IDO)

		self._manual_labels_include.enable = False if item is None else item.checkState() == Qt.CheckState.Checked

	def SetManualLabelsInclude(self):
		""" Установка параметра """
		dy, dm                    = self.Workspace.DyDm()
		labels : list[str] | None = RequestMultipleText("Обработка операций",
		                                                "Метки содержат",
		                                                self._manual_labels_include.data,
		                                                ClearList(self.Operations.Labels(dy, dm)))
		if labels is None: return

		self._manual_labels_include.data = ClearList(labels, clear_short=False)

		self.on_OptionsManualChanged()


	# Параметр ручной обработки: Убрать метку
	def ReadManualLabelsRemove(self):
		""" Чтение параметра из дерева данных """
		item : C20_StandardItem | None = self.ModelDataManual.itemByData(PROCESSING_FIELDS.LABELS_REMOVE,
		                                                                 ROLES.IDO)

		self._manual_labels_remove.enable = False if item is None else item.checkState() == Qt.CheckState.Checked

	def SetManualLabelsRemove(self):
		""" Установка параметра """
		dy, dm                    = self.Workspace.DyDm()
		labels : list[str] | None = RequestMultipleText("Обработка операций",
		                                                "Убрать метки",
		                                                self._manual_labels_remove.data,
		                                                ClearList(self.Operations.Labels(dy, dm)))
		if labels is None: return

		self._manual_labels_remove.data = ClearList(labels, clear_short=False)

		self.on_OptionsManualChanged()


	# Параметр ручной обработки: Заменить метку
	def ReadManualLabelsReplace(self):
		""" Чтение параметра из дерева данных """
		item : C20_StandardItem | None = self.ModelDataManual.itemByData(PROCESSING_FIELDS.LABELS_REPLACE,
		                                                                 ROLES.IDO)

		self._manual_labels_replace.enable = False if item is None else item.checkState() == Qt.CheckState.Checked

	def SetManualLabelsReplace(self):
		""" Установка параметра """
		dy, dm            = self.Workspace.DyDm()
		text : str | None = RequestText("Обработка данных",
		                                "Замена меток: " + ', '.join(self._manual_labels_include.data),
		                                self._manual_labels_replace.data,
		                                ClearList(self.Operations.Labels(dy, dm)))
		if text is None: return

		self._manual_labels_replace.data   = text

		self.on_OptionsManualChanged()


	# Модель данных ручной обработки
	def InitModelDataManual(self):
		""" Инициализация модели данных ручной обработки """
		self.ModelDataManual.removeAll()

		self.ModelDataManual.setHorizontalHeaderLabels(["Параметр", "Значение"])

		items             = [PROCESSING_FIELDS.DESCRIPTION_INCLUDE,
		                     PROCESSING_FIELDS.DESCRIPTION_EXCLUDE,
					         PROCESSING_FIELDS.LABELS_INCLUDE,
					         PROCESSING_FIELDS.LABELS_EXCLUDE,
		                     ]

		group_filter      = C20_StandardItem("Параметры фильтрации")

		for item in items:
			item_field        = C20_StandardItem(title        = item,
			                                     data         = item,
			                                     data_role    = ROLES.IDO,
			                                     flag_checked = False)
			item_value        = C20_StandardItem("",
			                                     item,
			                                     ROLES.IDO)
			group_filter.appendRow([item_field, item_value])

		self.ModelDataManual.appendRow([group_filter, C20_StandardItem("")])


		items             = [PROCESSING_FIELDS.DESCRIPTION_ADD,
							 PROCESSING_FIELDS.DESCRIPTION_REPLACE,
					         PROCESSING_FIELDS.DESCRIPTION_SET,
					         PROCESSING_FIELDS.LABELS_ADD,
		                     PROCESSING_FIELDS.LABELS_REPLACE,
		                     PROCESSING_FIELDS.LABELS_REMOVE,
		                     ]

		group_processing  = C20_StandardItem("Параметры обработки")

		for item in items:
			item_field        = C20_StandardItem(title        = item,
			                                     data         = item,
			                                     data_role    = ROLES.IDO,
			                                     flag_checked = False)
			item_value        = C20_StandardItem("",
			                                     item,
			                                     ROLES.IDO)
			group_processing.appendRow([item_field, item_value])

		self.ModelDataManual.appendRow([group_processing, C20_StandardItem("")])

	def LoadModelDataManual(self):
		""" Загрузка данных в модель данных ручной обработки """
		if self.ModelDataManual.checkIdo(PROCESSING_FIELDS.DESCRIPTION_INCLUDE):
			item_value = self.ModelDataManual.itemFromIndex(self.ModelDataManual.indexesInRowByIdo(PROCESSING_FIELDS.DESCRIPTION_INCLUDE)[1])
			item_value.setText('\n'.join(self._manual_description_include.data))

		if self.ModelDataManual.checkIdo(PROCESSING_FIELDS.DESCRIPTION_EXCLUDE):
			item_value = self.ModelDataManual.itemFromIndex(self.ModelDataManual.indexesInRowByIdo(PROCESSING_FIELDS.DESCRIPTION_EXCLUDE)[1])
			item_value.setText('\n'.join(self._manual_description_exclude.data))

		if self.ModelDataManual.checkIdo(PROCESSING_FIELDS.DESCRIPTION_REPLACE):
			item_value = self.ModelDataManual.itemFromIndex(self.ModelDataManual.indexesInRowByIdo(PROCESSING_FIELDS.DESCRIPTION_REPLACE)[1])
			item_value.setText(self._manual_description_replace.data)

		if self.ModelDataManual.checkIdo(PROCESSING_FIELDS.DESCRIPTION_SET):
			item_value = self.ModelDataManual.itemFromIndex(self.ModelDataManual.indexesInRowByIdo(PROCESSING_FIELDS.DESCRIPTION_SET)[1])
			item_value.setText(self._manual_description_set.data)

		if self.ModelDataManual.checkIdo(PROCESSING_FIELDS.DESCRIPTION_ADD):
			item_value = self.ModelDataManual.itemFromIndex(self.ModelDataManual.indexesInRowByIdo(PROCESSING_FIELDS.DESCRIPTION_ADD)[1])
			item_value.setText(self._manual_description_add.data)

		if self.ModelDataManual.checkIdo(PROCESSING_FIELDS.LABELS_ADD):
			item_value = self.ModelDataManual.itemFromIndex(self.ModelDataManual.indexesInRowByIdo(PROCESSING_FIELDS.LABELS_ADD)[1])
			item_value.setText('\n'.join(self._manual_labels_add.data))

		if self.ModelDataManual.checkIdo(PROCESSING_FIELDS.LABELS_EXCLUDE):
			item_value = self.ModelDataManual.itemFromIndex(self.ModelDataManual.indexesInRowByIdo(PROCESSING_FIELDS.LABELS_EXCLUDE)[1])
			item_value.setText('\n'.join(self._manual_labels_exclude.data))

		if self.ModelDataManual.checkIdo(PROCESSING_FIELDS.LABELS_INCLUDE):
			item_value = self.ModelDataManual.itemFromIndex(self.ModelDataManual.indexesInRowByIdo(PROCESSING_FIELDS.LABELS_INCLUDE)[1])
			item_value.setText('\n'.join(self._manual_labels_include.data))

		if self.ModelDataManual.checkIdo(PROCESSING_FIELDS.LABELS_REMOVE):
			item_value = self.ModelDataManual.itemFromIndex(self.ModelDataManual.indexesInRowByIdo(PROCESSING_FIELDS.LABELS_REMOVE)[1])
			item_value.setText('\n'.join(self._manual_labels_remove.data))

		if self.ModelDataManual.checkIdo(PROCESSING_FIELDS.LABELS_REPLACE):
			item_value = self.ModelDataManual.itemFromIndex(self.ModelDataManual.indexesInRowByIdo(PROCESSING_FIELDS.LABELS_REPLACE)[1])
			item_value.setText(self._manual_labels_replace.data)


	# Модель данных автоматической обработки
	def InitModelDataAuto(self):
		""" Инициализация модели данных автоматической обработки """
		self.ModelDataAuto.removeAll()

		match self.processing_rules_type:
			case RULES.REPLACE_DESCRIPTION: self.ModelDataAuto.setHorizontalHeaderLabels(["Поиск фрагмента", "Условие пропуска", "Замена на фрагмент"])

	def LoadRuleReplaceDescriptionInModel(self):
		""" Загрузка правила обработки замены описания в модель """
		if not self.processing_ido: return

		rule        = C90_ProcessingRule(self.processing_ido)

		if not self.ModelDataAuto.checkIdo(self.processing_ido):
			item_input  = C20_StandardItem("")
			item_input.setData(self.processing_ido, ROLES.IDO)

			item_output = C20_StandardItem("")
			item_output.setData(self.processing_ido, ROLES.IDO)

			item_block  = C20_StandardItem("")
			item_block.setData(self.processing_ido, ROLES.IDO)

			self.ModelDataAuto.appendRow([item_input, item_block, item_output])

		indexes     = self.ModelDataAuto.indexesInRowByIdo(self.processing_ido)
		item_input  = self.ModelDataAuto.itemFromIndex(indexes[0])
		item_input.setText('\n'.join(rule.inputs))

		item_block  = self.ModelDataAuto.itemFromIndex(indexes[1])
		item_block.setText('\n'.join(rule.blocks))

		item_output = self.ModelDataAuto.itemFromIndex(indexes[2])
		item_output.setText('\n'.join(rule.outputs))

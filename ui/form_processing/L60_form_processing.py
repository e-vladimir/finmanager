# ФОРМА ОБРАБОТКА ДАННЫХ: МЕХАНИКА ДАННЫХ
# 22 мар 2025

from PySide6.QtCore      import Qt

from G10_list            import ClearList

from L00_colors          import COLORS
from L00_form_processing import OBJECTS_TYPE, PROCESSING_FIELDS
from L20_PySide6         import C20_StandardItem, ROLES, RequestItem, RequestMultipleText, RequestText
from L50_form_processing import C50_FormProcessing


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


	# Рабочий PID
	@property
	def processing_idp(self) -> str:
		return self._processing_idp

	@processing_idp.setter
	def processing_idp(self, idp: str):
		self._processing_idp = idp


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


	# Параметр ручной обработки: Дополнение назначения
	def ReadManualDestinationAdd(self):
		""" Чтение параметра из дерева данных """
		item : C20_StandardItem | None = self.ModelDataManual.itemByData(PROCESSING_FIELDS.DESTINATION_ADD,
		                                                                 ROLES.IDO)

		self._manual_destination_add.enable = False if item is None else item.checkState() == Qt.CheckState.Checked

	def SetManualDestinationAdd(self):
		""" Установка параметра """
		text : str | None = RequestText("Обработка данных",
		                                "Дополнение назначения:",
		                                self._manual_destination_add.data,
		                                ClearList(' '.join(self.Operations.Destinations()).split(' ')))
		if text is None: return

		self._manual_destination_add.data = text

		self.on_OptionsManualChanged()


	# Параметр ручной обработки: Описание включает
	def ReadManualDestinationInclude(self):
		""" Чтение параметра из дерева данных """
		item : C20_StandardItem | None = self.ModelDataManual.itemByData(PROCESSING_FIELDS.DESTINATION_INCLUDE,
		                                                                 ROLES.IDO)

		self._manual_destination_include.enable = False if item is None else item.checkState() == Qt.CheckState.Checked

	def SetManualDestinationInclude(self):
		""" Установка параметра """
		dy, dm                   = self.Workspace.DyDm()

		words : list[str] | None = RequestMultipleText("Обработка данных",
						                               "Назначение включает:",
						                               self._manual_destination_include.data,
						                               ClearList(' '.join(self.Operations.Destinations(dy, dm)).split(' ')))
		if words is None: return

		self._manual_destination_include.data = ClearList(words, clear_simbols=False, clear_short=False, clear_numbers=False)

		self.on_OptionsManualChanged()


	# Параметр ручной обработки: Описание исключает
	def ReadManualDestinationExclude(self):
		""" Чтение параметра из дерева данных """
		item : C20_StandardItem | None = self.ModelDataManual.itemByData(PROCESSING_FIELDS.DESTINATION_EXCLUDE,
		                                                                 ROLES.IDO)

		self._manual_destination_exclude.enable = False if item is None else item.checkState() == Qt.CheckState.Checked

	def SetManualDestinationExclude(self):
		""" Установка параметра """
		dy, dm                   = self.Workspace.DyDm()

		words : list[str] | None = RequestMultipleText("Обработка данных",
						                               "Назначение исключает:",
						                               self._manual_destination_exclude.data,
						                               ClearList(' '.join(self.Operations.Destinations(dy, dm)).split(' ')))
		if words is None: return

		self._manual_destination_exclude.data = ClearList(words, clear_simbols=False, clear_short=False, clear_numbers=False)

		self.on_OptionsManualChanged()


	# Параметр ручной обработки: Замена фрагмента назначения
	def ReadManualDestinationReplace(self):
		""" Чтение параметра из дерева данных """
		item : C20_StandardItem | None = self.ModelDataManual.itemByData(PROCESSING_FIELDS.DESTINATION_REPLACE,
		                                                                 ROLES.IDO)

		self._manual_destination_replace.enable = False if item is None else item.checkState() == Qt.CheckState.Checked

	def SetManualDestinationReplace(self):
		""" Установка параметра """
		text : str | None = RequestText("Обработка данных",
		                                "Замена фрагментов назначения: " +', '.join(self._manual_destination_include.data),
		                                self._manual_destination_replace.data,
		                                ClearList(' '.join(self.Operations.Destinations()).split(' ')))
		if text is None: return

		self._manual_destination_replace.data = text

		self.on_OptionsManualChanged()


	# Параметр ручной обработки: Замена назначения
	def ReadManualDestinationSet(self):
		""" Чтение параметра из дерева данных """
		item : C20_StandardItem | None = self.ModelDataManual.itemByData(PROCESSING_FIELDS.DESTINATION_SET,
		                                                                 ROLES.IDO)

		self._manual_destination_set.enable = False if item is None else item.checkState() == Qt.CheckState.Checked

	def SetManualDestinationSet(self):
		""" Установка параметра """
		text : str | None = RequestText("Обработка данных",
		                                "Замена назначения:",
		                                self._manual_destination_set.data,
		                                self.Operations.Destinations())
		if text is None: return

		self._manual_destination_set.data = text

		self.on_OptionsManualChanged()


	# Параметр ручной обработки: Установить цветовую метку
	def ReadManualColorSet(self):
		""" Чтение параметра из дерева данных """
		item : C20_StandardItem | None = self.ModelDataManual.itemByData(PROCESSING_FIELDS.COLOR_SET,
		                                                                 ROLES.IDO)

		self._manual_color_set.enable = False if item is None else item.checkState() == Qt.CheckState.Checked

	def SetManualColorSet(self):
		""" Установка параметра """
		color : str | None = RequestItem("Обработка данных",
		                                "Установка цветовой метки:",
		                                [COLORS.BLACK, COLORS.GRAY, COLORS.BLUE, COLORS.GREEN, COLORS.RED])
		if color is None: return

		self._manual_color_set.data = color

		self.on_OptionsManualChanged()


	# Параметр ручной обработки: Установить пропуск операции
	def ReadManualSkipSet(self):
		""" Чтение параметра из дерева данных """
		item : C20_StandardItem | None = self.ModelDataManual.itemByData(PROCESSING_FIELDS.SKIP_SET,
		                                                                 ROLES.IDO)

		self._manual_skip_set.enable = False if item is None else item.checkState() == Qt.CheckState.Checked

	def SwitchManualSkipSet(self):
		""" Установка параметра """
		self._manual_skip_set.data = not self._manual_skip_set.data

		self.on_OptionsManualChanged()


	# Модель данных ручной обработки
	def InitModelDataManual(self):
		""" Инициализация модели данных ручной обработки """
		self.ModelDataManual.removeAll()

		self.ModelDataManual.setHorizontalHeaderLabels(["Параметр", "Значение"])

		items             = [PROCESSING_FIELDS.DESCRIPTION_INCLUDE,
		                     PROCESSING_FIELDS.DESCRIPTION_EXCLUDE,
		                     PROCESSING_FIELDS.DESTINATION_INCLUDE,
		                     PROCESSING_FIELDS.DESTINATION_EXCLUDE,
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


		items             = [PROCESSING_FIELDS.DESTINATION_ADD,
							 PROCESSING_FIELDS.DESTINATION_REPLACE,
					         PROCESSING_FIELDS.DESTINATION_SET,
		                     PROCESSING_FIELDS.COLOR_SET,
		                     PROCESSING_FIELDS.SKIP_SET,
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

		if self.ModelDataManual.checkIdo(PROCESSING_FIELDS.DESTINATION_ADD):
			item_value = self.ModelDataManual.itemFromIndex(self.ModelDataManual.indexesInRowByIdo(PROCESSING_FIELDS.DESTINATION_ADD)[1])
			item_value.setText(self._manual_destination_add.data)

		if self.ModelDataManual.checkIdo(PROCESSING_FIELDS.DESTINATION_INCLUDE):
			item_value = self.ModelDataManual.itemFromIndex(self.ModelDataManual.indexesInRowByIdo(PROCESSING_FIELDS.DESTINATION_INCLUDE)[1])
			item_value.setText('\n'.join(self._manual_destination_include.data))

		if self.ModelDataManual.checkIdo(PROCESSING_FIELDS.DESTINATION_EXCLUDE):
			item_value = self.ModelDataManual.itemFromIndex(self.ModelDataManual.indexesInRowByIdo(PROCESSING_FIELDS.DESTINATION_EXCLUDE)[1])
			item_value.setText('\n'.join(self._manual_destination_exclude.data))

		if self.ModelDataManual.checkIdo(PROCESSING_FIELDS.DESTINATION_REPLACE):
			item_value = self.ModelDataManual.itemFromIndex(self.ModelDataManual.indexesInRowByIdo(PROCESSING_FIELDS.DESTINATION_REPLACE)[1])
			item_value.setText(self._manual_destination_replace.data)

		if self.ModelDataManual.checkIdo(PROCESSING_FIELDS.DESTINATION_SET):
			item_value = self.ModelDataManual.itemFromIndex(self.ModelDataManual.indexesInRowByIdo(PROCESSING_FIELDS.DESTINATION_SET)[1])
			item_value.setText(self._manual_destination_set.data)

		if self.ModelDataManual.checkIdo(PROCESSING_FIELDS.COLOR_SET):
			item_value = self.ModelDataManual.itemFromIndex(self.ModelDataManual.indexesInRowByIdo(PROCESSING_FIELDS.COLOR_SET)[1])
			item_value.setText(self._manual_color_set.data)

		if self.ModelDataManual.checkIdo(PROCESSING_FIELDS.SKIP_SET):
			item_value = self.ModelDataManual.itemFromIndex(self.ModelDataManual.indexesInRowByIdo(PROCESSING_FIELDS.SKIP_SET)[1])
			item_value.setText("Не учитывать операцию" if self._manual_skip_set.data else "Учитывать операцию")

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


	# Параметр ручной обработки: Исходное описание включает
	def ReadManualSrcDescriptionInclude(self):
		""" Чтение параметра из дерева данных """
		item : C20_StandardItem | None = self.ModelDataManual.itemByData(PROCESSING_FIELDS.SRC_DESCRIPTION_INCLUDE,
		                                                                 ROLES.IDO)

		self._manual_src_description_include.enable = False if item is None else item.checkState() == Qt.CheckState.Checked

	def SetManualSrcDescriptionInclude(self):
		""" Установка параметра """
		dy, dm                   = self.Workspace.DyDm()

		words : list[str] | None = RequestMultipleText("Обработка данных",
						                               "Исходное описание включает:",
						                               self._manual_src_description_include.data,
						                               ClearList(' '.join(self.Operations.SrcDescriptions(dy, dm)).split(' ')))
		if words is None: return

		self._manual_src_description_include.data = ClearList(words, clear_simbols=False, clear_short=False, clear_numbers=False)

		self.on_OptionsManualChanged()


	# Параметр ручной обработки: Исходное описание исключает
	def ReadManualSrcDescriptionExclude(self):
		""" Чтение параметра из дерева данных """
		item : C20_StandardItem | None = self.ModelDataManual.itemByData(PROCESSING_FIELDS.SRC_DESCRIPTION_EXCLUDE,
		                                                                 ROLES.IDO)

		self._manual_src_description_exclude.enable = False if item is None else item.checkState() == Qt.CheckState.Checked

	def SetManualSrcDescriptionExclude(self):
		""" Установка параметра """
		dy, dm                   = self.Workspace.DyDm()

		words : list[str] | None = RequestMultipleText("Обработка данных",
						                               "Описание исключает:",
						                               self._manual_src_description_exclude.data,
						                               ClearList(' '.join(self.Operations.SrcDescriptions(dy, dm)).split(' ')))
		if words is None: return

		self._manual_src_description_exclude.data = ClearList(words, clear_simbols=False, clear_short=False, clear_numbers=False)

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

		items             = [PROCESSING_FIELDS.SRC_DESCRIPTION_INCLUDE,
		                     PROCESSING_FIELDS.SRC_DESCRIPTION_EXCLUDE,
		                     PROCESSING_FIELDS.DESCRIPTION_INCLUDE,
		                     PROCESSING_FIELDS.DESCRIPTION_EXCLUDE,
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
		if self.ModelDataManual.checkIdo(PROCESSING_FIELDS.SRC_DESCRIPTION_INCLUDE):
			item_value = self.ModelDataManual.itemFromIndex(self.ModelDataManual.indexesInRowByIdo(PROCESSING_FIELDS.SRC_DESCRIPTION_INCLUDE)[1])
			item_value.setText('\n'.join(self._manual_src_description_include.data))

		if self.ModelDataManual.checkIdo(PROCESSING_FIELDS.SRC_DESCRIPTION_EXCLUDE):
			item_value = self.ModelDataManual.itemFromIndex(self.ModelDataManual.indexesInRowByIdo(PROCESSING_FIELDS.SRC_DESCRIPTION_EXCLUDE)[1])
			item_value.setText('\n'.join(self._manual_src_description_exclude.data))

		if self.ModelDataManual.checkIdo(PROCESSING_FIELDS.DESCRIPTION_ADD):
			item_value = self.ModelDataManual.itemFromIndex(self.ModelDataManual.indexesInRowByIdo(PROCESSING_FIELDS.DESCRIPTION_ADD)[1])
			item_value.setText(self._manual_description_add.data)

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

		if self.ModelDataManual.checkIdo(PROCESSING_FIELDS.COLOR_SET):
			item_value = self.ModelDataManual.itemFromIndex(self.ModelDataManual.indexesInRowByIdo(PROCESSING_FIELDS.COLOR_SET)[1])
			item_value.setText(self._manual_color_set.data)

		if self.ModelDataManual.checkIdo(PROCESSING_FIELDS.SKIP_SET):
			item_value = self.ModelDataManual.itemFromIndex(self.ModelDataManual.indexesInRowByIdo(PROCESSING_FIELDS.SKIP_SET)[1])
			item_value.setText("Не учитывать операцию" if self._manual_skip_set.data else "Учитывать операцию")

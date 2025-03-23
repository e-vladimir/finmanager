# ФОРМА ОБРАБОТКА ДАННЫХ: МЕХАНИКА ДАННЫХ
# 22 мар 2025

from PySide6.QtCore      import Qt

from L00_colors          import COLORS
from L00_form_processing import PROCESSING_FIELDS

from L20_PySide6         import C20_StandardItem, ROLES, RequestItem, RequestText
from L50_form_processing import C50_FormProcessing


class C60_FormProcessing(C50_FormProcessing):
	""" Форма Обработка данных: Механика данных """

	# Обработка операций: Описание содержит
	@property
	def operations_description_include(self) -> str:
		return self._operations_description_include.data

	@operations_description_include.setter
	def operations_description_include(self, text: str):
		self._operations_description_include.data = text

	def SetOperationsDescriptionInclude(self):
		""" Установка значения """
		dy, dm             = self.Workspace.DyDm()
		value : str | None = RequestText("Обработка операций",
		                                 "Описание операций содержит:",
		                                 self.operations_description_include,
		                                 self.Operations.Descriptions(dy, dm))
		if value is None: return

		self.operations_description_include = value

		self.on_ProcessingOperationsChanged()

	def ReadOperationsDescriptionInclude(self):
		""" Чтение параметра """
		indexes    = self.ModelDataOperations.indexesInRowByIdo(PROCESSING_FIELDS.DESCRIPTION_INCLUDE)
		item_value = self.ModelDataOperations.itemFromIndex(indexes[0])
		self._operations_description_include.enable = item_value.checkState() == Qt.CheckState.Checked


	# Обработка операций: Описание идентично
	@property
	def operations_description_equal(self) -> str:
		return self._operations_description_equal.data

	@operations_description_equal.setter
	def operations_description_equal(self, text: str):
		self._operations_description_equal.data = text

	def SetOperationsDescriptionEqual(self):
		""" Установка значения """
		dy, dm             = self.Workspace.DyDm()
		value : str | None = RequestText("Обработка операций",
		                                 "Описание операций идентично:",
		                                 self.operations_description_equal,
		                                 self.Operations.Descriptions(dy, dm))
		if value is None: return

		self.operations_description_equal = value

		self.on_ProcessingOperationsChanged()

	def ReadOperationsDescriptionEqual(self):
		""" Чтение параметра """
		indexes    = self.ModelDataOperations.indexesInRowByIdo(PROCESSING_FIELDS.DESCRIPTION_EQUAL)
		item_value = self.ModelDataOperations.itemFromIndex(indexes[0])
		self._operations_description_equal.enable = item_value.checkState() == Qt.CheckState.Checked


	# Обработка операций: Замена текстового фрагмента в описании
	@property
	def operations_description_replace(self) -> str:
		return self._operations_description_replace.data

	@operations_description_replace.setter
	def operations_description_replace(self, text: str):
		self._operations_description_replace.data = text

	def SetOperationsDescriptionReplace(self):
		""" Установка значения """
		value : str | None = RequestText( "Обработка операций",
		                                 f"Замена {self.operations_description_include} на:",
		                                  self.operations_description_replace)
		if value is None: return

		self.operations_description_replace = value

		self.on_ProcessingOperationsChanged()

	def ReadOperationsDescriptionReplace(self):
		""" Чтение параметра """
		indexes    = self.ModelDataOperations.indexesInRowByIdo(PROCESSING_FIELDS.DESCRIPTION_REPLACE)
		item_value = self.ModelDataOperations.itemFromIndex(indexes[0])
		self._operations_description_replace.enable = item_value.checkState() == Qt.CheckState.Checked


	# Обработка операций: Установка описания
	@property
	def operations_description_set(self) -> str:
		return self._operations_description_set.data

	@operations_description_set.setter
	def operations_description_set(self, text: str):
		self._operations_description_set.data = text

	def SetOperationsDescriptionSet(self):
		""" Установка значения """
		value : str | None = RequestText( "Обработка операций",
		                                 f"Замена описания на:",
		                                  self.operations_description_set,
		                                  self.Operations.Descriptions())
		if value is None: return

		self.operations_description_set = value

		self.on_ProcessingOperationsChanged()

	def ReadOperationsDescriptionSet(self):
		""" Чтение параметра """
		indexes    = self.ModelDataOperations.indexesInRowByIdo(PROCESSING_FIELDS.DESCRIPTION_SET)
		item_value = self.ModelDataOperations.itemFromIndex(indexes[0])
		self._operations_description_set.enable = item_value.checkState() == Qt.CheckState.Checked


	# Обработка операций: Установка цвета
	@property
	def operations_color_set(self) -> COLORS:
		return self._operations_color_set.data

	@operations_color_set.setter
	def operations_color_set(self, color: COLORS):
		self._operations_color_set.data = color

	def SetOperationsColorSet(self):
		""" Установка цвета """
		color : str | None = RequestItem("Обработка операций",
		                                 "Установка цвета",
		                                 [color for color in COLORS])
		if color is None: return

		self.operations_color_set = COLORS(color)

		self.on_ProcessingOperationsChanged()

	def ReadOperationsColorSet(self):
		""" Чтение параметра """
		indexes    = self.ModelDataOperations.indexesInRowByIdo(PROCESSING_FIELDS.COLOR_SET)
		item_value = self.ModelDataOperations.itemFromIndex(indexes[0])
		self._operations_color_set.enable = item_value.checkState() == Qt.CheckState.Checked


	# Рабочее поле
	@property
	def processing_field(self) -> PROCESSING_FIELDS:
		return self._processing_field

	@processing_field.setter
	def processing_field(self, field: PROCESSING_FIELDS):
		self._processing_field = field

	def ReadProcessingFieldFromTreeDataOperations(self):
		""" Чтение из дерева данных обработка операций """
		self.processing_field = PROCESSING_FIELDS(self.TreeDataOperations.currentIndex().data(ROLES.IDO))


	# Модель данных Обработка операций
	def InitModelDataOperation(self):
		""" Инициализация модели данных Обработка операций """
		self.ModelDataOperations.removeAll()
		self.ModelDataOperations.setHorizontalHeaderLabels(["Параметр", "Значение"])

		group_filter     = C20_StandardItem("Критерии фильтрации")
		item_field       = C20_StandardItem("Описание содержит",
		                                    data         = PROCESSING_FIELDS.DESCRIPTION_INCLUDE,
		                                    data_role    = ROLES.IDO,
		                                    flag_checked = False
		                                    )
		item_value       = C20_StandardItem("",
		                                    data         = PROCESSING_FIELDS.DESCRIPTION_INCLUDE,
		                                    data_role    = ROLES.IDO
		                                    )
		group_filter.appendRow([item_field, item_value])

		item_field       = C20_StandardItem("Описание идентично",
		                                    data         = PROCESSING_FIELDS.DESCRIPTION_EQUAL,
		                                    data_role    = ROLES.IDO,
		                                    flag_checked = False
		                                    )
		item_value       = C20_StandardItem("",
		                                    data         = PROCESSING_FIELDS.DESCRIPTION_EQUAL,
		                                    data_role    = ROLES.IDO
		                                    )
		group_filter.appendRow([item_field, item_value])

		self.ModelDataOperations.appendRow([group_filter,
		                                    C20_StandardItem("")])

		group_processing = C20_StandardItem("Обработка")
		item_field       = C20_StandardItem("Заменить фрагмент описания",
		                                    data         = PROCESSING_FIELDS.DESCRIPTION_REPLACE,
		                                    data_role    = ROLES.IDO,
		                                    flag_checked = False
		                                    )
		item_value       = C20_StandardItem("",
		                                    data         = PROCESSING_FIELDS.DESCRIPTION_REPLACE,
		                                    data_role    = ROLES.IDO
		                                    )
		group_processing.appendRow([item_field, item_value])

		item_field       = C20_StandardItem("Заменить описание",
		                                    data         = PROCESSING_FIELDS.DESCRIPTION_SET,
		                                    data_role    = ROLES.IDO,
		                                    flag_checked = False
		                                    )
		item_value       = C20_StandardItem("",
		                                    data         = PROCESSING_FIELDS.DESCRIPTION_SET,
		                                    data_role    = ROLES.IDO
		                                    )
		group_processing.appendRow([item_field, item_value])

		item_field       = C20_StandardItem("Установить цвет",
		                                    data         = PROCESSING_FIELDS.COLOR_SET,
		                                    data_role    = ROLES.IDO,
		                                    flag_checked = False
		                                    )
		item_value       = C20_StandardItem("",
		                                    data         = PROCESSING_FIELDS.COLOR_SET,
		                                    data_role    = ROLES.IDO
		                                    )
		group_processing.appendRow([item_field, item_value])

		self.ModelDataOperations.appendRow([group_processing,
		                                    C20_StandardItem("")])

	def LoadModelDataOperations(self):
		""" Загрузка данных в модель данных Обработка операций """
		indexes    = self.ModelDataOperations.indexesInRowByIdo(PROCESSING_FIELDS.DESCRIPTION_INCLUDE)
		item_value = self.ModelDataOperations.itemFromIndex(indexes[1])
		item_value.setText(self.operations_description_include)

		indexes    = self.ModelDataOperations.indexesInRowByIdo(PROCESSING_FIELDS.DESCRIPTION_REPLACE)
		item_value = self.ModelDataOperations.itemFromIndex(indexes[1])
		item_value.setText(self.operations_description_replace)

		indexes    = self.ModelDataOperations.indexesInRowByIdo(PROCESSING_FIELDS.DESCRIPTION_SET)
		item_value = self.ModelDataOperations.itemFromIndex(indexes[1])
		item_value.setText(self.operations_description_set)

		indexes    = self.ModelDataOperations.indexesInRowByIdo(PROCESSING_FIELDS.COLOR_SET)
		item_value = self.ModelDataOperations.itemFromIndex(indexes[1])
		item_value.setText(self.operations_color_set)


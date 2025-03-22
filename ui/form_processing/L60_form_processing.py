# ФОРМА ОБРАБОТКА ДАННЫХ: МЕХАНИКА ДАННЫХ
# 22 мар 2025

from L00_colors          import COLORS
from L00_form_processing import PROCESSING_FIELDS
from L20_PySide6 import C20_StandardItem, ROLES, RequestItem, RequestText
from L50_form_processing import C50_FormProcessing


class C60_FormProcessing(C50_FormProcessing):
	""" Форма Обработка данных: Механика данных """

	# Обработка операций: Описание содержит
	@property
	def operations_filter_description(self) -> str:
		return self._operations_filter_description

	@operations_filter_description.setter
	def operations_filter_description(self, text: str):
		self._operations_filter_description = text

	def SetOperationsFilterDescription(self):
		""" Установка значения """
		value : str | None = RequestText("Обработка операций",
		                                 "Описание операций содержит:",
		                                 self.operations_filter_description,
		                                 self.Operations.Descriptions())
		if value is None: return

		self.operations_filter_description = value

		self.on_ProcessingOperationsChanged()


	# Обработка операций: Замена текстового фрагмента в описании
	@property
	def operations_processing_replace_description(self) -> str:
		return self._operations_processing_replace_description

	@operations_processing_replace_description.setter
	def operations_processing_replace_description(self, text: str):
		self._operations_processing_replace_description = text

	def SetOperationsReplaceDescription(self):
		""" Установка значения """
		value : str | None = RequestText( "Обработка операций",
		                                 f"Замена {self.operations_filter_description} на:",
		                                  self.operations_processing_replace_description)
		if value is None: return

		self.operations_processing_replace_description = value

		self.on_ProcessingOperationsChanged()


	# Обработка операций: Установка описания
	@property
	def operations_processing_set_description(self) -> str:
		return self._operations_processing_set_description

	@operations_processing_set_description.setter
	def operations_processing_set_description(self, text: str):
		self._operations_processing_set_description = text

	def SetOperationsProcessingSetDescription(self):
		""" Установка значения """
		value : str | None = RequestText( "Обработка операций",
		                                 f"Замена описания на:",
		                                  self.operations_processing_replace_description,
		                                  self.Operations.Descriptions())
		if value is None: return

		self.operations_processing_set_description = value

		self.on_ProcessingOperationsChanged()


	# Обработка операций: Установка цвета
	@property
	def operations_processing_set_color(self) -> COLORS:
		return self._operations_processing_set_color

	@operations_processing_set_color.setter
	def operations_processing_set_color(self, color: COLORS):
		self._operations_processing_set_color = color

	def SetOperationsProcessingSetColor(self):
		""" Установка цвета """
		color : str | None = RequestItem("Обработка операций",
		                                 "Установка цвета",
		                                 [color for color in COLORS])
		if color is None: return

		self.operations_processing_set_color = COLORS(color)

		self.on_ProcessingOperationsChanged()

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
		                                    data         = PROCESSING_FIELDS.FILTER_DESCRIPTION,
		                                    data_role    = ROLES.IDO,
		                                    flag_checked = False
		                                    )
		item_value       = C20_StandardItem("",
		                                    data         = PROCESSING_FIELDS.FILTER_DESCRIPTION,
		                                    data_role    = ROLES.IDO
		                                    )
		group_filter.appendRow([item_field, item_value])

		self.ModelDataOperations.appendRow([group_filter,
		                                    C20_StandardItem("")])

		group_processing = C20_StandardItem("Обработка")
		item_field       = C20_StandardItem("Заменить фрагмент описания",
		                                    data         = PROCESSING_FIELDS.PROCESSING_REPLACE_DESCRIPTION,
		                                    data_role    = ROLES.IDO,
		                                    flag_checked = False
		                                    )
		item_value       = C20_StandardItem("",
		                                    data         = PROCESSING_FIELDS.PROCESSING_REPLACE_DESCRIPTION,
		                                    data_role    = ROLES.IDO
		                                    )
		group_processing.appendRow([item_field, item_value])

		item_field       = C20_StandardItem("Заменить описание",
		                                    data         = PROCESSING_FIELDS.PROCESSING_SET_DESCRIPTION,
		                                    data_role    = ROLES.IDO,
		                                    flag_checked = False
		                                    )
		item_value       = C20_StandardItem("",
		                                    data         = PROCESSING_FIELDS.PROCESSING_SET_DESCRIPTION,
		                                    data_role    = ROLES.IDO
		                                    )
		group_processing.appendRow([item_field, item_value])

		item_field       = C20_StandardItem("Установить цвет",
		                                    data         = PROCESSING_FIELDS.PROCESSING_SET_COLOR,
		                                    data_role    = ROLES.IDO,
		                                    flag_checked = False
		                                    )
		item_value       = C20_StandardItem("",
		                                    data         = PROCESSING_FIELDS.PROCESSING_SET_COLOR,
		                                    data_role    = ROLES.IDO
		                                    )
		group_processing.appendRow([item_field, item_value])

		self.ModelDataOperations.appendRow([group_processing,
		                                    C20_StandardItem("")])

	def LoadModelDataOperations(self):
		""" Загрузка данных в модель данных Обработка операций """
		indexes    = self.ModelDataOperations.indexesInRowByIdo(PROCESSING_FIELDS.FILTER_DESCRIPTION)
		item_value = self.ModelDataOperations.itemFromIndex(indexes[1])
		item_value.setText(self.operations_filter_description)

		indexes    = self.ModelDataOperations.indexesInRowByIdo(PROCESSING_FIELDS.PROCESSING_REPLACE_DESCRIPTION)
		item_value = self.ModelDataOperations.itemFromIndex(indexes[1])
		item_value.setText(self.operations_processing_replace_description)

		indexes    = self.ModelDataOperations.indexesInRowByIdo(PROCESSING_FIELDS.PROCESSING_SET_DESCRIPTION)
		item_value = self.ModelDataOperations.itemFromIndex(indexes[1])
		item_value.setText(self.operations_processing_set_description)

		indexes    = self.ModelDataOperations.indexesInRowByIdo(PROCESSING_FIELDS.PROCESSING_SET_COLOR)
		item_value = self.ModelDataOperations.itemFromIndex(indexes[1])
		item_value.setText(self.operations_processing_set_color)


# ФОРМА ОБРАБОТКА ДАННЫХ: МЕХАНИКА ДАННЫХ

from L00_form_processing import INTERVALS, OPERATIONS
from L20_PySide6         import C20_StandardItem, ROLES
from L50_form_processing import C50_FormProcessing


class C60_FormProcessing(C50_FormProcessing):
	""" Форма Обработка данных: Механика данных """

	# Модель данных Обработка операций
	def InitModelOperations(self):
		""" Инициализация модели данных Обработка операций """
		self.model_operations.removeAll()
		self.model_operations.setHorizontalHeaderLabels(["Параметр", "Значение"])

		item_group = C20_StandardItem("Критерии обработки")
		item_group.appendRow([C20_StandardItem("Фрагмент поиска",              OPERATIONS.INCLUDE, ROLES.IDO),
		                      C20_StandardItem("",                             OPERATIONS.INCLUDE, ROLES.IDO)])
		item_group.appendRow([C20_StandardItem("Фрагмент исключения",          OPERATIONS.EXCLUDE, ROLES.IDO),
		                      C20_StandardItem("",                             OPERATIONS.EXCLUDE, ROLES.IDO)])
		self.model_operations.appendRow([item_group,
		                                 C20_StandardItem("")])

		item_group = C20_StandardItem("Параметры обработки")
		item_group.appendRow([C20_StandardItem("Установить назначение",        OPERATIONS.DESTINATION, ROLES.IDO, flag_checked=False),
		                      C20_StandardItem("",                             OPERATIONS.DESTINATION, ROLES.IDO                    )])
		item_group.appendRow([C20_StandardItem("Установить уточнение",         OPERATIONS.DETAIL,      ROLES.IDO, flag_checked=False),
		                      C20_StandardItem("",                             OPERATIONS.DETAIL,      ROLES.IDO                    )])
		item_group.appendRow([C20_StandardItem("Установить объект внутренний", OPERATIONS.OBJECT_INT,  ROLES.IDO, flag_checked=False),
		                      C20_StandardItem("",                             OPERATIONS.OBJECT_INT,  ROLES.IDO                    )])
		item_group.appendRow([C20_StandardItem("Установить объект внешний",    OPERATIONS.OBJECT_EXT,  ROLES.IDO, flag_checked=False),
		                      C20_StandardItem("",                             OPERATIONS.OBJECT_EXT,  ROLES.IDO                    )])
		item_group.appendRow([C20_StandardItem("Установить цветовую метку",    OPERATIONS.COLOR,       ROLES.IDO, flag_checked=False),
		                      C20_StandardItem("",                             OPERATIONS.COLOR,       ROLES.IDO                    )])
		self.model_operations.appendRow([item_group,
		                                 C20_StandardItem("")])

		item_group = C20_StandardItem("Параметры выборки")
		item_group.appendRow([C20_StandardItem("Период обработки",             OPERATIONS.INTERVAL,    ROLES.IDO),
		                      C20_StandardItem("",                             OPERATIONS.INTERVAL,    ROLES.IDO)])
		self.model_operations.appendRow([item_group,
		                                 C20_StandardItem("")])

	def LoadModelOperations(self):
		""" Загрузка данных модели Обработка операций """
		indexes    = self.model_operations.indexesInRowByIdo(OPERATIONS.INCLUDE)
		item_value = self.model_operations.itemFromIndex(indexes[1])
		item_value.setText(self._operations_include or "Не указано")

		indexes    = self.model_operations.indexesInRowByIdo(OPERATIONS.EXCLUDE)
		item_value = self.model_operations.itemFromIndex(indexes[1])
		item_value.setText(self._operations_exclude or "Не указано")

		indexes    = self.model_operations.indexesInRowByIdo(OPERATIONS.DESTINATION)
		item_value = self.model_operations.itemFromIndex(indexes[1])
		item_value.setText(self._operations_destination)

		indexes    = self.model_operations.indexesInRowByIdo(OPERATIONS.DETAIL)
		item_value = self.model_operations.itemFromIndex(indexes[1])
		item_value.setText(self._operations_detail)

		indexes    = self.model_operations.indexesInRowByIdo(OPERATIONS.OBJECT_INT)
		item_value = self.model_operations.itemFromIndex(indexes[1])
		item_value.setText(self._operations_object_int)

		indexes    = self.model_operations.indexesInRowByIdo(OPERATIONS.OBJECT_EXT)
		item_value = self.model_operations.itemFromIndex(indexes[1])
		item_value.setText(self._operations_object_ext)

		indexes    = self.model_operations.indexesInRowByIdo(OPERATIONS.COLOR)
		item_value = self.model_operations.itemFromIndex(indexes[1])
		item_value.setText(self._operations_color)

		indexes    = self.model_operations.indexesInRowByIdo(OPERATIONS.INTERVAL)
		item_value = self.model_operations.itemFromIndex(indexes[1])
		item_value.setText(self.workspace.DmDyToString() if self._operations_interval == INTERVALS.DM else self._operations_interval)

	# Параметры
	def ReadProcessingIdoFromTreeDataOperations(self):
		""" Чтение текущего IDO из дерева данных Обработка операций """
		self._processing_ido = self.tree_data_operations.currentIndex().data(ROLES.IDO)

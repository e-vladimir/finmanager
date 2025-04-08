# ФОРМА ОБРАБОТКА ДАННЫХ: КАТАЛОГ ПРОЕКТА
# 22 мар 2025

import enum


class OBJECTS_TYPE(enum.StrEnum):
	""" Типы объектов """
	NONE       = "Объект не указан"

	OPERATIONS = "Операции"
	LABELS     = "Метки"

	@classmethod
	def _missing_(cls, value): return cls.NONE


class PROCESSING_FIELDS(enum.StrEnum):
	""" Параметры обработки """
	NONE                = "Нет данных"

	DESCRIPTION_INCLUDE = "Описание включает"
	DESCRIPTION_EXCLUDE = "Описание исключает"

	DESTINATION_INCLUDE = "Назначение включает"
	DESTINATION_EXCLUDE = "Назначение исключает"
	DESTINATION_REPLACE = "Заменить назначение"
	DESTINATION_SET     = "Установить назначение"
	DESTINATION_ADD     = "Дополнить назначение"

	LABELS_ADD          = "Добавить метку"
	LABELS_EXCLUDE      = "Метки не содержат"
	LABELS_INCLUDE      = "Метки содержат"
	LABELS_REMOVE       = "Убрать метку"
	LABELS_REPLACE      = "Заменить метку"

	COLOR_SET           = "Установить цветовую метку"

	@classmethod
	def _missing_(cls, value): return cls.NONE

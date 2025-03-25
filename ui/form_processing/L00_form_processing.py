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
	DESCRIPTION_REPLACE = "Заменить фрагмент описания"
	DESCRIPTION_SET     = "Заменить описание"

	LABELS_ADD          = "Добавить метку"
	LABELS_EXCLUDE      = "Метки не содержат"
	LABELS_INCLUDE      = "Поиск по метке"
	LABELS_REMOVE       = "Убрать метку"
	LABELS_REPLACE      = "Заменить на метку"

	@classmethod
	def _missing_(cls, value): return cls.NONE

# ФОРМА ОБРАБОТКА ДАННЫХ: КАТАЛОГ ПРОЕКТА
# 22 мар 2025

import enum


class OBJECTS_TYPE(enum.StrEnum):
	""" Типы объектов """
	NONE       = "Объект не указан"

	OPERATIONS = "Операции"

	@classmethod
	def _missing_(cls, value): return cls.NONE


class PROCESSING_FIELDS(enum.StrEnum):
	""" Параметры обработки """
	NONE                    = "Нет данных"

	OPERATIONS_ALL          = "Все операции"

	SRC_DESCRIPTION_INCLUDE = "Исходное описание включает"
	SRC_DESCRIPTION_EXCLUDE = "Исходное описание исключает"

	DESCRIPTION_ADD         = "Дополнить описание"
	DESCRIPTION_CLEAR       = "Очистить описание"
	DESCRIPTION_EXCLUDE     = "Описание исключает"
	DESCRIPTION_INCLUDE     = "Описание включает"
	DESCRIPTION_REPLACE     = "Заменить описание"
	DESCRIPTION_SET         = "Установить описание"

	DESTINATION_CLEAR       = "Очистить назначение"

	COLOR_SET               = "Установить цветовую метку"

	SKIP_SET                = "Установить пропуск операции"

	@classmethod
	def _missing_(cls, value): return cls.NONE

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
	NONE                = "Нет данных"

	SRC_DESCRIPTION_INCLUDE = "Исходное описание включает"
	SRC_DESCRIPTION_EXCLUDE = "Исходное описание исключает"

	DESCRIPTION_INCLUDE     = "Описание включает"
	DESCRIPTION_EXCLUDE     = "Описание исключает"
	DESCRIPTION_REPLACE     = "Заменить описание"
	DESCRIPTION_SET         = "Установить описание"
	DESCRIPTION_ADD         = "Дополнить описание"

	COLOR_SET               = "Установить цветовую метку"

	SKIP_SET                = "Установить пропуск операции"

	@classmethod
	def _missing_(cls, value): return cls.NONE

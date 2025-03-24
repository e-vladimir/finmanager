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

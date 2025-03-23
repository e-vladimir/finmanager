# ФОРМА ОБРАБОТКА ДАННЫХ: КАТАЛОГ ДАННЫХ
# 22 мар 2025

import enum


class PROCESSING_FIELDS(enum.Enum):
	""" Поля """
	NONE                = enum.auto()

	DESCRIPTION_EQUAL   = enum.auto()
	DESCRIPTION_INCLUDE = enum.auto()

	DESCRIPTION_REPLACE = enum.auto()
	DESCRIPTION_SET     = enum.auto()
	COLOR_SET           = enum.auto()

	@classmethod
	def _missing_(cls, value): return cls.NONE

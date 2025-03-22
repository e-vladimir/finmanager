# ФОРМА ОБРАБОТКА ДАННЫХ: КАТАЛОГ ДАННЫХ
# 22 мар 2025

import enum


class PROCESSING_FIELDS(enum.Enum):
	""" Поля """
	NONE                           = enum.auto()

	FILTER_DESCRIPTION             = enum.auto()

	PROCESSING_REPLACE_DESCRIPTION = enum.auto()
	PROCESSING_SET_DESCRIPTION     = enum.auto()
	PROCESSING_SET_COLOR           = enum.auto()

	@classmethod
	def _missing_(cls, value): return cls.NONE

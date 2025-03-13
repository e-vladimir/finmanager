# КАТАЛОГ ПРОЕКТА: ЦВЕТА

import enum


class COLORS(enum.StrEnum):
	""" Каталог проекта: Цвета """
	BLACK = "Чёрный"
	GRAY  = "Серый"
	GREEN = "Зелёный"
	BLUE  = "Синий"
	RED   = "Красный"

	@classmethod
	def _missing_(cls, value): return cls.BLACK

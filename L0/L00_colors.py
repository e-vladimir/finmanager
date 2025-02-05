# КАТАЛОГ ПРОЕКТА: ЦВЕТА

import enum


class COLORS(enum.StrEnum):
	""" Каталог цветов """
	NONE  = ""
	BLACK = "Чёрный"
	BLUE  = "Синий"
	GRAY  = "Серый"
	GREEN = "Зелёный"
	RED   = "Красный"

	@classmethod
	def _missing_(cls, value): return cls.BLACK

# КАТАЛОГ ПРОЕКТА: ТИПЫ ПРАВИЛ ОБРАБОТКИ ДАННЫХ

import enum


class RULES(enum.StrEnum):
	""" Типы правил обработки данных """
	UNKNOWN              = "Неизвестно"
	REPLACE_TEXT         = "Замена текстового фрагмента"
	DETECT_LABEL_BY_TEXT = "Сопоставление текстовый фрагмент - метка"

	@classmethod
	def _missing_(cls, value):
		return cls.UNKNOWN

# КАТАЛОГ ПРОЕКТА: ТИПЫ ПРАВИЛ ОБРАБОТКИ ДАННЫХ

import enum


class RULES(enum.StrEnum):
	""" Каталог проекта: Типы правил обработки данных """
	NONE                = "Неизвестно"

	REPLACE_DESCRIPTION = "Замена фрагмента описания"
	DETECT_LABELS       = "Определение меток"

	@classmethod
	def _missing_(cls, value): return cls.NONE

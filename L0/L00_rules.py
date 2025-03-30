# КАТАЛОГ ПРОЕКТА: ГРУППЫ ПРАВИЛ ОБРАБОТКИ ДАННЫХ

import enum


class RULES(enum.StrEnum):
	""" Каталог проекта: Группы правил обработки данных """
	NONE                = "Неизвестно"

	REPLACE_DESCRIPTION = "Замена фрагмента описания"

	@classmethod
	def _missing_(cls, value): return cls.NONE

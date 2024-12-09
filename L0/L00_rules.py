# КАТАЛОГ ПРОЕКТА: ПРАВИЛА

import enum


class RULES(enum.StrEnum):
	""" Правила обработки данных """
	NONE                = "Нет данных"
	REPLACE_DESCRIPTION = "Автозамена описания"
	MATCH_DESTINATION   = "Сопоставление назначения"
	DETECT_LABEL        = "Определение меток"

	def _missing_(cls, value) -> 'RULES':
		return cls.NONE

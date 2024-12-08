# КАТАЛОГ ФОРМЫ ОБРАБОТКА ОПЕРАЦИЙ

import enum


class SUBJECTS(enum.StrEnum):
	""" Субъекты обработки """
	DESCRIPTION = "Описание"
	DESTINATION = "Назначение"
	LABELS      = "Метки"


class MODES(enum.StrEnum):
	""" Режимы обработки """
	APPEND   = "Добавление"
	COLLAPSE = "Сокращение"
	EXPAND   = "Расширение"
	REPLACE  = "Замена"


class OPTIONS(enum.StrEnum):
	""" Параметры """
	INCLUDE = "Включает"
	EXCLUDE = "Исключает"
	OUTPUT  = "Результат"
	MODE    = "Режим"

# КАТАЛОГ ФОРМЫ ОБРАБОТКА ОПЕРАЦИЙ

import enum


class MODES(enum.StrEnum):
	""" Каталог формы Обработка операций: Режимы обработки """
	APPEND  = "Добавление"
	REPLACE = "Замена"
	EXPAND  = "Расширение"


class TOOLS(enum.StrEnum):
	""" Каталог формы Обработка операций: IDO параметров """
	GROUP_DESCRIPTION   = "Описание"
	GROUP_DESTINATION   = "Назначение"
	GROUP_LABELS        = "Метки"

	DESCRIPTION_INCLUDE = "Описание: Включает"
	DESCRIPTION_APPLIES = "Описание: Применяется"

	DESTINATION_INCLUDE = "Назначение: Включает"
	DESTINATION_APPLIES = "Назначение: Применяется"

	LABELS_INCLUDE      = "Метки: Включает"
	LABELS_MODE         = "Метки: Режим обработки"
	LABELS_APPLIES      = "Метки: Применяется"

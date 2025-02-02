# ФОРМА АНАЛИТИКА: КАТАЛОГОВ КОДОВ

import enum


class ANALYTICS(enum.StrEnum):
	INCLUDE     = "Признаки+"
	EXCLUDE     = "Признаки-"

	DESTINATION = "Назначение"
	OBJECT_INT  = "Объект внутренний"
	OBJECT_EXT  = "Объект внешний"
	ITEM        = "Элемент аналитики"

# КАТАЛОГ ПРОЕКТА: КОНТЕЙНЕРЫ

import enum


class CONTAINERS(enum.StrEnum):
	""" Контейнеры """
	DISK   = "local"
	MEMORY = "ram"
	CACHE  = "cache"

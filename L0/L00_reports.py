# КАТАЛОГ ПРОЕКТА: ОТЧЁТНОСТЬ

import enum


class REPORTS(enum.StrEnum):
	""" Виды отчётов """
	DM              = "Отчёт за месяц"
	BALANCES_ALL_DM = "Отчёт по остаткам за все периоды"

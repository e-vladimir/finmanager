# ПАЛИТРА ИНСТРУМЕТОВ ДЛЯ РАБОТЫ С ДАТОЙ-ВРЕМЕНЕМ
# 2024-05-02

import datetime

from   L10_math import Sign


DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# ТЕКУЩИЕ ДАННЫЕ
def CurrentDTime() -> datetime.datetime:
	""" Текущая дата-время """
	return datetime.datetime.now()


def CurrentDy() -> int:
	""" Текущий год 0..9999 """
	return CurrentDTime().year


def CurrentDm(flag_start_from_0: bool = False) -> int:
	""" Текущий месяц в виде 1..12|0..11 """
	current_month : int = CurrentDTime().month

	if flag_start_from_0: return current_month - 1

	return current_month


def CurrentDd() -> int:
	""" Текущее число месяца 1..31 """
	return CurrentDTime().day


# СМЕЩЕНИЕ ДАТ
def CalcDyDmByShiftDm(year: int, month: int, shift: int) -> tuple[int, int]:
	""" Вычисление года и месяца при смещении по месяцу """
	_year  : int = year
	_month : int = month - 1
	_month      += shift

	if _month < 0: _month -= 12

	_year  += Sign(_month) * (abs(_month) // 12)
	_month  = _month  % 12
	_month += 1

	return _year, _month


# ПРЕОБРАЗОВАНИЕ
def DTimeToUTime(dtime: datetime.datetime) -> int:
	""" Преобразование datetime в unix-формат """
	return int(dtime.timestamp())


def UTimeToDTime(utime: int) -> datetime.datetime:
	""" Преобразование unix формата в datetime """
	return datetime.datetime.fromtimestamp(utime)


# ФОРМИРОВАНИЕ ДАННЫХ
def DyDmDdToUTime(year: int, month: int = None, day: int = None, flag_end_day: bool = False) -> int:
	""" Преобразование ГГГГ.ММ.ДД в unix-формат. Примечание: месяц 1..12, число 1..31 """
	dy     : int = year
	dm     : int = 1
	dd     : int = 1

	if month is not None:
		if month in range(1, 13): dm = month

	if day is not None:
		if day in range(1, 32)  : dd = day

	max_dd : int = DAYS_IN_MONTH[dm - 1]
	max_dd      += 1 if (dy % 4 == 0) else 0

	dd           = min(dd, max_dd)

	hh     : int = 0
	hm     : int = 0
	hs     : int = 0
	hs6    : int = 0

	if flag_end_day:
		hh = 23
		hm = 59
		hs = 59

	dtime = datetime.datetime(year=dy, month=dm, day=dd, hour=hh, minute=hm, second=hs, microsecond=hs6)

	return DTimeToUTime(dtime)

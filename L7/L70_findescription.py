# ФИНСОСТАВ: МЕХАНИКА УПРАВЛЕНИЯ

from L60_findescription import C60_RecordFindescription, C60_Findescription


class C70_RecordFindescription(C60_RecordFindescription):
	""" Запись финсостава: Механика управления """

	pass


class C70_Findescription(C60_Findescription):
	""" Финсостав: Механика управления """

	# Проверки данных
	def ValidateName(self, name: str) -> bool:
		""" Валидация значения финсостава """
		if not name.strip(): return False

		return True

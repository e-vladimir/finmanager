# ФИНСТРУКТУРА: МЕХАНИКА УПРАВЛЕНИЯ

from L60_finstruct import C60_RecordFinstruct, C60_Finstruct


class C70_RecordFinstruct(C60_RecordFinstruct):
	""" Запись финструктуры: Механика управления """
	pass


class C70_Finstruct(C60_Finstruct):
	""" Финструктура: Механика управления """

	# Проверки данных
	def ValidateName(self, name: str) -> bool:
		""" Валидация наименования записи финструктуры """
		if not name.strip(): return False

		return True

# ФОРМА СБРОС ДАННЫХ: МЕХАНИКА УПРАВЛЕНИЯ

from L60_form_reset import C60_FormReset


class C70_FormReset(C60_FormReset):
	""" Форма Сброс данных: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка окна """
		self.setWindowTitle("Сброс данных")

	# Дерево объектов
	def SetupExpandTreObjects(self):
		""" Настройка раскрытия элементов дерева объектов """
		self.tre_objects.expandAll()

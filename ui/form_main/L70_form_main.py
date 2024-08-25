# ФОРМА ОСНОВНАЯ: МЕХАНИКА УПРАВЛЕНИЯ

from G10_datetime  import CurrentDy

from L00_months    import MONTHS_SHORT
from L60_form_main import C60_FormMain


class C70_FormMain(C60_FormMain):
	""" Форма основная: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка окна """
		self.setWindowTitle(f"Финменеджер.19 - {self.workspace.DmDyToString()}")

	# Панель финпериода
	def FillCbboxDy(self):
		""" Заполнение списка годов """
		self.cbbox_dy.clear()
		self.cbbox_dy.addItems([str(dy) for dy in range(CurrentDy() - 5, CurrentDy() + 1)])

	def FillCbboxDm(self):
		""" Заполнение списка месяцев """
		self.cbbox_dm.clear()
		self.cbbox_dm.addItems(MONTHS_SHORT[1:])

	def ShowDy(self):
		""" Отображение года """
		self.cbbox_dy.setCurrentText(f"{self.workspace.Dy()}")

	def ShowDm(self):
		""" Отображение месяца """
		self.cbbox_dm.setCurrentText(f"{MONTHS_SHORT[self.workspace.Dm()]}")


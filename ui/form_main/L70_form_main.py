# ФОРМА ОСНОВНАЯ: МЕХАНИКА УПРАВЛЕНИЯ

from L60_form_main import C60_FormMain


class C70_FormMain(C60_FormMain):
	""" Форма Основная: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка окна """
		self.setWindowTitle(f"Финорганайзер.20 - {self.workspace.DmDyToString()}")

	# Панель рабочего периода
	def AdjustBtnDyDm_Text(self):
		""" Кнопка Рабочий период """
		self.btn_dmdy.setText(self.workspace.DmDyToString())

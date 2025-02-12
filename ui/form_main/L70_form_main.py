# ФОРМА ОСНОВНАЯ: МЕХАНИКА УПРАВЛЕНИЯ
# 12 фев 2025
from G10_datetime import CalcDyDmByShiftDm
from L00_months    import MONTHS_SHORT
from L60_form_main import C60_FormMain


class C70_FormMain(C60_FormMain):
	""" Форма Основная: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка формы """
		self.setWindowTitle(f"Финорганайзер.22 - {self.Workspace.DmDyToString()}")

	# Панель рабочий период
	def ShowDyDm(self):
		""" Отображение параметров рабочего периода """
		dy, dm = self.Workspace.DyDm()
		self.label_dm_dy.setText(f"{MONTHS_SHORT[dm].upper()}\n{dy}")

		dy, dm = CalcDyDmByShiftDm(dy, dm, -1)
		self.label_dm_dy_prev.setText(f"{MONTHS_SHORT[dm]}\n{dy}")

		dy, dm = CalcDyDmByShiftDm(dy, dm,  2)
		self.label_dm_dy_next.setText(f"{MONTHS_SHORT[dm]}\n{dy}")

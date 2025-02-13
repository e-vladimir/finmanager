# ФОРМА ОСНОВНАЯ: МЕХАНИКА УПРАВЛЕНИЯ
# 12 фев 2025

from G10_datetime  import CalcDyDmByShiftDm
from G11_convertor_data import AmountToString

from L00_months    import MONTHS_SHORT
from L60_form_main import C60_FormMain


class C70_FormMain(C60_FormMain):
	""" Форма Основная: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка формы """
		self.setWindowTitle(f"Финорганайзер.22 - {self.Workspace.DmDyToString()}")

	# Панель рабочий период
	def ShowWorkspace(self):
		""" Отображение данных рабочего периода """
		dy, dm = self.Workspace.DyDm()
		self.label_dm_dy.setText(f"{MONTHS_SHORT[dm].upper()}\n{dy}")

		dy, dm = CalcDyDmByShiftDm(dy, dm, -1)
		self.label_dm_dy_prev.setText(f"{MONTHS_SHORT[dm]}\n{dy}")

		dy, dm = CalcDyDmByShiftDm(dy, dm,  2)
		self.label_dm_dy_next.setText(f"{MONTHS_SHORT[dm]}\n{dy}")

	# Панель Счета
	def ShowAccounts(self):
		""" Отображение данных Счета """
		self.label_amout.setText(AmountToString(0, flag_point=False, flag_sign=True))

	# Панель Операции
	def ShowOperations(self):
		""" Отображение данных Операции """
		amount_income  : int = 0
		amount_outcome : int = 0
		amount_delta   : int = amount_income - amount_outcome

		self.label_delta.setText(AmountToString(amount_delta, flag_sign=True))
		self.label_subdelta.setText(f"{AmountToString(amount_income, flag_sign=True)}  |  {AmountToString(amount_outcome, flag_sign=True)}")

	# Панель Копия данных
	def ShowBackup(self):
		""" Отображение данных Копия данных """
		backup_dy_dm_dd : str = "Нет копии"
		backup_th_tm    : str = "--:--"
		self.label_backup_dd_dm_dy.setText(backup_dy_dm_dd)
		self.label_backup_th_tm.setText(backup_th_tm)


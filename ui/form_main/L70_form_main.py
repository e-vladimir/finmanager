# ФОРМА ОСНОВНАЯ: МЕХАНИКА УПРАВЛЕНИЯ
# 12 фев 2025
from G10_convertor_format import UTimeToDTime
from G10_datetime       import CalcDyDmByShiftDm
from G11_convertor_data import AmountToString

from L00_months         import MONTHS_SHORT
from L60_form_main      import C60_FormMain


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
		self.LabelDmDy.setText(f"{MONTHS_SHORT[dm].upper()}\n{dy}")

		dy, dm = CalcDyDmByShiftDm(dy, dm, -1)
		self.LabelPrevDmDy.setText(f"{MONTHS_SHORT[dm]}\n{dy}")

		dy, dm = CalcDyDmByShiftDm(dy, dm,  2)
		self.LabelNextDmDy.setText(f"{MONTHS_SHORT[dm]}\n{dy}")

	# Панель Счета
	def ShowAccounts(self):
		""" Отображение данных Счета """
		dy, dm = self.Workspace.DyDm()

		self.LabelInitialBalance.setText(AmountToString(self.Accounts.CalcInitialBalance(dy, dm),
		                                                flag_point=False,
		                                                flag_sign =False))

	# Панель Операции
	def ShowOperations(self):
		""" Отображение данных Операции """
		dy,dm                        = self.Workspace.DyDm()
		amounts        : list[float] = self.Operations.Amounts(dy, dm)
		amount_income  : int         = sum(filter(lambda amount: amount > 0, amounts))
		amount_outcome : int         = sum(filter(lambda amount: amount < 0, amounts))
		amount_delta   : int         = amount_income + amount_outcome

		self.LabelDelta.setText(AmountToString(amount_delta, flag_sign=True))
		self.LabelSubdelta.setText(f"{AmountToString(amount_income, flag_sign=True)}  |  {AmountToString(amount_outcome, flag_sign=True)}")

	# Панель Копия данных
	def ShowBackup(self):
		""" Отображение данных Копия данных """
		backup_dy_dm_dd : str = "Нет копии"
		backup_th_tm    : str = "--:--"
		self.LabelBackupDdDmDy.setText(backup_dy_dm_dd)
		self.LabelBackupThTm.setText(backup_th_tm)

		if not self.Application.backup_names: return

		backup_name : str = sorted(self.Application.backup_names)[-1].split('.')[0]
		if not backup_name.isnumeric(): return

		dtime = UTimeToDTime(int(backup_name))

		backup_dy_dm_dd : str = f"{dtime.day:02d} {MONTHS_SHORT[dtime.month]} {dtime.year}"
		backup_th_tm    : str = f"{dtime.hour:02d}:{dtime.minute:02d}"
		self.LabelBackupDdDmDy.setText(backup_dy_dm_dd)
		self.LabelBackupThTm.setText(backup_th_tm)

	# Панель Обзор месяца
	def ShowMonthView(self):
		""" Отображение обзора месяца """
		dy, dm = self.Workspace.DyDm()

		self.DiaDmViewer.InitDaysFromDyDm(dy, dm)
		self.update()

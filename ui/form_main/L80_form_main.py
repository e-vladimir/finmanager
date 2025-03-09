# ФОРМА ОСНОВНАЯ: ЛОГИКА ДАННЫХ
# 12 фев 2025

from L00_months    import MONTHS_SHORT
from L20_PySide6   import RequestText
from L70_form_main import C70_FormMain


class C80_FormMain(C70_FormMain):
	""" Форма Основная: Логика данных """

	# Рабочий период
	def EditDyDm(self):
		""" Редактирование рабочего периода """
		text  : str | None = RequestText("Рабочий период", "Формат: месяц год", self.Workspace.DmDyToString())
		if not text                  : return

		items : list[str]  = (text.lower()
		                          .strip()
		                          .split(' '))

		if not len(items) == 2       : return

		raw_dm, raw_dy     = items
		if not raw_dm in MONTHS_SHORT: return
		if not raw_dy.isdigit()      : return

		self.Workspace.dm  = MONTHS_SHORT.index(raw_dm)
		self.Workspace.dy  = int(raw_dy)

		self.on_DyDm_Changed()

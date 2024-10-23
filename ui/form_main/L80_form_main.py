# ФОРМА ОСНОВНАЯ: ЛОГИКА ДАННЫХ

from L00_months    import MONTHS
from L20_PySide6   import RequestText
from L70_form_main import C70_FormMain


class C80_FormMain(C70_FormMain):
	""" Форма Основная: Логика данных """

	# Рабочий период
	def SetDyDm(self):
		""" Установка рабочего периода """
		dydm_raw : str | None = RequestText("Рабочий период", "Формат: МЕС ГОД", self.workspace.DmDyToString())
		if dydm_raw is None: return

		try   :
			dm_raw, dy_raw = dydm_raw.lower().split(' ')

			dy : int       = int(dy_raw)
			dm : MONTHS    = MONTHS.FindByNameS(dm_raw)
		except: return

		self.workspace.DyDm(dy, dm.code)

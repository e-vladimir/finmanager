# ФОРМА ОСНОВНАЯ: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtGui         import QIcon

from G10_convertor_format import AnyToStrings
from L00_months            import MONTHS_SHORT

from L60_form_main         import C60_FormMain


class C70_FormMain(C60_FormMain):
	""" Форма основная: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка окна """
		self.setWindowTitle(f"Финменеджер 18.17 - {self.workspace.DmDyToString()}")

	# Кнопки смены финпериода
	def SetupButtons(self):
		""" Настройка кнопок """
		icon_prev = QIcon("./ui/icons/arrow_left.svg")
		icon_next = QIcon("./ui/icons/arrow_right.svg")

		self.btn_dm_prev.setIcon(icon_prev)
		self.btn_dm_next.setIcon(icon_next)

	# Поля финпериода
	def FillCbbDy(self):
		""" Заполнение списка годов """
		self._flag_loading = True

		self.cbbox_dy.clear()
		self.cbbox_dy.addItems(AnyToStrings(self.workspace.Dys()))

		self._flag_loading = False

	def ShowDyFromWorkspace(self):
		""" Отображение года финпериода """
		self._flag_loading = True

		self.cbbox_dy.setCurrentText(f"{self.workspace.Dy()}")

		self._flag_loading = False

	def ReadDyToWorkspace(self):
		""" Чтение выбранного года """
		if self._flag_loading: return

		self.workspace.Dy(int(self.cbbox_dy.currentText()))

	def FillCbbDm(self):
		""" Заполнение списка месяцев """
		self._flag_loading = True

		self.cbbox_dm.clear()
		self.cbbox_dm.addItems(MONTHS_SHORT[1:])

		self._flag_loading = False

	def ShowDmFromWorkspace(self):
		""" Отображение месяца финпериода """
		self._flag_loading = True

		self.cbbox_dm.setCurrentIndex(self.workspace.Dm() - 1)

		self._flag_loading = False

	def ReadDmToWorkspace(self):
		""" Чтение выбранного месяца """
		if self._flag_loading: return

		self.workspace.Dm(self.cbbox_dm.currentIndex() + 1)

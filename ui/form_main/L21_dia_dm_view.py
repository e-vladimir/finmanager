# КОМПОНЕНТ ОБЗОР МЕСЯЦА
# 12 фев 2025

from collections           import defaultdict

from PySide6.QtGui         import QColor, QFont, QPainter, QPen, Qt

from G10_datetime          import CountDdInDyDm
from L20_PySide6           import C20_DiaFrame
from L20_finmanager_struct import T20_Day
from L90_operations        import C90_Operations
from L90_workspace import C90_Workspace


class C21_DiaDmView(C20_DiaFrame):
	""" Компонент Обзор месяца """

	# Модель данных
	_days     : defaultdict[int, T20_Day] = defaultdict(T20_Day)

	_margin_l : int = 50
	_margin_r : int = 50
	_margin_t : int = 10
	_margin_b : int = 10

	_margin_c : int = 10

	Operations           = C90_Operations()
	Workspace            = C90_Workspace()

	# Модель событий
	pass

	# Механика данных
	pass

	# Механика управления
	def DrawBackground(self, painter: QPainter):
		""" Отрисовка фона """
		painter.setPen(QColor(225, 225, 225))
		painter.setBrush(QColor(250, 250, 250))
		painter.drawRect(0, 0, self.width() - 1, self.height() - 1)

	def DrawGrid(self, painter: QPainter):
		""" Отрисовка сетки """
		x0 : int = 10
		x1 : int = self.width()  - 1 - 10
		h  : int = (self.height() - self._margin_t - self._margin_b) // 2
		yC : int = self.height() // 2

		y  : int = yC
		painter.setPen(QColor(205, 205, 205))
		painter.drawLine(x0, y, x1, y)

		for shift in [h * 0.25, h * 0.50, h * 0.75]:
			y  : int = int(yC + shift)
			painter.setPen(QPen(QColor(205, 205, 205), 1, Qt.PenStyle.DashLine))
			painter.drawLine(x0, y, x1, y)

			y  : int = int(yC - shift)
			painter.setPen(QPen(QColor(205, 205, 205), 1, Qt.PenStyle.DashLine))
			painter.drawLine(x0, y, x1, y)

	def DrawLabels(self, painter: QPainter):
		""" Отрисовка меток """
		margin : int       = 50
		w      : int       = 24
		h      : int       = 12
		x0     : int       = margin
		x1     : int       = self.width() - 1 - margin
		y      : int       = self.height() // 2

		step_x : float     = (x1 - x0) / (CountDdInDyDm(self.Workspace.dy, self.Workspace.dm) - 1)

		font_labels : QFont = painter.font()
		font_labels.setFamily("Sans")
		font_labels.setPixelSize(9)

		painter.setFont(font_labels)

		for idx_day in range(CountDdInDyDm(self.Workspace.dy, self.Workspace.dm)):
			day = self._days[idx_day + 1]
			x : int = x0 + int(step_x * idx_day)

			if day.is_weekend:
				painter.setPen(QColor(155, 155, 155))
				painter.setBrush(QColor(155, 155, 155))
			else:
				painter.setPen(QColor(205, 205, 205))
				painter.setBrush(QColor(255, 255, 255))

			painter.drawRect(x - w // 2, y - h // 2, w, h)

			if day.is_weekend:
				painter.setPen(QColor(255, 255, 255))
			else:
				painter.setPen(QColor(105, 105, 105))

			painter.drawText(x - 5, y + 3, f"{idx_day + 1:02d}")

	def DrawAmounts(self, painter: QPainter):
		""" Отрисовка объёма """
		income_max   : int   = int(max([day.amount_income  for day in self._days.values()]))
		outcome_max  : int   = int(min([day.amount_outcome for day in self._days.values()]))

		w            : int   = 24
		x0           : int   = self._margin_l
		x1           : int   = self.width()   - 1 - self._margin_r
		y            : int   = self.height() // 2

		step_x       : float = (x1 - x0) / (len(self._days) - 1)
		step_income  : float = (y - self._margin_t - self._margin_c) / (income_max  or 1)
		step_outcome : float = (y - self._margin_b - self._margin_c) / (outcome_max or 1)

		for idx_day in range(CountDdInDyDm(self.Workspace.dy, self.Workspace.dm)):
			day             = self._days[idx_day + 1]
			x         : int = x0 + int(step_x * idx_day)
			h_income  : int = int(day.amount_income  * step_income)
			h_outcome : int = int(day.amount_outcome * step_outcome)

			painter.setPen(QColor(235, 205, 205))
			painter.setBrush(QColor(255, 225, 225))
			painter.drawRect(x - w // 2, y + self._margin_c, w,  h_outcome)

			painter.setPen(QColor(205, 235, 205))
			painter.setBrush(QColor(225, 255, 225))
			painter.drawRect(x - w // 2, y - self._margin_c, w, -h_income)

	def DrawAmountsDynamic(self, painter: QPainter):
		""" Отрисовка динамики объёма """
		x0           : int   = self._margin_l
		x1           : int   = self.width() - 1 - self._margin_r
		y            : int   = self.height() // 2
		step_x : float     = (x1 - x0) / (CountDdInDyDm(self.Workspace.dy, self.Workspace.dm) - 1)
		income_sum   : int   = int(sum([day.amount_income  for day in self._days.values()]))
		income_val   : int   = 0
		outcome_sum  : int   = int(sum([day.amount_outcome for day in self._days.values()]))
		outcome_val  : int   = 0
		step_income  : float = (y - self._margin_t - self._margin_c) / (income_sum  or 1)
		step_outcome : float = (y - self._margin_b - self._margin_c) / (outcome_sum or 1)

		x_prev         : int = x0
		y_income_prev  : int = y - self._margin_c
		y_outcome_prev : int = y + self._margin_c

		for idx_day in range(CountDdInDyDm(self.Workspace.dy, self.Workspace.dm)):
			day = self._days[idx_day + 1]
			x         : int = x0 + int(step_x * idx_day)
			income_val     += day.amount_income
			outcome_val    += day.amount_outcome

			y_income  : int = y - int(income_val  * step_income)  - self._margin_c
			y_outcome : int = y + int(outcome_val * step_outcome) + self._margin_c

			if idx_day > 0:
				painter.setPen(QPen(QColor(205, 175, 175), 3))
				painter.drawLine(x_prev, y_outcome_prev, x, y_outcome)

				painter.setPen(QPen(QColor(175, 205, 175), 3))
				painter.drawLine(x_prev, y_income_prev, x, y_income)

			x_prev = x
			y_income_prev = y_income
			y_outcome_prev = y_outcome

	# Логика данных
	pass

	# Логика управления
	def paintEvent(self, event):
		""" Отрисовка """
		painter = QPainter(self)
		painter.setRenderHint(QPainter.RenderHint.Antialiasing)
		painter.translate(0.5, 0.5)

		self.DrawBackground(painter)
		self.DrawBorder(painter)

		self.DrawGrid(painter)
		self.DrawLabels(painter)

		self.DrawAmounts(painter)
		self.DrawAmountsDynamic(painter)

		painter.resetTransform()

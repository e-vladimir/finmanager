# КОМПОНЕНТЫ ФОРМЫ АНАЛИТИКИ

from PySide6.QtCore     import QRect
from PySide6.QtGui      import QColor, QFont, QPainter, Qt

from G11_convertor_data import AmountToString
from L20_PySide6        import C20_DiaFrame
from L20_data_struct    import T20_StatisticItem


class C20_DiaDynamic(C20_DiaFrame):
	""" Диаграмма динамики """

	def Init_00(self):
		super().Init_00()

		self._margin_l   : int       = 50
		self._margin_r   : int       = 50
		self._margin_t   : int       = 20
		self._margin_b   : int       = 50

		self._statistics : list[T20_StatisticItem] = []

	def DrawCenter(self, painter: QPainter):
		""" Отрисовка центра """
		painter.setPen(QColor(60, 60, 60))

		y : int = int(self._margin_t + (self.height() - 1 - self._margin_b - self._margin_t) / 2)

		painter.drawLine(10, y, self.width() - 1 - 10, y)

	def DrawBorder(self, painter: QPainter):
		""" Отрисовка границ """
		painter.setPen(QColor(180, 180, 180))
		painter.setBrush(QColor(255, 255, 255))
		painter.drawRect(0, 0, self.width() - 1, self.height() - 1)

	def DrawIncome(self, painter: QPainter):
		""" Отрисовка поступлений """
		amounts      : list[int] = [item.amount_income for item in self._statistics]
		if not amounts   : return

		amount_max   : int       = max(amounts)
		if not amount_max: return

		amount_scale : float     = ((self.height() - 1 - self._margin_b - 5 - self._margin_t - 5) / 2) / amount_max

		x_step       : float     = (self.width() - 1 - self._margin_l - self._margin_r) / 11
		y            : int       = int(self._margin_t + (self.height() - 1 - self._margin_b - self._margin_t) / 2)

		painter.setFont(QFont("Noto Sans Mono", 8))

		for idx, amount in enumerate(amounts):
			if not amount: continue
			x : int = int(self._margin_l + x_step * idx)
			h : int = int(amount_scale * amount)

			painter.setPen(QColor(50, 150, 50))
			painter.setBrush(QColor(220, 250, 220))

			painter.drawRect(x - 12, y, 24, -h)

			painter.setPen(QColor(30, 30, 30))
			painter.drawText(QRect(x - 35, self._margin_t - 18, 70, 16), Qt.AlignmentFlag.AlignCenter, AmountToString(amount, flag_sign=True))

	def DrawOutcome(self, painter: QPainter):
		""" Отрисовка списаний """
		amounts      : list[int] = [abs(item.amount_outcome) for item in self._statistics]
		if not amounts   : return

		amount_max   : int       = max(amounts)
		if not amount_max: return

		amount_scale : float     = ((self.height() - 1 - self._margin_b - 5 - self._margin_t - 5) / 2) / amount_max

		x_step       : float     = (self.width() - 1 - self._margin_l - self._margin_r) / 11
		y            : int       = int(self._margin_t + (self.height() - 1 - self._margin_b - self._margin_t) / 2)

		painter.setFont(QFont("Noto Sans Mono", 8))

		for idx, amount in enumerate(amounts):
			if not amount: continue
			x : int = int(self._margin_l + x_step * idx)
			h : int = int(amount_scale * amount)

			painter.setPen(QColor(150, 50, 50))
			painter.setBrush(QColor(250, 220, 220))

			painter.drawRect(x - 12, y, 24, h)

			painter.setPen(QColor(30, 30, 30))
			painter.drawText(QRect(x - 35, self.height() - 1 - self._margin_b, 70, 16), Qt.AlignmentFlag.AlignCenter, AmountToString(-amount, flag_sign=True))

	def DrawGrid(self, painter: QPainter):
		""" Отрисовка сетки """
		painter.setPen(QColor(200, 200, 200))
		x_step : float = (self.width() - 1 - self._margin_l - self._margin_r) / 11

		for idx in range(12):
			x : int = int(self._margin_l + x_step * idx)

			painter.drawLine(x, self._margin_t, x, self.height() - 1 - self._margin_b)

	def DrawLabels(self, painter: QPainter):
		""" Отрисовка меток """
		x_step : float     = (self.width() - 1 - self._margin_l - self._margin_r) / 11
		labels : list[str] = [item.caption for item in self._statistics]

		painter.setPen(QColor(150, 150, 150))
		painter.setFont(QFont("Noto Sans Mono", 8))

		for idx, label in enumerate(labels):
			x : int = int(self._margin_l + x_step * idx)

			painter.drawText(QRect(x - 35 + 2, self.height() - 1 - 30, 70, 24), Qt.AlignmentFlag.AlignCenter, label)

	def DrawAvg(self, painter: QPainter):
		""" Отрисовка средних линий """
		available_h   : int       = (self.height() - 1 - self._margin_t - self._margin_b) // 2
		center        : int       = int(self._margin_t + available_h)

		y             : int       = int(center - available_h * 0.50)
		painter.setPen(QColor(50, 150, 50, 127))
		painter.drawLine(10, y, self.width() - 1 - 10, y)

		y             : int       = int(center - available_h * 0.80)
		painter.setPen(QColor(50, 150, 50, 64))
		painter.drawLine(10, y, self.width() - 1 - 10, y)

		y             : int       = int(center + available_h * 0.50)
		painter.setPen(QColor(150, 50, 50, 127))
		painter.drawLine(10, y, self.width() - 1 - 10, y)

		y             : int       = int(center + available_h * 0.80)
		painter.setPen(QColor(150, 50, 50, 64))
		painter.drawLine(10, y, self.width() - 1 - 10, y)

	def paintEvent(self, event):
		painter = QPainter(self)

		self.DrawBackground(painter)
		self.DrawBorder(painter)

		self.DrawGrid(painter)
		self.DrawIncome(painter)
		self.DrawOutcome(painter)
		self.DrawCenter(painter)
		self.DrawLabels(painter)
		self.DrawAvg(painter)

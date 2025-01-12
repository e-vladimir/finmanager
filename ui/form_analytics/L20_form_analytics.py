# КОМПОНЕНТЫ ФОРМЫ АНАЛИТИКИ

from PySide6.QtCore     import QRect
from PySide6.QtGui      import QColor, QFont, QPainter, Qt

from G10_math_linear    import Sign
from G11_convertor_data import AmountToString

from L20_PySide6        import C20_DiaFrame


class C20_DiaDynamic(C20_DiaFrame):
	""" Диаграмма динамики """

	def Init_00(self):
		super().Init_00()

		self._margin_l   : int       = 50
		self._margin_r   : int       = 120
		self._margin_t   : int       = 40
		self._margin_b   : int       = 40

		self._title      : str       = "Заголовок"

		self._labels     : list[str] = ["мес\n0000"] * 12
		self._amounts    : list[int] = [0] * 12

		self._amount_avg : int       = 0

	def CalcAmountAvg(self):
		""" Расчёт среднее значение суммы """
		amount_max   : int = max(self._amounts)
		amount_min   : int = min(self._amounts)
		amount_delta : int = int(amount_max - amount_min)

		self._amount_avg = amount_min + Sign(amount_max) * amount_delta // 2

	def DrawTitle(self, painter: QPainter):
		""" Отрисовка заголовка """
		painter.setFont(QFont("Noto Sans Mono", 10, QFont.Weight.Bold))
		painter.setPen(QColor(30, 30, 30))

		painter.drawText(5, 16, self._title.upper())

	def DrawLabels(self, painter: QPainter):
		""" Отрисовка меток """
		step   : float = (self.width() - 1 - self._margin_l - self._margin_r) / 11

		painter.setPen(QColor(220, 220, 220))
		for idx in range(12):
			x : int = int(self._margin_l + idx * step) - 1
			painter.drawLine(x, self._margin_t, x, self.height() - self._margin_b)

		painter.setFont(QFont("Noto Sans Mono", 8))
		painter.setPen(QColor(30, 30, 30))
		for idx, label in enumerate(self._labels):
			x : int = int(self._margin_l + idx * step)
			painter.drawText(QRect(x - 25, self.height() - self._margin_b + 5, 50, 25), Qt.AlignmentFlag.AlignCenter, label)

	def DrawAmounts(self, painter: QPainter):
		""" Отрисовка значений """
		y            : int   = (self.height() - 1) // 2
		step         : float = (self.width() - 1 - self._margin_l - self._margin_r) / 11

		amount_max   : int   = max(list(map(abs, self._amounts)))
		amount_scale : float = 0 if not amount_max else (self.height() - 1 - self._margin_l - self._margin_b) / amount_max

		color_pen_r          = QColor(150, 100, 100)
		color_pen_g          = QColor(100, 150, 100)

		color_brush_r        = QColor(250, 200, 200)
		color_brush_g        = QColor(200, 250, 200)

		painter.setFont(QFont("Noto Sans Mono", 6))

		for idx, amount in enumerate(self._amounts):
			x              : int = int(self._margin_l + idx * step) - 1

			amount_delta   : int = self._amount_avg - amount
			amount_percent : int = 0 if not self._amount_avg else -1 * Sign(self._amount_avg) * Sign(amount_delta) * int(abs(amount_delta) / abs(self._amount_avg) * 100)

			painter.setPen(color_pen_r if self._amount_avg < 0 else color_pen_g)
			painter.setBrush(color_brush_r if self._amount_avg < 0 else color_brush_g)

			painter.drawRect(x - 12, y, 24, amount_delta * amount_scale)

			painter.setPen(color_pen_r if self._amount_avg < 0 else color_pen_g)
			painter.setBrush(color_brush_r if self._amount_avg < 0 else color_brush_g)
			painter.drawRect(x - 25, y - 8, 50, 16)
			painter.setPen(QColor(30, 30, 30))
			painter.drawText(QRect(x - 25, y - 8, 50, 16), Qt.AlignmentFlag.AlignCenter, AmountToString(amount, flag_sign=True))

			painter.drawText(QRect(x - 23, self._margin_t - 20, 50, 16), Qt.AlignmentFlag.AlignCenter, f"{AmountToString(amount_percent, flag_sign=True)}%")

	def DrawAvg(self, painter: QPainter):
		""" Отрисовка среднего """
		y : int = (self.height() - 1) // 2
		painter.setPen(QColor(30, 30, 30))
		painter.drawLine(20, y, self.width() - 1 - 20, y)

		painter.setBrush(QColor(255, 255, 255))
		painter.drawRect(QRect(self.width() - 60, y - 8, 50, 16))

		painter.setFont(QFont("Noto Sans Mono", 6))
		painter.drawText(QRect(self.width() - 60, y - 8, 50, 16), Qt.AlignmentFlag.AlignCenter, AmountToString(self._amount_avg, flag_sign=True))

	def DrawBorder(self, painter: QPainter):
		""" Отрисовка границ """
		painter.setPen(QColor(180, 180, 180))
		painter.setBrush(QColor(255, 255, 255))
		painter.drawRect(0, 0, self.width() - 1, self.height() - 1)

	def paintEvent(self, event):
		painter = QPainter(self)

		self.CalcAmountAvg()

		self.DrawBackground(painter)
		self.DrawBorder(painter)

		self.DrawTitle(painter)
		self.DrawLabels(painter)
		self.DrawAvg(painter)
		self.DrawAmounts(painter)

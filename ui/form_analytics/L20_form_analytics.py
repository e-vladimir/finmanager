# КОМПОНЕНТЫ ФОРМЫ АНАЛИТИКИ

from PySide6.QtCore     import QRect
from PySide6.QtGui      import QColor, QFont, QPainter, Qt

from G11_convertor_data import AmountToString
from L20_PySide6        import C20_DiaFrame


class C20_DiaDynamic(C20_DiaFrame):
	""" Диаграмма динамики """

	def Init_00(self):
		super().Init_00()

		self._margin_l : int = 50
		self._margin_r : int = 120
		self._margin_t : int = 40
		self._margin_b : int = 40

		self._title  : str       = "Заголовок"

		self._labels : list[str] = ["мес\n0000"] * 12
		self._amounts: list[int] = [0] * 12

	def DrawTitle(self, painter: QPainter):
		""" Отрисовка заголовка """
		painter.setFont(QFont("Noto Sans Mono", 10, QFont.Weight.Bold))
		painter.setPen(QColor(30, 30, 30))

		painter.drawText(5, 16, self._title.upper())

	def DrawLabels(self, painter: QPainter):
		""" Отрисовка меток """
		step   : float = (self.width() - 1 - self._margin_l - self._margin_r) / 11

		painter.setPen(QColor(220, 220, 220))
		for idx_dm in range(12):
			x : int = int(self._margin_l + idx_dm * step) - 1
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

		amount_max   : int   = max(self._amounts)
		amount_min   : int   = min(self._amounts)
		amount_avg   : int   = int((amount_min - amount_max) / 2)
		amount_scale : float = 0 if not amount_avg else ((self.height() - 1 - self._margin_b - self._margin_t) // 2) / amount_avg

		for idx, amount in enumerate(self._amounts):
			x            : int = int(self._margin_l + idx * step)
			amount_delta : int = amount - amount_avg
			amount_prc   : int = 0 if not amount_avg else int((amount / amount_avg - 1.00) * 100)
			y_delta      : int = int(amount_delta * amount_scale)

			painter.setPen(QColor(160 if amount_avg > 0 else 180, 160 if amount_avg < 0 else 180, 160))
			painter.setBrush(QColor(200 if amount_avg > 0 else 220, 200 if amount_avg < 0 else 220, 200))
			painter.drawRect(x - 12, y, 24, y_delta)

			painter.setPen(QColor(3, 30, 30))
			painter.setBrush(QColor(255, 255, 255))
			painter.drawRect(x - 25, y - 8, 50, 16)

			painter.setFont(QFont("Noto Sans Mono", 6))
			painter.drawText(QRect(x - 25, self._margin_t - 16, 50, 16), Qt.AlignmentFlag.AlignCenter, f"{AmountToString(amount_prc, flag_sign=True)}%")
			painter.drawText(QRect(x - 25, y - 8, 50, 16), Qt.AlignmentFlag.AlignCenter, AmountToString(amount, flag_sign=True))

	def DrawAvg(self, painter: QPainter):
		""" Отрисовка среднего """
		y : int = (self.height() - 1) // 2
		painter.setPen(QColor(30, 30, 30))
		painter.drawLine(20, y, self.width() - 1 - 20, y)

		amount_max : int = max(self._amounts)
		amount_min : int = min(self._amounts)
		amount_avg : int = int((amount_min - amount_max) / 2)

		painter.setBrush(QColor(255, 255, 255))
		painter.drawRect(QRect(self.width() - 60, y - 8, 50, 16))

		painter.setFont(QFont("Noto Sans Mono", 6))
		painter.drawText(QRect(self.width() - 60, y - 8, 50, 16), Qt.AlignmentFlag.AlignCenter, AmountToString(amount_avg, flag_sign=True))

	def DrawBorder(self, painter: QPainter):
		""" Отрисовка границ """
		painter.setPen(QColor(180, 180, 180))
		painter.setBrush(QColor(255, 255, 255))
		painter.drawRect(0, 0, self.width() - 1, self.height() - 1)

	def paintEvent(self, event):
		painter = QPainter(self)

		self.DrawBackground(painter)
		self.DrawBorder(painter)

		self.DrawTitle(painter)
		self.DrawLabels(painter)
		self.DrawAvg(painter)
		self.DrawAmounts(painter)

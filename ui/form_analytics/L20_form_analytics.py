# КОМПОНЕНТЫ ФОРМЫ АНАЛИТИКИ

from PySide6.QtGui import QColor, QPainter

from L20_PySide6   import C20_DiaFrame


class C20_DiaDynamic(C20_DiaFrame):
	""" Диаграмма динамики """

	def DrawBorder(self, painter: QPainter):
		""" Отрисовка границ """
		painter.setPen(QColor(180, 180, 180))
		painter.setBrush(QColor(255, 255, 255))
		painter.drawRect(0, 0, self.width() - 1, self.height() - 1)

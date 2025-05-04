# ФОРМА АНАЛИТИКА ДАННЫХ: МЕХАНИКА УПРАВЛЕНИЯ
# 27 апр 2025

from PySide6.QtCore     import Qt
from PySide6.QtGui      import QCursor
from PySide6.QtWidgets  import QHeaderView

from L00_form_analytics import GROUPS
from L60_form_analytics import C60_FormAnalytics
from L90_analytics      import C90_AnalyticsItem


class C70_FormAnalytics(C60_FormAnalytics):
	""" Форма Аналитика данных: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка формы """
		self.setWindowTitle(f"Аналитика данных - {self.Workspace.DmDyToString()}")


	# Дерево данных
	def AdjustTreeDataSize(self):
		""" Настройка размера дерева данных """
		self.TreeData.header().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)

	def AdjustTreeDataColor(self):
		""" Настройка цветовой схемы дерева данных """
		self.ModelData.adjustGroupView(False, True, True)

	def AdjustTreeDataExpand(self):
		""" Настройка раскрытия схемы дерева данных """
		self.TreeData.expandAll()

	def AdjustTreeDataSort(self):
		""" Настойка сортировки """
		self.TreeData.sortByColumn(0, Qt.SortOrder.AscendingOrder)

	def ProcessingTreeDataDbClick(self):
		""" Обработка двойного клика по дереву данных """
		match self.processing_group:
			case GROUPS.DISTRIBUTION:
				if not self.processing_ido: return

				self.on_RequestEditDestinationName()


	# Меню структуры аналитики
	def AdjustMenuStruct(self):
		""" Настройка меню структуры аналитики """
		self.MenuStruct.clear()

		if self.processing_ido:
			self.MenuStruct.addAction(self.ActionEditDestinationName)

			if self.processing_parent:
				self.MenuStruct.addAction(self.ActionCreateDestination)

			self.MenuStruct.addAction(self.ActionCreateSubDestination)
			self.MenuStruct.addSeparator()

		self.MenuStruct.addAction(self.ActionCreateTopDestination)
		self.MenuStruct.addSeparator()
		self.MenuStruct.addMenu(self.SubmenuStruct)
		if self._processing_parent: self.MenuStruct.addMenu(self.SubmenuStructGroup)
		if self._processing_ido   : self.MenuStruct.addMenu(self.SubmenuStructItem)


	def AdjustMenuStructText(self):
		""" Настройка текста меню структуры аналитики """
		analytics_item = C90_AnalyticsItem(self.processing_ido)
		parent_item    = C90_AnalyticsItem(analytics_item.parent_ido)

		self.SubmenuStructGroup.setTitle(f"{parent_item.name}")
		self.SubmenuStructItem.setTitle(f"{analytics_item.name}")

		self.ActionCreateDestination.setText(f"Расширить {parent_item.name}")
		self.ActionCreateSubDestination.setText(f"Уточнить {analytics_item.name}")

	def AdjustMenuStructEnable(self):
		""" Настройка доступности меню структуры аналитики """
		pass

	def ShowMenuStruct(self):
		""" Отображение меню структуры аналитики """
		self.MenuStruct.exec_(QCursor().pos())

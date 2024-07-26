# ФОРМА ФИНСОСТАВА: МЕХАНИКА УПРАВЛЕНИЯ
from PySide6.QtCore import QModelIndex
from PySide6.QtGui import QCursor, QFont, QStandardItem
from PySide6.QtWidgets       import QListWidgetItem

from L60_form_findescription import C60_FormFindescription
from L90_findescription      import C90_RecordFindescription


class C70_FormFindescription(C60_FormFindescription):
	""" Форма Финсостав: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка окна """
		self.setWindowTitle(f"Финсостав - {self._category_processing}")

	# Меню финсостава
	def ShowMenuFindescription(self):
		""" Отображение меню финсостава """
		self.mnu_findescription.popup(QCursor().pos())

	def SetupMenuFindescription(self):
		""" Настройка меню финсостава """
		record_findescription = C90_RecordFindescription(self._ido_processing)

		self.mnu_findescription_record_header.setText(record_findescription.Name())
		self.mnu_findescription_move_up.setText(f"Перенести {record_findescription.Name()} выше")
		self.mnu_findescription_move_memory.setText(f"Запомнить {record_findescription.Name()}")

		parent_name = ""
		if record_findescription.ParentIdo():
			record_findescription.Ido(record_findescription.ParentIdo())
			parent_name = record_findescription.Name()
		self.mnu_findescription_parent_header.setText(parent_name if parent_name else "Корневой уровень")

		record_findescription = C90_RecordFindescription(self._ido_memory)
		self.mnu_findescription_parent_paste.setText(f"Перенести {record_findescription.Name()}")
		self.mnu_findescription_record_paste.setText(f"Перенести {record_findescription.Name()}")

	def EnabledMenuFindescription(self):
		""" Установка доступности меню финсостава """
		record_findescription     = C90_RecordFindescription(self._ido_processing)

		flag_selected      : bool = bool(self._ido_processing)
		flag_exist_root    : bool = bool(record_findescription.ParentIdo())
		flag_memory        : bool = bool(self._ido_memory)
		flag_memory_self   : bool = self._ido_memory == self._ido_processing
		flag_memory_parent : bool = self._ido_memory == record_findescription.ParentIdo()

		self.mnu_findescription_parent_paste.setEnabled((flag_exist_root and flag_memory) and not flag_memory_parent)

		self.mnu_findescription_record_create.setEnabled(flag_selected)
		self.mnu_findescription_record_rename.setEnabled(flag_selected)
		self.mnu_findescription_record_delete.setEnabled(flag_selected)

		self.mnu_findescription_move_up.setEnabled(flag_exist_root)
		self.mnu_findescription_move_memory.setEnabled(flag_selected)
		self.mnu_findescription_record_paste.setEnabled(flag_selected and flag_memory and not flag_memory_self)

	# Список категорий финсостава
	def SelectCurrentCategory(self):
		""" Подсветка категории финсостава """
		item_category : QListWidgetItem | None = self.lst_categories.item(0)
		self.lst_categories.setCurrentItem(item_category)

	# Дерево финсостава
	def ExpandTreFindescription(self):
		""" Раскрытие дерева финсостава """
		for index_row in range(self.model_findescription.rowCount()):
			index_record : QModelIndex = self.model_findescription.index(index_row, 0)
			self.tre_findescription.expand(index_record)

	def ShowParents(self):
		""" Отображение корневых записей в структуре """
		font_normal : QFont = self.tre_findescription.font()

		font_bold   : QFont = self.tre_findescription.font()
		font_bold.setBold(True)

		for index_row in range(self.model_findescription.rowCount()):
			item_parent : QStandardItem = self.model_findescription.item(index_row, 0)

			item_parent.setFont(font_bold if item_parent.rowCount() > 0 else font_normal)

	# Модель финсостава
	def ProcessingItemChanged(self):
		""" Обработка изменения записи """
		if self._flag_loading: return

		self.on_ItemCheckStateChanged()

# ФОРМА ОБРАБОТКА ДАННЫХ: ЛОГИКА ДАННЫХ
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QProgressDialog

from L00_colors          import COLORS
from L00_form_processing import INTERVALS, OPERATIONS
from L20_PySide6         import RequestItem, RequestText
from L70_form_processing import C70_FormProcessing
from L90_operations import C90_Operation


class C80_FormProcessing(C70_FormProcessing):
	""" Форма Обработка данных: Логика данных """

	# Параметры Обработка операций
	def EditOperationsInclude(self):
		""" Редактирование параметров Обработка операций: Фрагмент поиска """
		flag_dm : bool       = self._operations_interval == INTERVALS.DM
		dy, dm               = self.workspace.DyDm()

		text    : str | None = RequestText("Обработка операций", "Фрагмент поиска", self._operations_include, self.operations.Destinations(dy if flag_dm else None, dm if flag_dm else None))
		if text is None: return

		self._operations_include = text

	def EditOperationsExclude(self):
		""" Редактирование параметров Обработка операций: Фрагмент исключения """
		flag_dm : bool       = self._operations_interval == INTERVALS.DM
		dy, dm               = self.workspace.DyDm()

		text    : str | None = RequestText("Обработка операций", "Фрагмент исключения", self._operations_exclude, self.operations.Destinations(dy if flag_dm else None, dm if flag_dm else None))
		if text is None: return

		self._operations_exclude = text

	def EditOperationsDestination(self):
		""" Редактирование параметров Обработка операций: Назначение """
		text : str | None = RequestText("Обработка операций", "Назначение", self._operations_destination, self.operations.Destinations())
		if text is None: return

		self._operations_destination = text

	def EditOperationsDetail(self):
		""" Редактирование параметров Обработка операций: Назначение """
		text : str | None = RequestText("Обработка операций", "Уточнение", self._operations_detail, self.operations.Details())
		if text is None: return

		self._operations_detail = text

	def EditOperationsObjectInt(self):
		""" Редактирование параметров Обработка операций: Назначение """
		text : str | None = RequestText("Обработка операций", "Объект внутренний", self._operations_object_int, self.operations.ObjectsInt())
		if text is None: return

		self._operations_object_int = text

	def EditOperationsObjectExt(self):
		""" Редактирование параметров Обработка операций: Назначение """
		text : str | None = RequestText("Обработка операций", "Объект внешний", self._operations_object_ext, self.operations.ObjectsExt())
		if text is None: return

		self._operations_object_ext = text

	def EditOperationsColor(self):
		""" Редактирование параметров Обработка операций: Цветовая метка """
		color : str | None = RequestItem("Обработка операций", "Цветовая метка", [f"{color}" for color in COLORS])
		if color is None: return

		self._operations_color = COLORS(color)

	def SwitchOperationsInterval(self):
		""" Смена интервала  """
		match self._operations_interval:
			case INTERVALS.DM : self._operations_interval = INTERVALS.ALL
			case INTERVALS.ALL: self._operations_interval = INTERVALS.DM

	def ProcessingOperations(self):
		""" Обработка операций """
		dy, dm           = self.workspace.DyDm() if self._operations_interval == INTERVALS.DM else (None, None)

		indexes          = self.model_operations.indexesInRowByIdo(OPERATIONS.DESTINATION)
		item_value       = self.model_operations.itemFromIndex(indexes[0])
		flag_destination = item_value.checkState() == Qt.CheckState.Checked

		indexes          = self.model_operations.indexesInRowByIdo(OPERATIONS.DETAIL)
		item_value       = self.model_operations.itemFromIndex(indexes[0])
		flag_detail      = item_value.checkState() == Qt.CheckState.Checked

		indexes          = self.model_operations.indexesInRowByIdo(OPERATIONS.OBJECT_INT)
		item_value       = self.model_operations.itemFromIndex(indexes[0])
		flag_object_int  = item_value.checkState() == Qt.CheckState.Checked

		indexes          = self.model_operations.indexesInRowByIdo(OPERATIONS.OBJECT_EXT)
		item_value       = self.model_operations.itemFromIndex(indexes[0])
		flag_object_ext  = item_value.checkState() == Qt.CheckState.Checked

		indexes          = self.model_operations.indexesInRowByIdo(OPERATIONS.COLOR)
		item_value       = self.model_operations.itemFromIndex(indexes[0])
		flag_color       = item_value.checkState() == Qt.CheckState.Checked

		idos : list[str] = self.operations.OperationsIdosInDyDmDd(dy, dm)

		dialog_import    = QProgressDialog(self)
		dialog_import.setWindowTitle("Обработка финансовых операций")
		dialog_import.setMaximum(len(idos))
		dialog_import.setWindowModality(Qt.WindowModality.WindowModal)
		dialog_import.setLabelText(f"Осталось обработать: {dialog_import.maximum()} записей")
		dialog_import.setMinimumWidth(480)
		dialog_import.forceShow()

		for index_data, ido in enumerate(idos):
			dialog_import.setValue(index_data + 1)
			dialog_import.setLabelText(f"Осталось обработать: {dialog_import.maximum() - dialog_import.value()} записей")

			operation         = C90_Operation(ido)
			destination : str = operation.Destination()

			if  self._operations_include not in destination                                    : continue
			if (self._operations_exclude     in destination) and bool(self._operations_exclude): continue

			if flag_destination: operation.Destination(self._operations_destination)
			if flag_detail     : operation.Detail(self._operations_detail)
			if flag_object_int : operation.ObjectInt(self._operations_object_int)
			if flag_object_ext : operation.ObjectExt(self._operations_object_ext)
			if flag_color      : operation.Color(self._operations_color)

		self.application.form_operations.UpdateData()

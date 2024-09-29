# ФОРМА ФИНАНАЛИТИКА: МЕХАНИКА ДАННЫХ

from PySide6.QtCore        import Qt, QModelIndex

from G11_convertor_data import AmountToString
from L00_finanalitics import FINANALITICS
from L20_PySide6           import C20_StandardItem
from L50_form_finanalitics import C50_FormFinanalitics


class C60_FormFinanalitics(C50_FormFinanalitics):
	""" Форма Финаналитика: Механика данных """

	# Финаналитика
	def ReadLabelsFinanalitics(self):
		""" Чтение меток финаналитики """
		labels_checked   : list[str] = self.model_options.dataByCheckState(role=Qt.ItemDataRole.DisplayRole, check_state=Qt.CheckState.Checked)
		labels_unchecked : list[str] = self.model_options.dataByCheckState(role=Qt.ItemDataRole.DisplayRole, check_state=Qt.CheckState.PartiallyChecked)

		self.finanalitics.LabelsInclude(labels_checked)
		self.finanalitics.LabelsExclude(labels_unchecked)

	def SendProcessingDy(self):
		""" Отправка текущего года """
		self.finanalitics.ProcessingDy(self.workspace.Dy())

	def SendProcessingDm(self):
		""" Отправка текущего месяца """
		self.finanalitics.ProcessingDm(self.workspace.Dm())

	# Модель данных: Параметры
	def InitModelOptions(self):
		""" Инициализация модели параметров """
		self.model_options.removeAll()

	def LoadLabelGroupInModelOptions(self):
		""" Загрузка группы меток в модель параметров """
		if not self._processing_label: return

		group_name : str = self._processing_label[0]

		if self.model_options.indexByData(group_name, Qt.ItemDataRole.DisplayRole): return

		self.model_options.appendRow(C20_StandardItem(group_name))

	def LoadLabelInModelOptions(self):
		""" Загрузка метки в модель параметров """
		if not self._processing_label  : return

		self.LoadLabelGroupInModelOptions()

		group_name  : str                = self._processing_label[0]
		index_group : QModelIndex | None = self.model_options.indexByData(group_name)

		if     index_group is None     : return

		item_group  : C20_StandardItem   = self.model_options.itemFromIndex(index_group)

		item_label : C20_StandardItem | None = self.model_options.itemByData(self._processing_label, Qt.ItemDataRole.DisplayRole)

		if item_label is None:
			item_label = C20_StandardItem(self._processing_label)
			item_label.setCheckable(True)
			item_label.setUserTristate(True)

			item_group.appendRow(item_label)

	# Модель данных месяца
	def InitModelDataDm(self):
		""" Инициализация модели данных месяца """
		self.model_data_dm.removeAll()

	def LoadModelDataDm_Income(self):
		""" Загрузка данных поступления в модель данных месяца """
		pass

	def LoadModelDataDm_Outcome(self):
		""" Загрузка данных выбытия в модель данных месяца """
		pass

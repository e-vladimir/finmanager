# ФОРМА ЗАПИСЬ ФИНДЕЙСТВИЙ: МЕХАНИКА УПРАВЛЕНИЯ

from PySide6.QtCore             import Qt

from G11_convertor_data         import AmountToString

from L00_months                 import MONTHS_SHORT
from L20_PySide6                import ROLES, C20_StandardItem
from L60_form_finactions_record import C60_FormFinactionsRecord


class C70_FormFinactionsRecord(C60_FormFinactionsRecord):
	""" Форма Запись финдействий: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Заголовок окна """
		self.setWindowTitle(f"Запись финдействий {AmountToString(self.finactions_record.Amount(), False, True)} от {self.finactions_record.DdDmDyToString()}")

	# Основные данные: Год
	def FillCbboxDy(self):
		""" Заполнение списка годов """
		self.cbbox_dy.clear()
		self.cbbox_dy.addItems(list(map(str, self.workspace.AvailableDys())))

	def ShowDy(self):
		""" Отображение года """
		self.cbbox_dy.setCurrentText(f"{self.finactions_record.Dy()}")

	# Основные данные: Месяц
	def FillCbboxDm(self):
		""" Заполнение списка месяцев """
		self.cbbox_dm.clear()
		self.cbbox_dm.addItems(MONTHS_SHORT[1:])

	def ShowDm(self):
		""" Отображение месяца """
		self.cbbox_dm.setCurrentIndex(self.finactions_record.Dm() - 1)

	# Основные данные: Число
	def ShowDd(self):
		""" Отображение числа месяца """
		self.edit_dd.setValue(self.finactions_record.Dd())

	# Основные данные: Сумма
	def ShowAmount(self):
		""" Отображение суммы """
		self.edit_amount.setValue(int(self.finactions_record.Amount()))

	# Исходные данные: Примечание
	def ShowSrcNote(self):
		""" Отображение исходного примечания """
		self.label_src_note.setText(self.finactions_record.SrcNote())

	# Исходные данные: Сумма
	def ShowSrcAmount(self):
		""" Отображение исходной суммы """
		self.label_src_amount.setText(AmountToString(self.finactions_record.SrcAmount(), False, True))

	# Рабочие данные: Примечание
	def ShowNote(self):
		""" Отображение рабочего примечания """
		self.edit_note.setText(self.finactions_record.Note())

	# Рабочие данные: Финструктура
	def ShowFinstruct(self):
		""" Отображение счетов """
		for self._processing_ido in self.finactions_record.FinstructIdos():
			if not self._processing_ido: continue

			item_record : C20_StandardItem | None = self.model_finstruct.itemByData(self._processing_ido, ROLES.ROLE_IDO)
			if item_record is None: continue

			item_record.setCheckState(Qt.CheckState.Checked)

	# Рабочие данные: Метки
	def ShowLabels(self):
		""" Отображение меток """
		self.edit_labels.setPlainText('\n'.join(self.finactions_record.Labels()))

	# Дерево финструктуры
	def AdjustTreeDataExpand(self):
		""" Дерево финструктуры: Настройка  """
		self.tree_finstruct.expandAll()

	def AdjustTreeDataColors(self):
		""" Настройка цветовой схемы дерева финструктуры """
		self.model_finstruct.setGroupsView(True, True)

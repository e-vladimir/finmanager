# ФОРМА ЗАПИСЬ ФИНДЕЙСТВИЙ: МЕХАНИКА ДАННЫХ
from G11_convertor_data import AmountToString
from L00_months                 import MONTHS_SHORT
from L20_PySide6                import C20_StandardItem
from L50_form_finactions_record import C50_FormFinactionsRecord


class C60_FormFinactionsRecord(C50_FormFinactionsRecord):
	""" Форма Запись финдействий: Механика данных """

	# Модель данных
	def InitModel(self):
		""" Инициализация модели данных """
		self.model_data.removeAll()

		self.model_data.fastAppendRow(["ОБЩАЯ ИНФОРМАЦИЯ", ""])  # 0
		self.model_data.fastAppendRow(["Год", ""])
		self.model_data.fastAppendRow(["Месяц", ""])
		self.model_data.fastAppendRow(["Число", ""])

		self.model_data.fastAppendRow(["ИСХОДНАЯ ИНФОРМАЦИЯ", ""])  # 4
		self.model_data.fastAppendRow(["Сумма", "0.00"])
		self.model_data.fastAppendRow(["Примечание", ""])

		self.model_data.fastAppendRow(["ЗАПИСЬ ФИНДЕЙСТВИЙ", ""])  # 7
		self.model_data.fastAppendRow(["Сумма", "0.00"])
		self.model_data.fastAppendRow(["Примечание", ""])
		self.model_data.fastAppendRow(["Счета", ""])
		self.model_data.fastAppendRow(["Метки", ""])

	def LoadFinactionsRecord(self):
		""" Загрузка данных записи финдействий """
		self.finactions_record.Ido(self.workspace.IdoFinactionsRecord())

		item_dy         : C20_StandardItem = self.model_data.item(1, 1)
		item_dm         : C20_StandardItem = self.model_data.item(2, 1)
		item_dd         : C20_StandardItem = self.model_data.item(3, 1)

		item_src_amount : C20_StandardItem = self.model_data.item( 5, 1)
		item_src_note   : C20_StandardItem = self.model_data.item( 6, 1)

		item_amount     : C20_StandardItem = self.model_data.item( 8, 1)
		item_note       : C20_StandardItem = self.model_data.item( 9, 1)
		item_finstruct  : C20_StandardItem = self.model_data.item(10, 1)
		item_labels     : C20_StandardItem = self.model_data.item(11, 1)

		item_dy.setText(f"{self.finactions_record.Dy():04d}")
		item_dm.setText(f"{MONTHS_SHORT[self.finactions_record.Dm()]}")
		item_dd.setText(f"{self.finactions_record.Dd():02d}")

		item_src_amount.setText(f"{AmountToString(self.finactions_record.SrcAmount(), False, True)}")
		item_src_note.setText(f"{self.finactions_record.SrcNote()}")

		item_amount.setText(f"{AmountToString(self.finactions_record.Amount(), False, True)}")
		item_note.setText(f"{self.finactions_record.Note()}")

		item_labels.setText('\n'.join(self.finactions_record.Labels()))

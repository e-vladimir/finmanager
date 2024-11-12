# ФОРМА ФИНАНСОВАЯ ОПЕРАЦИЯ: МЕХАНИКА УПРАВЛЕНИЯ

from G11_convertor_data import AmountToString

from L60_form_operation import C60_FormOperation


class C70_FormOperation(C60_FormOperation):
	""" Форма Финансовая операция: Механика управления """

	# Форма
	def ShowTitle(self):
		""" Отображение заголовка формы """
		amount   : str = AmountToString(self.operation.Amount())
		dd_dm_dy : str = self.operation.DdDmDyToString()

		self.setWindowTitle(f"{amount} от {dd_dm_dy}")

	# Дерево данных
	def AdjustTreeData_Size(self):
		""" Настройка дерева данных: Размеры """
		self.tree_data.setColumnWidth(0, 150)

	def AdjustTreeData_Color(self):
		""" Настройка дерева данных: Цвета """
		self.model_data.adjustGroupView(True, True, True)

	def AdjustTreeData_Expand(self):
		""" Настройка дерева данных: Раскрытие """
		self.tree_data.expandAll()

	def ProcessingTreeData_DbClick(self):
		""" Обработка двойного клика по дереву данных """
		idp_dd              = self.operation.f_dd.Idp().data
		idp_amount          = self.operation.f_amount.Idp().data
		idp_description     = self.operation.f_description.Idp().data
		idp_src_amount      = self.operation.f_src_amount.Idp().data
		idp_src_description = self.operation.f_src_description.Idp().data
		idp_accounts        = self.operation.f_accounts_idos.Idp().data
		idp_labels          = self.operation.f_labels.Idp().data

		if   self._processing_ido == idp_dd         : self.on_RequestSetDate()
		elif self._processing_ido == idp_amount     : self.on_RequestSetAmount()
		elif self._processing_ido == idp_description: self.on_RequestSetDescription()
		elif self._processing_ido == idp_accounts   : self.on_RequestSetAccounts()
		elif self._processing_ido == idp_labels     : self.on_RequestSetLabels()

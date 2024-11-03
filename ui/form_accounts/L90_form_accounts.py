# ФОРМА СЧЕТА: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_accounts import C80_FormAccounts


class C90_FormAccounts(C80_FormAccounts):
	""" Форма Счета: Логика управления """

	def on_Open(self):
		super().on_Open()

		self.ShowTitle()

		self.InitModelData()
		self.ShowAccounts()

		self.AdjustTreeData_Expand()
		self.AdjustTreeData_Sort()
		self.AdjustTreeData_Size()
		self.AdjustTreeData_Color()

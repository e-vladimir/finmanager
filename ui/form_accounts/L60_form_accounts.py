# ФОРМА СЧЕТА: МЕХАНИКА ДАННЫХ
# 14 фев 2025

from PySide6.QtGui      import Qt

from G11_convertor_data import AmountToString

from L20_PySide6        import C20_StandardItem, ROLES
from L50_form_accounts  import C50_FormAccounts
from L90_account        import C90_Account


class C60_FormAccounts(C50_FormAccounts):
	""" Форма Счета: Механика данных """

	# Рабочий IDO
	@property
	def processing_ido(self) -> str:
		return self._processing_ido
	@processing_ido.setter
	def processing_ido(self, ido: str):
		self._processing_ido = ido

	def ReadProcessingIdoFromTreeData(self):
		""" Чтение IDO из дерева данных """
		self.processing_ido = self.TreeData.currentIndex().data(ROLES.IDO)

	# Рабочий IDP
	@property
	def processing_idp(self) -> str:
		return self._processing_idp

	@processing_idp.setter
	def processing_idp(self, idp: str):
		self._processing_idp = idp

	def ReadProcessingIdpFromTreeData(self):
		""" Чтение IDP из дерева данных """
		self.processing_idp = self.TreeData.currentIndex().data(ROLES.IDP)

	# Рабочая группа
	@property
	def processing_group(self) -> str:
		return self._processing_group
	@processing_group.setter
	def processing_group(self, name: str):
		self._processing_group = name

	def ReadProcessingGroupFromTreeData(self):
		""" Чтение группы из дерева данных """
		self.processing_group = self.TreeData.currentIndex().data(ROLES.GROUP)

	# Модель данных
	def InitModelData(self):
		""" Инициализация модели данных """
		self.ModelData.removeAll()

		self.ModelData.setHorizontalHeaderLabels(["Группа счетов\nСчёт",
		                                          "Остаток\nначальный",
		                                          "Остаток\nизменение",
		                                          "Остаток\nрасчётный",
		                                          ])

		for idx_column in range(1, self.ModelData.columnCount()):
			self.ModelData.horizontalHeaderItem(idx_column).setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

	def LoadAccountInModelData(self):
		""" Загрузка счёта в модель данных """
		if not self.processing_ido: return

		account                                      = C90_Account(self.processing_ido)
		group              : str                     = account.group

		item_group         : C20_StandardItem | None = self.ModelData.itemByData(group, ROLES.TEXT)
		if not item_group         : return

		if not self.ModelData.checkIdo(self.processing_ido):
			item_name                            = C20_StandardItem("")
			item_name.setData(self.processing_ido,      ROLES.IDO)
			item_name.setData(account.FName.Idp().data, ROLES.IDP)
			item_name.setData(group,                    ROLES.GROUP)

			item_initial_balance                 = C20_StandardItem(AmountToString(0, flag_point=False, flag_sign=False), flag_align_right=True)
			item_initial_balance.setData(self.processing_ido,                ROLES.IDO)
			item_initial_balance.setData(account.FInitialBalance.Idp().data, ROLES.IDP)
			item_initial_balance.setData(group,                              ROLES.GROUP)

			item_delta_balance                   = C20_StandardItem(AmountToString(0, flag_point=False, flag_sign=False), flag_align_right=True)
			item_delta_balance.setData(self.processing_ido, ROLES.IDO)
			item_delta_balance.setData("", ROLES.IDP)
			item_delta_balance.setData(group,               ROLES.GROUP)

			item_calculated_balance              = C20_StandardItem(AmountToString(0, flag_point=False, flag_sign=False), flag_align_right=True)
			item_calculated_balance.setData(self.processing_ido, ROLES.IDO)
			item_calculated_balance.setData("", ROLES.IDP)
			item_calculated_balance.setData(group,               ROLES.GROUP)

			item_group.appendRow([item_name,
			                      item_initial_balance,
			                      item_delta_balance,
			                      item_calculated_balance,
			                      ])

		initial_balance    : int                     = account.initial_balance
		calculated_balance : int                     = account.CalcCalculatedBalance()
		delta_balance      : int                     = calculated_balance - initial_balance

		indexes                                      = self.ModelData.indexesInRowByIdo(self.processing_ido)

		item_name                                    = self.ModelData.itemFromIndex(indexes[0])
		item_name.setText(account.name)

		item_initial_balance                         = self.ModelData.itemFromIndex(indexes[1])
		item_initial_balance.setText(AmountToString(initial_balance, flag_point=False, flag_sign=False))

		item_delta_balance                           = self.ModelData.itemFromIndex(indexes[2])
		item_delta_balance.setText(AmountToString(delta_balance, flag_point=False, flag_sign=False))

		item_calculated_balance                      = self.ModelData.itemFromIndex(indexes[3])
		item_calculated_balance.setText(AmountToString(calculated_balance, flag_point=False, flag_sign=False))

	def LoadGroupInModelData(self):
		""" Загрузка группы счетов в модель данных """
		if not self.processing_group                                        : return
		if     self.ModelData.indexByData(self.processing_group, ROLES.TEXT): return

		item_group = C20_StandardItem(self.processing_group)
		item_group.setData(self.processing_group, ROLES.GROUP)

		self.ModelData.appendRow([item_group,
		                          C20_StandardItem(""),
		                          C20_StandardItem(""),
		                          C20_StandardItem(""),
		                          ])

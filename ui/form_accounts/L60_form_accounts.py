# ФОРМА СЧЕТА: МЕХАНИКА ДАННЫХ

from L50_form_accounts import C50_FormAccounts


class C60_FormAccounts(C50_FormAccounts):
	""" Форма Счета: Механика данных """

	# Модель данных
	def InitModelData(self):
		""" Инициализация модели данных """
		self.model_data.removeAll()
		self.model_data.setHorizontalHeaderLabels(["Группа счетов\nСчёт"])

	def LoadAccountsGroup(self):
		"""  """
		pass

	def LoadAccount(self):
		"""  """
		pass

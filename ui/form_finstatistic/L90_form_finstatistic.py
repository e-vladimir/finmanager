# ФОРМА ФИНСТАТИСТИКА: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_finstatistic import C80_FormFinstatistic


class C90_FormFinstatistic(C80_FormFinstatistic):
	""" Форма Финстатистика: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Дерево финстатистики
		self.tree_finstatistic.doubleClicked.connect(self.on_RequestExpandRecordFinstatistic)

	def on_Open(self):
		self.ShowTitle()

		self.SetupModelFinstatistic()
		self.ShowFinstatistic()

		self.AdjustTreeFinstatisticExpand()
		self.AdjustTreeFinstatisticSize()

		self.HideZeroRowsInTreeFinstatistic()

		self.model_finstatistic.setGroupsView(False, True, True)

	# Дерево финстатистики
	def on_RequestExpandRecordFinstatistic(self):
		""" Запрос на фрагментацию записи финстатистики """
		self.ReadIndexProcessing()
		self.CalcIdosStructProcessingFromSuboids()

		self.ExpandRecordFinstatistic()

		self.AdjustTreeFinstatisticExpand()
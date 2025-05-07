# ФОРМА АНАЛИТИКА ДАННЫХ: МЕХАНИКА ДАННЫХ
# 27 апр 2025

from PySide6.QtCore        import QModelIndex

from G10_datetime          import CalcDyDmByShiftDm
from G11_convertor_data    import AmountToString

from L00_form_analytics    import GROUPS
from L00_months            import MONTHS_SHORT
from L00_operations        import OPERATIONS
from L20_PySide6           import C20_StandardItem, ROLES
from L20_finmanager_struct import T20_AmountItem
from L50_form_analytics    import C50_FormAnalytics
from L90_analytics         import C90_AnalyticsItem
from L90_operations        import C90_Operation


class C60_FormAnalytics(C50_FormAnalytics):
	""" Форма Аналитика данных: Механика данных """

	# Рабочий IDO
	@property
	def processing_ido(self) -> str:
		return self._processing_ido

	@processing_ido.setter
	def processing_ido(self, ido: str):
		self._processing_ido = ido

	def ReadProcessingIdoFromTreeData(self):
		""" Чтение из дерева данных """
		self.processing_ido = self.TreeData.currentIndex().data(ROLES.IDO) or ""

		if self.processing_ido not in [GROUPS.DISTRIBUTION]: return

		self.processing_ido = ""


	# Рабочая группа
	@property
	def processing_group(self) -> str:
		return self._processing_group

	@processing_group.setter
	def processing_group(self, text: str):
		self._processing_group = text

	def ReadProcessingGroupFromTreeData(self):
		""" Чтение из дерева данных """
		self.processing_group = self.TreeData.currentIndex().data(ROLES.GROUP) or ""


	# Рабочая корневой уровень
	@property
	def processing_parent(self) -> str:
		return self._processing_parent

	@processing_parent.setter
	def processing_parent(self, text: str):
		self._processing_parent = text

	def ReadProcessingParentFromTreeData(self):
		""" Чтение из дерева данных """
		self.processing_parent = self.TreeData.currentIndex().data(ROLES.PARENT) or ""

		if self.processing_parent not in [GROUPS.DISTRIBUTION]: return

		self.processing_parent = ""


	# IDO в памяти
	@property
	def memory_ido(self) -> str:
		return self._memory_ido

	@memory_ido.setter
	def memory_ido(self, ido: str):
		self._memory_ido = ido

	def ReadMemoryIdo(self):
		""" Чтение из дерева данных """
		self.memory_ido = self.processing_ido


	# Модель данных
	def InitModelData(self):
		""" Инициализация модели данных """
		self.ModelData.removeAll()
		self.ModelData.setHorizontalHeaderLabels(["Критерий/Показатель анализа", "", "", "", "", ""])


	# Данные распределения месяца
	def InitDistributionInModel(self):
		""" Сброс распределения месяца """
		index_group       = self.ModelData.indexByData(GROUPS.DISTRIBUTION, ROLES.IDO)
		if index_group is None: return

		self.ModelData.removeRow(index_group.row(), QModelIndex())

	def LoadDistributionInModel(self):
		""" Загрузка распределения месяца в модель """
		dy, dm           = self.Workspace.DyDm()
		amount_dm        = self.Analytics.Amount(dy, dm, use_cache=True)

		if not self.ModelData.checkIdo(GROUPS.DISTRIBUTION):
			item_group       = C20_StandardItem(GROUPS.DISTRIBUTION)
			item_group.setData(GROUPS.DISTRIBUTION, ROLES.IDO)
			item_group.setData(GROUPS.DISTRIBUTION, ROLES.GROUP)
			item_group.setData(1,                   ROLES.SORT_INDEX)

			item_income      = C20_StandardItem("+",  flag_align_right=True)
			item_income.setData(GROUPS.DISTRIBUTION, ROLES.IDO)
			item_income.setData(GROUPS.DISTRIBUTION, ROLES.GROUP)

			item_income_pct  = C20_StandardItem("+%", flag_align_right=True)
			item_income_pct.setData(GROUPS.DISTRIBUTION, ROLES.IDO)
			item_income_pct.setData(GROUPS.DISTRIBUTION, ROLES.GROUP)

			item_outcome     = C20_StandardItem("-",  flag_align_right=True)
			item_outcome.setData(GROUPS.DISTRIBUTION, ROLES.IDO)
			item_outcome.setData(GROUPS.DISTRIBUTION, ROLES.GROUP)

			item_outcome_pct = C20_StandardItem("-%", flag_align_right=True)
			item_outcome_pct.setData(GROUPS.DISTRIBUTION, ROLES.IDO)
			item_outcome_pct.setData(GROUPS.DISTRIBUTION, ROLES.GROUP)

			item_delta       = C20_StandardItem("",   flag_align_right=True)
			item_delta.setData(GROUPS.DISTRIBUTION, ROLES.IDO)
			item_delta.setData(GROUPS.DISTRIBUTION, ROLES.GROUP)

			self.ModelData.appendRow([item_group, item_income, item_income_pct, item_outcome, item_outcome_pct, item_delta])

		indexes          = self.ModelData.indexesInRowByIdo(GROUPS.DISTRIBUTION)
		item_group       = self.ModelData.itemByData(GROUPS.DISTRIBUTION, ROLES.IDO)
		item_income      = self.ModelData.itemFromIndex(indexes[1])
		item_income.setText(AmountToString(amount_dm.amount_income, flag_sign=True))

		item_income_pct  = self.ModelData.itemFromIndex(indexes[2])
		item_income_pct.setText("100%")

		item_outcome     = self.ModelData.itemFromIndex(indexes[3])
		item_outcome.setText(AmountToString(amount_dm.amount_outcome, flag_sign=True))

		item_outcome_pct = self.ModelData.itemFromIndex(indexes[4])
		item_outcome_pct.setText("100%")

		item_delta       = self.ModelData.itemFromIndex(indexes[5])
		item_delta.setText(AmountToString(amount_dm.amount_income - abs(amount_dm.amount_outcome), flag_sign=True))

		idos : list[str] = self.Analytics.Idos("")
		for ido in idos:
			idos.extend(self.Analytics.Idos(ido))

			analytics_item   = C90_AnalyticsItem(ido)

			if not self.ModelData.checkIdo(ido):
				item_destination = C20_StandardItem("")
				item_destination.setData(ido,                       ROLES.IDO)
				item_destination.setData(GROUPS.DISTRIBUTION,       ROLES.GROUP)
				item_destination.setData(analytics_item.parent_ido, ROLES.PARENT)

				item_income      = C20_StandardItem("", flag_align_right=True)
				item_income.setData(ido,                       ROLES.IDO)
				item_income.setData(GROUPS.DISTRIBUTION,       ROLES.GROUP)
				item_income.setData(analytics_item.parent_ido, ROLES.PARENT)

				item_income_pct  = C20_StandardItem("", flag_align_right=True)
				item_income_pct.setData(ido,                       ROLES.IDO)
				item_income_pct.setData(GROUPS.DISTRIBUTION,       ROLES.GROUP)
				item_income_pct.setData(analytics_item.parent_ido, ROLES.PARENT)

				item_outcome     = C20_StandardItem("", flag_align_right=True)
				item_outcome.setData(ido,                       ROLES.IDO)
				item_outcome.setData(GROUPS.DISTRIBUTION,       ROLES.GROUP)
				item_outcome.setData(analytics_item.parent_ido, ROLES.PARENT)

				item_outcome_pct = C20_StandardItem("", flag_align_right=True)
				item_outcome_pct.setData(ido,                       ROLES.IDO)
				item_outcome_pct.setData(GROUPS.DISTRIBUTION,       ROLES.GROUP)
				item_outcome_pct.setData(analytics_item.parent_ido, ROLES.PARENT)

				item_delta       = C20_StandardItem("", flag_align_right=True)
				item_delta.setData(ido,                       ROLES.IDO)
				item_delta.setData(GROUPS.DISTRIBUTION,       ROLES.GROUP)
				item_delta.setData(analytics_item.parent_ido, ROLES.PARENT)

				item_parent      = self.ModelData.itemByData(analytics_item.parent_ido, ROLES.IDO) or item_group
				item_parent.appendRow([item_destination, item_income, item_income_pct, item_outcome, item_outcome_pct, item_delta])

			amount_item      = analytics_item.Amount(dy, dm, use_cache=True)

			indexes          = self.ModelData.indexesInRowByIdo(ido)

			item_destination = self.ModelData.itemFromIndex(indexes[0])
			item_destination.setText(analytics_item.name)

			item_income      = self.ModelData.itemFromIndex(indexes[1])
			item_income.setText(AmountToString(amount_item.amount_income,   flag_sign=True))

			item_income_pct  = self.ModelData.itemFromIndex(indexes[2])
			item_income_pct.setText("" if not amount_dm.amount_income else f"{100 * amount_item.amount_income / amount_dm.amount_income:.0f}%")

			item_outcome     = self.ModelData.itemFromIndex(indexes[3])
			item_outcome.setText(AmountToString(amount_item.amount_outcome, flag_sign=True))

			item_outcome_pct = self.ModelData.itemFromIndex(indexes[4])
			item_outcome_pct.setText("" if not amount_dm.amount_outcome else f"{100 * amount_item.amount_outcome / amount_dm.amount_outcome:.0f}%")


	# Данные динамики месяца
	def LoadDynamicDmInModel(self):
		""" Загрузка динамики месяца в модель """
		if not self.ModelData.checkIdo(GROUPS.DYNAMIC_DM):
			item_group       = C20_StandardItem(GROUPS.DYNAMIC_DM)
			item_group.setData(GROUPS.DYNAMIC_DM, ROLES.IDO)
			item_group.setData(GROUPS.DYNAMIC_DM, ROLES.GROUP)
			item_group.setData(2,                   ROLES.SORT_INDEX)

			item_income      = C20_StandardItem("+",  flag_align_right=True)
			item_income.setData(GROUPS.DYNAMIC_DM, ROLES.IDO)
			item_income.setData(GROUPS.DYNAMIC_DM, ROLES.GROUP)

			item_income_pct  = C20_StandardItem("+%", flag_align_right=True)
			item_income_pct.setData(GROUPS.DYNAMIC_DM, ROLES.IDO)
			item_income_pct.setData(GROUPS.DYNAMIC_DM, ROLES.GROUP)

			item_outcome     = C20_StandardItem("-",  flag_align_right=True)
			item_outcome.setData(GROUPS.DYNAMIC_DM, ROLES.IDO)
			item_outcome.setData(GROUPS.DYNAMIC_DM, ROLES.GROUP)

			item_outcome_pct = C20_StandardItem("-%", flag_align_right=True)
			item_outcome_pct.setData(GROUPS.DYNAMIC_DM, ROLES.IDO)
			item_outcome_pct.setData(GROUPS.DYNAMIC_DM, ROLES.GROUP)

			item_delta       = C20_StandardItem("",   flag_align_right=True)
			item_delta.setData(GROUPS.DYNAMIC_DM, ROLES.IDO)
			item_delta.setData(GROUPS.DYNAMIC_DM, ROLES.GROUP)

			self.ModelData.appendRow([item_group, item_income, item_income_pct, item_outcome, item_outcome_pct, item_delta])

		dy, dm                            = self.Workspace.DyDm()
		amount_dm                         = self.Analytics.Amount(dy, dm, use_cache=True)
		amount_dds : list[T20_AmountItem] = [T20_AmountItem() for _ in range(32)]
		operation                         = C90_Operation()
		operation.use_cache               = True

		for ido in self.Operations.Idos(dy, dm, use_cache=True, type_operation=OPERATIONS.ANALYTICAL):
			operation.Ido(ido)

			amount = operation.amount

			if amount > 0: amount_dds[operation.dd].amount_income  += amount
			else         : amount_dds[operation.dd].amount_outcome += amount

		item_group                        = self.ModelData.itemByData(GROUPS.DYNAMIC_DM, ROLES.IDO)
		item_group.removeRows(0, item_group.rowCount())

		amount_dw_1                       = T20_AmountItem(amount_income =int(sum([item.amount_income  for item in amount_dds[  :7]])),
		                                                   amount_outcome=int(sum([item.amount_outcome for item in amount_dds[  :7]])))

		amount_dw_2                       = T20_AmountItem(amount_income =int(sum([item.amount_income  for item in amount_dds[ 7:14]])),
		                                                   amount_outcome=int(sum([item.amount_outcome for item in amount_dds[ 7:14]])))

		amount_dw_3                       = T20_AmountItem(amount_income =int(sum([item.amount_income  for item in amount_dds[14:21]])),
		                                                   amount_outcome=int(sum([item.amount_outcome for item in amount_dds[14:21]])))

		amount_dw_4                       = T20_AmountItem(amount_income =int(sum([item.amount_income  for item in amount_dds[21:  ]])),
		                                                   amount_outcome=int(sum([item.amount_outcome for item in amount_dds[21:  ]])))

		for idx_dw, amount_dw in enumerate([amount_dw_1, amount_dw_2, amount_dw_3, amount_dw_4], start=1):
			item_subgroup    = C20_StandardItem(f"Неделя {idx_dw}",
                                                GROUPS.DYNAMIC_DM,
                                                ROLES.GROUP)

			item_income      = C20_StandardItem(AmountToString(amount_dw.amount_income,
                                                               flag_sign=True),
                                                GROUPS.DYNAMIC_DM,
                                                ROLES.GROUP,
                                                flag_align_right=True)

			item_income_pct  = C20_StandardItem("" if not amount_dm.amount_income else f"{100 * amount_dw.amount_income / amount_dm.amount_income:.0f}%",
                                                GROUPS.DYNAMIC_DM,
                                                ROLES.GROUP,
                                                flag_align_right=True)

			item_outcome     = C20_StandardItem(AmountToString(amount_dw.amount_outcome,
                                                               flag_sign=True),
                                                GROUPS.DYNAMIC_DM,
                                                ROLES.GROUP,
                                                flag_align_right=True)

			item_outcome_pct = C20_StandardItem("" if not amount_dm.amount_outcome else f"{100 * amount_dw.amount_outcome / amount_dm.amount_outcome:.0f}%",
                                                GROUPS.DYNAMIC_DM,
                                                ROLES.GROUP,
                                                flag_align_right=True)

			item_delta       = C20_StandardItem("",
                                                GROUPS.DYNAMIC_DM,
                                                ROLES.GROUP,
                                                flag_align_right=True)

			item_group.appendRow([item_subgroup, item_income, item_income_pct, item_outcome, item_outcome_pct, item_delta])


	# Данные динамики года
	def LoadDynamicDyInModel(self):
		""" Загрузка динамики года в модель """
		if not self.ModelData.checkIdo(GROUPS.DYNAMIC_DY):
			item_group       = C20_StandardItem(GROUPS.DYNAMIC_DY)
			item_group.setData(GROUPS.DYNAMIC_DY, ROLES.IDO)
			item_group.setData(GROUPS.DYNAMIC_DY, ROLES.GROUP)
			item_group.setData(3,                   ROLES.SORT_INDEX)

			item_income      = C20_StandardItem("+", flag_align_right=True)
			item_income.setData(GROUPS.DYNAMIC_DY, ROLES.IDO)
			item_income.setData(GROUPS.DYNAMIC_DY, ROLES.GROUP)

			item_income_pct  = C20_StandardItem("",  flag_align_right=True)
			item_income_pct.setData(GROUPS.DYNAMIC_DY, ROLES.IDO)
			item_income_pct.setData(GROUPS.DYNAMIC_DY, ROLES.GROUP)

			item_outcome     = C20_StandardItem("-", flag_align_right=True)
			item_outcome.setData(GROUPS.DYNAMIC_DY, ROLES.IDO)
			item_outcome.setData(GROUPS.DYNAMIC_DY, ROLES.GROUP)

			item_outcome_pct = C20_StandardItem("",  flag_align_right=True)
			item_outcome_pct.setData(GROUPS.DYNAMIC_DY, ROLES.IDO)
			item_outcome_pct.setData(GROUPS.DYNAMIC_DY, ROLES.GROUP)

			item_delta       = C20_StandardItem("",  flag_align_right=True)
			item_delta.setData(GROUPS.DYNAMIC_DY, ROLES.IDO)
			item_delta.setData(GROUPS.DYNAMIC_DY, ROLES.GROUP)

			self.ModelData.appendRow([item_group, item_income, item_income_pct, item_outcome, item_outcome_pct, item_delta])

		item_group                        = self.ModelData.itemByData(GROUPS.DYNAMIC_DY, ROLES.IDO)
		item_group.removeRows(0, item_group.rowCount())

		dy, dm                            = self.Workspace.DyDm()

		for idx in range(12):
			amount_dm        = self.Analytics.Amount(dy, dm, use_cache=False)

			item_subgroup    = C20_StandardItem(f"{MONTHS_SHORT[dm]} {dy}",
		                                        GROUPS.DYNAMIC_DY,
		                                        ROLES.GROUP)
			item_subgroup.setData(idx, ROLES.SORT_INDEX)

			item_income      = C20_StandardItem(AmountToString(amount_dm.amount_income,
	                                                           flag_sign=True),
                                                GROUPS.DYNAMIC_DY,
                                                ROLES.GROUP,
                                                flag_align_right=True)

			item_income_pct  = C20_StandardItem("",
                                                GROUPS.DYNAMIC_DY,
                                                ROLES.GROUP,
                                                flag_align_right=True)

			item_outcome     = C20_StandardItem(AmountToString(amount_dm.amount_outcome,
			                                                   flag_sign=True),
                                                GROUPS.DYNAMIC_DY,
                                                ROLES.GROUP,
                                                flag_align_right=True)

			item_outcome_pct = C20_StandardItem("",
                                                GROUPS.DYNAMIC_DY,
                                                ROLES.GROUP,
                                                flag_align_right=True)

			item_delta       = C20_StandardItem(AmountToString(amount_dm.amount_income - abs(amount_dm.amount_outcome),
			                                                   flag_sign=True),
                                                GROUPS.DYNAMIC_DY,
                                                ROLES.GROUP,
                                                flag_align_right=True)

			item_group.appendRow([item_subgroup, item_income, item_income_pct, item_outcome, item_outcome_pct, item_delta])
			dy, dm = CalcDyDmByShiftDm(dy, dm, -1)

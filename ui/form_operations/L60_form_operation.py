# ФОРМА ОПЕРАЦИИ: МЕХАНИКА ДАННЫХ
# 11 мар 2025

from PySide6.QtCore     import QModelIndex
from PySide6.QtGui      import QColor, QIcon

from G11_convertor_data import AmountToString

from L00_colors         import COLORS
from L20_PySide6        import C20_StandardItem, ROLES
from L50_form_operation import C50_FormOperation
from L90_operations     import C90_Operation


class C60_FormOperation(C50_FormOperation):
	""" Форма Операции: Механика данных """

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


	# Рабочее число месяца
	@property
	def processing_dd(self) -> int:
		return self._processing_dd

	@processing_dd.setter
	def processing_dd(self, dd: int):
		self._processing_dd = dd

	def ReadProcessingDdFromTreeData(self):
		""" Чтение рабочего дня из дерева данных """
		self.processing_dd = self.TreeData.currentIndex().data(ROLES.GROUP)


	# Модель данных
	def InitModelData(self):
		""" Инициализация модели данных """
		self.ModelData.removeAll()

		self.ModelData.setHorizontalHeaderLabels(["Дата/Сумма",
		                                          "Счёт",
		                                          "Описание/Назначение"
		                                          ])

	def LoadDdInModelData(self):
		""" Загрузка дня в модель """
		if self.processing_dd < 1: return

		name_dd : str = f"{self.processing_dd:02d} {self.Workspace.DmDyToString()}"

		if self.ModelData.indexByData(name_dd, ROLES.TEXT) is not None: return

		item_dd       = C20_StandardItem("", flag_align_right=True)
		item_dd.setText(name_dd)
		item_dd.setData(self.processing_dd, ROLES.GROUP)
		item_dd.setData(self.processing_dd, ROLES.SORT_INDEX)
		item_dd.setIcon(QIcon("./L0/icons/calendar.svg"))

		self.ModelData.appendRow([item_dd,
		                          C20_StandardItem(""),
		                          C20_StandardItem(""),
		                          ])

	def LoadOperationOnModelData(self):
		""" Загрузка операции в модель """
		if not self.processing_ido: return

		operation                                  = C90_Operation(self.processing_ido)
		operation.use_cache                        = True

		idp_amount      : str                      = operation.FAmount.Idp().data
		idp_accounts    : str                      = operation.FAccountIdos.Idp().data
		idp_description : str                      = operation.FDescription.Idp().data

		if operation.parent_ido: item_parent : C20_StandardItem | None  = self.ModelData.itemByData(operation.parent_ido, ROLES.IDO)
		else                   : item_parent : C20_StandardItem | None  = self.ModelData.itemByData(operation.DdDmDyToString(), ROLES.TEXT)

		if item_parent is None: return

		if not self.ModelData.checkIdo(self.processing_ido):
			item_amount      = C20_StandardItem("", flag_align_right=True)
			item_amount.setData(self.processing_ido, ROLES.IDO)
			item_amount.setData(operation.amount,    ROLES.SORT_INDEX)
			item_amount.setData(operation.dd,        ROLES.GROUP)
			item_amount.setData(idp_amount,          ROLES.IDP)

			item_accounts    = C20_StandardItem("")
			item_accounts.setData(self.processing_ido, ROLES.IDO)
			item_accounts.setData(operation.dd,        ROLES.GROUP)
			item_accounts.setData(idp_accounts,        ROLES.IDP)

			item_destination = C20_StandardItem("")
			item_destination.setData(self.processing_ido, ROLES.IDO)
			item_destination.setData(operation.dd,        ROLES.GROUP)
			item_destination.setData(idp_description,     ROLES.IDP)

			item_parent.appendRow([item_amount, item_accounts, item_destination])

		indexes         : list[QModelIndex]        = self.ModelData.indexesInRowByIdo(self.processing_ido)

		item_amount                                = self.ModelData.itemFromIndex(indexes[0])
		item_amount.setText(AmountToString(operation.amount, flag_sign=True))
		item_amount.setData(operation.amount, ROLES.SORT_INDEX)

		item_accounts                              = self.ModelData.itemFromIndex(indexes[1])
		item_accounts.setText('\n'.join(self.Accounts.IdosToNames(operation.account_idos)))

		item_destination                           = self.ModelData.itemFromIndex(indexes[2])
		item_destination.setText(operation.DestinationOrDescription())

		color_bg : QColor = QColor(255, 255, 255)
		color_fg : QColor = QColor(  0,   0,   0)

		match operation.color:
			case COLORS.BLACK: color_fg = QColor(  0,   0,   0)
			case COLORS.GRAY : color_fg = QColor(150, 150, 150)
			case COLORS.GREEN: color_fg = QColor( 30, 130,  30)
			case COLORS.BLUE : color_fg = QColor( 30,  30, 130)
			case COLORS.RED  : color_fg = QColor(130,  30,  30)

		if not operation.destination: color_fg = QColor(150, 150, 150)

		self.ModelData.setRowColor(item_parent,
		                           item_amount.row(),
		                           color_bg,
		                           color_fg)

		suboids : list[str] = operation.suboids

		if   suboids        : item_amount.setIcon(QIcon("./L0/icons/square_black.svg"))
		elif operation.skip : item_amount.setIcon(QIcon("./L0/icons/hide.svg"))
		else                : item_amount.setIcon(QIcon())

		for self.processing_ido in suboids: self.LoadOperationOnModelData()

	def CleanModelData(self):
		""" Очистка модели от некорректных данных """
		dy, dm           = self.Workspace.DyDm()
		idos : list[str] = self.Operations.Idos(dy, dm)
		dds  : list[int] = self.Operations.Dds(dy, dm)

		for index_dd in self.ModelData.indexes(QModelIndex()):
			dd : int = int(index_dd.data(ROLES.GROUP))

			if dd not in dds:
				self.ModelData.removeRow(index_dd.row())
				continue

			for index_ido in reversed(self.ModelData.indexes(index_dd)):
				for index_subido in reversed(self.ModelData.indexes(index_ido)):
					ido: str = index_subido.data(ROLES.IDO)
					if ido in idos: continue

					self.ModelData.removeRow(index_subido.row(), index_ido)

				ido : str = index_ido.data(ROLES.IDO)
				if ido in idos: continue

				self.ModelData.removeRow(index_ido.row(), index_dd)

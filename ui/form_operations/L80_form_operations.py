# ФОРМА ФИНАНСОВЫЕ ОПЕРАЦИИ: ЛОГИКА ДАННЫХ

from PySide6.QtCore      import Qt
from PySide6.QtWidgets   import QProgressDialog

from G11_convertor_data  import AmountToString

from L00_containers      import CONTAINERS
from L20_PySide6         import RequestValue, RequestText, RequestConfirm, RequestMultipleText, QFindReplaceTextDialog, C20_StandardItem, ROLES
from L70_form_operations import C70_FormOperations
from L90_operations      import C90_Operation


class C80_FormOperations(C70_FormOperations):
	""" Форма Финансовые операции: Логика данных """

	# Финансовые операции
	def ShowOperations(self):
		""" Отображение финансовых операций """
		dy, dm = self.workspace.DyDm()

		for self._processing_dd  in self.operations.DdsInDyDm(dy, dm)             : self.LoadDd()
		for self._processing_ido in self.operations.OperationsIdosInDyDmDd(dy, dm): self.LoadOperation()

	def UpdateDataPartial(self):
		""" Частичное обновление данных """
		operation = C90_Operation(self.workspace.IdoOperation())
		self._processing_ido = self.workspace.IdoOperation()
		self._processing_dd  = operation.Dd()

		self.CleanOperation()
		self.CleanDd()

		self.LoadDd()

		self.LoadOperation()

		self.on_UpdateDataPartial()

	def ReplaceText(self):
		""" Поиск и замена текстового фрагмента """
		dy, dm           = self.workspace.DyDm()
		idos : list[str] = self.operations.OperationsIdosInDyDmDd(dy, dm)

		if not idos                 : return

		operation        = C90_Operation(self._processing_ido)
		dialog_request   = QFindReplaceTextDialog("Финансовые операции", "Поиск и замена текстового фрагмента", operation.Description(), operation.Description())
		if not dialog_request.exec(): return

		text_find        = dialog_request.textFind()
		text_replace     = dialog_request.textReplace()

		dialog_progress  = QProgressDialog(self)
		dialog_progress.setWindowTitle("Финансовые операции: Поиск и замена текстового фрагмента")
		dialog_progress.setLabelText("Осталось обработать: --")
		dialog_progress.setWindowModality(Qt.WindowModality.WindowModal)
		dialog_progress.setMaximum(len(idos))

		for self._processing_ido in idos:
			dialog_progress.setValue(dialog_progress.value() + 1)
			dialog_progress.setLabelText(f"Осталось обработать: {dialog_progress.maximum() - dialog_progress.value()}")

			operation = C90_Operation(self._processing_ido)
			if text_find not in operation.Description(): continue

			operation.Description(operation.Description().replace(text_find, text_replace))

			self.LoadOperation()

		dialog_progress.close()

	def ResetData(self):
		""" Сброс данных """
		dy, dm           = self.workspace.DyDm()
		idos : list[str] = self.operations.OperationsIdosInDyDmDd(dy, dm)

		if not idos                                                                  : return
		if not RequestConfirm("Сброс данных", f"Будет удалено операций: {len(idos)}"): return

		dialog_progress  = QProgressDialog(self)
		dialog_progress.setWindowTitle("Финансовые операции: Сброс данных")
		dialog_progress.setLabelText("Осталось обработать: --")
		dialog_progress.setWindowModality(Qt.WindowModality.WindowModal)
		dialog_progress.setMaximum(len(idos))

		for ido in idos:
			dialog_progress.setValue(dialog_progress.value() + 1)
			dialog_progress.setLabelText(f"Осталось обработать: {dialog_progress.maximum() - dialog_progress.value()}")

			operation = C90_Operation(ido)
			operation.DeleteObject(CONTAINERS.DISK)

		dialog_progress.close()

	# Пакет операций
	def UncheckedAllPackOperations(self):
		""" Сброс пакета операций """
		for ido in self._processing_idos:
			item : C20_StandardItem | None = self.model_data.itemByData(ido, ROLES.IDO)
			item.setCheckState(Qt.CheckState.Unchecked)

	def ExpandPackOperations(self):
		""" Расширение пакета операций """
		dy, dm            = self.workspace.DyDm()

		text : str | None = RequestText("Расширение пакета операций", "Поиск в описании")
		if text is None: return

		for ido in self.operations.OperationsIdosInDyDmDd(dy, dm):
			operation                      = C90_Operation(ido)

			if text.lower() not in operation.Description().lower(): continue

			item : C20_StandardItem | None = self.model_data.itemByData(ido, ROLES.IDO)
			if item is None                                       : continue

			item.setCheckState(Qt.CheckState.Checked)

	def CollapsePackOperations(self):
		""" Расширение пакета операций """
		dy, dm            = self.workspace.DyDm()

		text : str | None = RequestText("Сокращение пакета операций", "Поиск в описании")
		if text is None: return

		for ido in self.operations.OperationsIdosInDyDmDd(dy, dm):
			operation                      = C90_Operation(ido)

			if text.lower() not in operation.Description().lower(): continue

			item : C20_StandardItem | None = self.model_data.itemByData(ido, ROLES.IDO)
			if item is None                                       : continue

			item.setCheckState(Qt.CheckState.Unchecked)

	def DeletePackOperations(self):
		""" Удаление пакета операций """
		for self._processing_ido in self._processing_idos:
			operation = C90_Operation(self._processing_ido)
			operation.DeleteObject(CONTAINERS.DISK)

			self.CleanOperation()

	# Финансовая операция
	def CreateOperation(self):
		""" Создание операции """
		dd_dm_dy    : str        = f"{self._processing_dd:02d} {self.workspace.DmDyToString()}"

		amount      : int | None = RequestValue("Создание финансовой операции", f"Создание операции на {dd_dm_dy}", 0, -99999999, 99999999)
		if amount      is None: return

		description : str | None = RequestText("Создание финансовой операции", f"{AmountToString(amount, flag_sign=True)} от {dd_dm_dy}")
		if description is None: return

		operation                = C90_Operation()
		operation.GenerateIdo()
		operation.RegisterObject(CONTAINERS.DISK)
		operation.Dy(self.workspace.Dy())
		operation.Dm(self.workspace.Dm())
		operation.Dd(self._processing_dd)
		operation.SrcAmount(amount)
		operation.SrcDescription(description)
		operation.Amount(amount)
		operation.Description(description)

		self._processing_ido = operation.Ido().data

	def OpenOperation(self):
		""" Открытие операции """
		self.workspace.IdoOperation(self._processing_ido)

		self.application.form_operation.Open()

	def DeleteOperation(self):
		""" Удаление операции """
		operation  = C90_Operation(self._processing_ido)
		text : str = f"{AmountToString(operation.Amount(), flag_sign=True)} от {operation.DdDmDyToString()}\n{operation.Description()}"

		if not RequestConfirm("Удаление операции", text): return

		operation.DeleteObject(CONTAINERS.DISK)

	def SetOperationColor(self):
		""" Установка цвета операции """
		operation = C90_Operation(self._processing_ido)
		operation.Color(self._processing_color)

	def SetOperationDescription(self):
		""" Установка описания операции """
		operation                = C90_Operation(self._processing_ido)
		text        : str        = f"{AmountToString(operation.Amount(), flag_sign=True)} от {operation.DdDmDyToString()}\n{operation.Description()}"

		description : str | None = RequestText("Редактирование операции", text, operation.Description())
		if description is None: return

		operation.Description(description)

	def SetOperationLabels(self):
		""" Установка меток операции """
		operation                      = C90_Operation(self._processing_ido)
		text        : str              = f"{AmountToString(operation.Amount(), flag_sign=True)} от {operation.DdDmDyToString()}\n{operation.Description()}"

		labels      : list[str] | None = RequestMultipleText("Редактирование операции", text, operation.Labels())
		if labels is None: return

		operation.Labels(labels)

	def SplitOperation(self):
		""" Разделение операции """
		operation              = C90_Operation(self._processing_ido)
		text      : str        = f"{AmountToString(operation.Amount(), flag_sign=True)} от {operation.DdDmDyToString()}\n{operation.Description()}"

		amount    : int | None = RequestValue("Разделение операции", text, int(operation.Amount()), -99999999, 99999999)
		if amount is None: return

		ido_old = operation.Ido().data
		operation.Split(amount)

		self.LoadOperation()

		ido_new = operation.Ido().data
		self._processing_ido = ido_new

	def ApplyRulesToOperation(self):
		""" Применение правил обработки данных """
		operation = C90_Operation(self._processing_ido)
		operation.ApplyRulesReplaceText()
		operation.ApplyRulesDetectLabels()

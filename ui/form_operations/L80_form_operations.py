# ФОРМА ФИНАНСОВЫЕ ОПЕРАЦИИ: ЛОГИКА ДАННЫХ

from PySide6.QtCore      import  Qt
from PySide6.QtWidgets   import  QProgressDialog

from G11_convertor_data  import  AmountToString

from L00_containers      import  CONTAINERS
from L20_PySide6         import (RequestValue,
                                 RequestText,
                                 RequestConfirm,
                                 RequestMultipleText,
                                 QFindReplaceTextDialog,
                                 C20_StandardItem,
                                 ROLES)
from L70_form_operations import  C70_FormOperations
from L90_operations      import  C90_Operation


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
		dialog_request   = QFindReplaceTextDialog("Финансовые операции", "Поиск и замена текстового фрагмента.\n\nПоиск в назначении.", operation.Destination(), operation.Destination())
		if not dialog_request.exec(): return

		text_find        = dialog_request.textFind()
		text_replace     = dialog_request.textReplace()

		dialog_progress  = QProgressDialog(self)
		dialog_progress.setWindowTitle("Финансовые операции: Поиск и замена текстового фрагмента")
		dialog_progress.setLabelText("Осталось обработать: --")
		dialog_progress.setWindowModality(Qt.WindowModality.WindowModal)
		dialog_progress.setMaximum(len(idos))
		dialog_progress.setMinimumWidth(480)

		for self._processing_ido in idos:
			dialog_progress.setValue(dialog_progress.value() + 1)
			dialog_progress.setLabelText(f"Осталось обработать: {dialog_progress.maximum() - dialog_progress.value()}")

			operation = C90_Operation(self._processing_ido)
			operation.Destination(operation.Destination().replace(text_find, text_replace))

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
		dialog_progress.setMinimumWidth(480)

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

		text : str | None = RequestText("Расширение пакета операций", "Поиск в описании и назначении")
		if text is None: return

		for ido in self.operations.OperationsIdosInDyDmDd(dy, dm):
			operation                             = C90_Operation(ido)

			flag_result : bool                    = text.lower() in operation.Description().lower()
			flag_result                          |= text.lower() in operation.Destination().lower()

			if not flag_result  : continue

			item        : C20_StandardItem | None = self.model_data.itemByData(ido, ROLES.IDO)
			if     item is None : continue

			item.setCheckState(Qt.CheckState.Checked)

	def CollapsePackOperations(self):
		""" Расширение пакета операций """
		dy, dm            = self.workspace.DyDm()

		text : str | None = RequestText("Сокращение пакета операций", "Поиск в описании и назначении")
		if text is None: return

		for ido in self.operations.OperationsIdosInDyDmDd(dy, dm):
			operation                      = C90_Operation(ido)

			flag_result : bool                    = text.lower() in operation.Description().lower()
			flag_result                          |= text.lower() in operation.Destination().lower()

			if not flag_result  : continue

			item : C20_StandardItem | None = self.model_data.itemByData(ido, ROLES.IDO)
			if     item is None : continue

			item.setCheckState(Qt.CheckState.Unchecked)

	def DeletePackOperations(self):
		""" Удаление пакета операций """
		dialog_progress  = QProgressDialog(self)
		dialog_progress.setWindowTitle("Финансовые операции: Удаление")
		dialog_progress.setLabelText("Осталось удалить: --")
		dialog_progress.setWindowModality(Qt.WindowModality.WindowModal)
		dialog_progress.setMaximum(len(self._processing_idos))
		dialog_progress.setMinimumWidth(480)

		for self._processing_ido in self._processing_idos:
			dialog_progress.setValue(dialog_progress.value() + 1)
			dialog_progress.setLabelText(f"Осталось удалить: {dialog_progress.maximum() - dialog_progress.value()}")

			operation = C90_Operation(self._processing_ido)
			operation.DeleteObject(CONTAINERS.DISK)

			self.CleanOperation()

		dialog_progress.close()

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
		operation.Amount(amount)
		operation.Description(description)

		self._processing_ido = operation.Ido().data

	def OpenOperation(self):
		""" Открытие операции """
		self.workspace.IdoOperation(self._processing_ido)

		self.application.form_operation.Open()

	def DeleteOperation(self):
		""" Удаление операции """
		operation     = C90_Operation(self._processing_ido)
		text    : str = (f"{AmountToString(operation.Amount(), flag_sign=True)} от {operation.DdDmDyToString()}\n\n"
		                 f"Описание:\n{operation.Description()}\n\n"
		                 f"Назначение:\n{operation.Destination()}")

		if not RequestConfirm("Удаление операции", text): return

		operation.DeleteObject(CONTAINERS.DISK)

	def SetOperationColor(self):
		""" Установка цвета операции """
		operation = C90_Operation(self._processing_ido)
		operation.Color(self._processing_color)

	def SetOperationDestination(self):
		""" Установка назначения операции """
		operation                = C90_Operation(self._processing_ido)
		text        : str        = (f"{AmountToString(operation.Amount(), flag_sign=True)} от {operation.DdDmDyToString()}\n\n"
		                            f"Описание:\n"
		                            f"{operation.Description()}")

		destination : str | None = RequestText("Редактирование операции", text, operation.DescriptionOrDestination())
		if destination is None: return

		operation.Destination(destination)

	def SetOperationDescription(self):
		""" Установка описания операции """
		operation                = C90_Operation(self._processing_ido)
		text        : str        = f"{AmountToString(operation.Amount(), flag_sign=True)} от {operation.DdDmDyToString()}"

		description : str | None = RequestText("Редактирование операции", text, operation.Description())
		if description is None: return

		operation.Description(description)

	def SetOperationLabels(self):
		""" Установка меток операции """
		operation                      = C90_Operation(self._processing_ido)
		text        : str              = (f"{AmountToString(operation.Amount(), flag_sign=True)} от {operation.DdDmDyToString()}\n\n"
		                                  f"Описание:\n"
		                                  f"{operation.Description()}\n\n"
		                                  f"Назначение:\n"
		                                  f"{operation.Destination()}")

		labels      : list[str] | None = RequestMultipleText("Редактирование операции", text, operation.Labels())
		if labels is None: return

		operation.Labels(labels)

	def SplitOperation(self):
		""" Разделение операции """
		operation           = C90_Operation(self._processing_ido)
		text   : str        = (f"{AmountToString(operation.Amount(), flag_sign=True)} от {operation.DdDmDyToString()}\n\n"
		                       f"Описание:\n"
		                       f"{operation.Description()}\n\n"
		                       f"Назначение:\n"
		                       f"{operation.Destination()}")

		amount : int | None = RequestValue("Разделение операции", text, int(operation.Amount()), -99999999, 99999999)
		if amount is None: return

		ido_old             = operation.Ido().data
		operation.Split(amount)

		self.LoadOperation()

		ido_new             = operation.Ido().data
		self._processing_ido = ido_new

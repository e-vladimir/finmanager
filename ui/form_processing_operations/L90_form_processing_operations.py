# ФОРМА ОБРАБОТКА ОПЕРАЦИЙ: ЛОГИКА УПРАВЛЕНИЯ

from L80_form_processing_operations import C80_FormProcessingOperations


class C90_FormProcessingOperations(C80_FormProcessingOperations):
	""" Форма Обработка операций: Логика управления """

	def InitEvents(self):
		super().InitEvents()

		# Список субъектов обработки
		self.cbbox_subject.activated.connect(self.on_SubjectChanged)

	# Форма
	def on_Open(self):
		""" Открытие формы """
		self.ShowTitle()

		self.FillCbboxSubject()

		self.ReadProcessingSubjectFromCbboxSubject()
		self.InitModelRules()
		self.ShowRules()
		self.AdjustTableRules_Size()

	def on_Show(self):
		""" Отображение формы """
		self.AdjustTableRules_Size()

	# Субъект обработки
	def on_SubjectChanged(self):
		""" Изменился субъект обработки """
		self.ReadProcessingSubjectFromCbboxSubject()

		self.InitModelRules()
		self.ShowRules()
		self.AdjustTableRules_Size()

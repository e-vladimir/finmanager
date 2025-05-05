# ПРЕДИКТИВНЫЙ АНАЛИЗАТОР ДАННЫХ: МОДЕЛЬ ДАННЫХ
# 08 апр 2025

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model            import LogisticRegression
from sklearn.multiclass              import OneVsRestClassifier
from sklearn.preprocessing           import MultiLabelBinarizer

from G31_cactus_frame                import C31_StructFrameWithEvents

from L20_finmanager_struct           import T20_PredictDescriptionItem, T20_RawOperation


class C40_DataCompleter(C31_StructFrameWithEvents):
	""" Предиктивный анализатор данных: Модель данных """

	def Init_00(self):
		super().Init_00()

		self._data_operations   : dict[str, T20_RawOperation]            = dict()
		self._data_descriptions : dict[str, T20_PredictDescriptionItem]  = dict()

	def Init_10(self):
		super().Init_10()

		self.data_predict_destinations                                   = MultiLabelBinarizer()
		self.model_predict_destinations                                  = OneVsRestClassifier(LogisticRegression(solver="liblinear"))
		self.vectorizer_predict_destination                              = TfidfVectorizer(max_features=1000, stop_words="english")

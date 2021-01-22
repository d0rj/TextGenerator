import pymorphy2
from typing import Dict, Callable


DEFAULT_FORMS = ['nomn', 'gent', 'datv', 'accs', 'ablt', 'loct', 'voct', 'gen2', 'acc2', 'loc2']


class WordMorpher:
	"""
	A class that changes the form of a word for the template engine using built-in commands.

	It is more optimized for constant use than simple function calls every time.
	"""

	__morph = pymorphy2.MorphAnalyzer()

	__cached_words: Dict[str, pymorphy2.analyzer.Parse] = {}
	__form_converters: Dict[str, Callable[[str], str]] = {}


	def __init__(self) -> None:
		self.__form_converters[None] = lambda x: x
		self.__form_converters[''] = lambda x: x
		self.__form_converters['about'] = self.__about_word
		for form in DEFAULT_FORMS:
			self.__form_converters[form] = self.__morphy_default(form)


	def process_word(self, word: str, form: str) -> str:
		"""
		This method does the main job - changes the word.

		Parameters:

			word: The word to change.
			form: String form or template engine's snippet to change that word.
		"""
		return self.__form_converters[form](word)


	def __morphy_default(self, form: str) -> Callable[[str], str]:
		# Default pymorpher2's way to change
		return lambda x: \
			self.__parsed_word(x).inflect({form})[0]


	def __parsed_word(self, word: str) -> pymorphy2.analyzer.Parse:
		# Returns cached parsed word. Adds to cached words if it's new.
		if word not in self.__cached_words:
			self.__cached_words[word] = self.__morph.parse(word)[0]

		return self.__cached_words[word]


	def __about_word(self, word: str) -> str:
		# Snipper for 'о слове' and 'об обоях' form
		result = self.__parsed_word(word).inflect({'loct'}).word

		if result[0] in 'уеыаоэяиюi':
			result = 'об ' + result
		else:
			result = 'о ' + result
		
		return result

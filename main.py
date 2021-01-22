import pymorphy2
import re
from typing import List


WORD_REGEX = r'X\[(\w*)\]'
morph = pymorphy2.MorphAnalyzer()


def load_template(path: str) -> List[str]:
	result: List[str]
	with open(path, 'r', encoding='utf8') as file:
		result = file.readlines()

	return result


def about_word(word: str) -> str:
	result = morph.parse(word)[0].inflect({'loct'}).word

	if result[0] in 'уеыаоэяию':
		result = 'об ' + result
	else:
		result = 'о ' + result
	
	return result


def process_word(word: str, form: str) -> str:
	if form == 'about':
		return about_word(word)
	else:
		return morph.parse(word)[0].inflect({form}).word


def process_template(template: str, word: str) -> str:
	parsed = [m for m in re.finditer(WORD_REGEX, template)]

	matches = [p.group() for p in parsed]
	forms = [p.group(1) for p in parsed]
	
	result = template
	for index, match in enumerate(matches, start=0):
		result = result.replace(match, process_word(word, forms[index]), 1)

	return result


def main() -> None:
	print(process_template(''.join(load_template('./templates/zvonov.txt')), 'коммунизм'))


if __name__ == '__main__':
	main()

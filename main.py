import pymorphy2
import re
from typing import List


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


def process_template(template: List[str], word: str) -> List[str]:
	result: List[str] = []
	for line in template:
		parsed = [m for m in re.finditer(r'X\[(\w*)\]', line)]

		matches = [p.group() for p in parsed]
		forms = [p.group(1) for p in parsed]
		
		processed: str = line
		for index, match in enumerate(matches, start=0):
			processed = processed.replace(match, process_word(word, forms[index]), 1)

		result.append(processed)

	return result


def main() -> None:
	print(''.join(process_template(load_template('./templates/zvonov.txt'), 'коммунизм')))


if __name__ == '__main__':
	main()

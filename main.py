import re
import argparse
import pathlib
from typing import List
from src.word_morpher import WordMorpher


WORD_REGEX = r'X\[(\w*)\]'


def load_template(path: str) -> List[str]:
	result: List[str]
	with open(path, 'r', encoding='utf8') as file:
		result = file.readlines()

	return result


def process_template(template: str, word: str) -> str:
	morpher = WordMorpher()
	parsed = [m for m in re.finditer(WORD_REGEX, template)]

	matches = [p.group() for p in parsed]
	forms = [p.group(1) for p in parsed]
	
	result = template
	for index, match in enumerate(matches, start=0):
		result = result.replace(match, morpher.process_word(word, forms[index]))

	return result


def main() -> None:
	parser = argparse.ArgumentParser()
	parser.add_argument('-X', '--X', type=str, default='коммунизм', metavar='X', help='Значение переменной слова X.')
	parser.add_argument('-f', '--file', type=pathlib.Path, default='./templates/zvonov.txt', metavar='file', help='Входной файл с шаблоном.')

	args = parser.parse_args()

	print(process_template(''.join(load_template(args.file)), args.X))


if __name__ == '__main__':
	main()

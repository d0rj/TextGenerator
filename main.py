import argparse
import pathlib
from typing import List
from src.template_engine import TemplateEngine


def load_template(path: str) -> List[str]:
	result: List[str]
	with open(path, 'r', encoding='utf8') as file:
		result = file.readlines()

	return result


def main() -> None:
	parser = argparse.ArgumentParser()
	parser.add_argument('-X', '--X', type=str, default='коммунизм', metavar='X', 
		help='Значение переменной слова X.')
	parser.add_argument('-f', '--file', type=pathlib.Path, default='./templates/zvonov.txt', metavar='file', 
		help='Входной файл с шаблоном.')
	parser.add_argument('-v', '--variable', action='append', type=lambda kv: kv.split("="), dest='variables', 
		help='Добавляет в список переменных значение. Может применяться несколько раз. Аргумент должен выглядеть как X=слово, где X - любое название вашей переменной')

	args = parser.parse_args()

	filename = args.file
	variables = dict(args.variables)

	engine = TemplateEngine(variables)
	print(engine.process_template(''.join(load_template(filename))))


if __name__ == '__main__':
	main()

import argparse
import pathlib
import os
from typing import List
from src.template_engine import TemplateEngine


def load_template(path: str) -> List[str]:
	result: List[str]
	with open(path, 'r', encoding='utf8') as file:
		result = file.readlines()

	return result


def save_file(filename: str, data: str) -> None:
	if not os.path.exists(filename):
		os.makedirs(os.path.dirname(filename))
	
	with open(filename, 'w+', encoding='utf8') as file:
		file.write(data)


def main() -> None:
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--file', type=pathlib.Path, default='./templates/zvonov.txt', metavar='file', 
		help='Входной файл с шаблоном.')
	parser.add_argument('-v', '--variable', action='append', type=lambda kv: kv.split("="), dest='variables', 
		help='Добавляет в список переменных значение. Может применяться несколько раз. Аргумент должен выглядеть как X=слово, где X - любое название вашей переменной')
	parser.add_argument('-i', '--ignore-unknown', type=bool, required=False, nargs='?', const=True, default=False, metavar='ignore_unknown', 
		help='Этот флаг указывает: игнорировать ли неизвестные переменные в шаблоне (если True), или выбрасывать исключение в ином случае. По умолчанию False.')
	parser.add_argument('-o', '--output', required=False, type=pathlib.Path, metavar='output', default=None, 
		help='Файл для вывода результата. Опционально. Если не указано, то вывод будет в стандартном потоке (консоли).')

	args = parser.parse_args()

	filename = args.file
	variables = dict(args.variables)
	ignore_unknown = bool(args.ignore_unknown)
	output = args.output

	engine = TemplateEngine(variables, ignore_unknown)

	template_string = ''.join(load_template(filename))
	result = engine.process_template(template_string)

	if output:
		save_file(output, result)
	else:
		print(result)


if __name__ == '__main__':
	main()

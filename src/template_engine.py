import re
from typing import Dict, Literal
from src.word_morpher import WordMorpher


class TemplateEngine:	
	variables: Dict[str, str] = {}
	ignore_unknown = False
	
	__morpher = WordMorpher()
	__general_regex: Literal = r'\[[\ ]*([A-Z_-]+)[\ ]*[|]{0,1}[\ ]*(\w*)[\ ]*\]'

	
	def __init__(self, variables: Dict[str, str], ignore_unknown: bool = False) -> None:
		self.variables = { k.upper() : v for k, v in variables.items() }
		self.ignore_unknown = ignore_unknown


	def process_template(self, template: str) -> str:
		result = template

		parsed = [m for m in re.finditer(self.__general_regex, template)]
		parsed = [(p.group(), p.group(1), p.group(2)) for p in parsed]

		matches = [p[0] for p in parsed]
		parsed_vars = [p[1] for p in parsed]
		forms = [p[2] for p in parsed]

		for index, match in enumerate(matches):

			if parsed_vars[index] in self.variables:
				processed_word = self.__morpher.process_word(self.variables[parsed_vars[index]], forms[index])
				result = result.replace(match, processed_word, 1)
			else:
				if self.ignore_unknown:
					continue
				else:
					raise Exception('No such variable: ' + parsed_vars[index] + '.')

		
		return result

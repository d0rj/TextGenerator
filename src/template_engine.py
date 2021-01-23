import re
from typing import Dict, Literal
from src.word_morpher import WordMorpher


class TemplateEngine:
	ANY_VAR_REGEX = r'([A-Z_-]+)'
	
	variables: Dict[str, str] = {}
	ignore_unknown = False
	
	__morpher = WordMorpher()
	__vars_regexes: Dict[str, str] = {}
	__general_regex: Literal = ''

	
	def __init__(self, variables: Dict[str, str], ignore_unknown: bool = False) -> None:
		self.variables = { k.upper() : v for k, v in variables.items() }
		self.ignore_unknown = ignore_unknown

		self.__general_regex = self.__var_regex(self.ANY_VAR_REGEX)

		for var in variables.keys():
			self.__vars_regexes[var] = self.__var_regex(var)


	def process_template(self, template: str) -> str:
		result = template
		
		if self.ignore_unknown:
			for var in self.variables:
				result = self.process_variable(result, var, self.variables[var])			
		else:
			parsed_vars = [m.group(1) for m in re.finditer(self.__general_regex, template)]

			for parsed_var in parsed_vars:
				if parsed_var in self.variables.keys():
					result = self.process_variable(result, parsed_var, self.variables[parsed_var])
				else:
					raise Exception('No such variable: ' + parsed_var + '.')

		return result


	def process_variable(self, template: str, var_name: str, var_value: str) -> str:
		parsed = [m for m in re.finditer(self.__vars_regexes[var_name], template)]

		matches = [p.group() for p in parsed]
		forms = [p.group(1) for p in parsed]
		
		result = template
		for index, match in enumerate(matches, start=0):
			result = result.replace(match, self.__morpher.process_word(var_value, forms[index]))

		return result


	def __var_regex(self, var_name: str) -> str:
		return r'\[[\ ]*' + var_name + r'[\ ]*[|]{0,1}[\ ]*(\w*)[\ ]*\]'

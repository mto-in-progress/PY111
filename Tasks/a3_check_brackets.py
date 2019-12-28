def check_brackets(brackets_row: str) -> bool:
	"""
	Check whether input string is a valid bracket sequence
	Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
	:param brackets_row: input string to be checked
	:return: True if valid, False otherwise
	"""
	cnt: int = 0
	if len(brackets_row) == 0 or (brackets_row[0] == "(" and len(brackets_row) % 2 == 0):
		for ch in brackets_row:
			cnt += 1 if ch == "(" else (-1)
		return True if cnt == 0 else False
	else:
		return False



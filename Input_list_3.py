from typing import List
from numpy import prod


def sucin(numbers: List[int or float]) -> int or float:
	"""Pomaly sposob by bol:
	result = 1
	for i in numbers:
		result *= i
	return result
	"""
	return prod(numbers)


print(sucin( [2, 3, 5, 7, 11]))

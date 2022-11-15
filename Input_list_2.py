from typing import List


def nakup(shopping_list: List[float or int]) -> float:
	result = 0
	for i in range(len(shopping_list) // 2):
		result += shopping_list[2 * i] * shopping_list[2 * i + 1]
	return result
	

print(nakup([3, 2.5, 0.5, 10, 1.2, 1.2]))

from typing import List, Any


def vypis_typy(list: List[Any]):
	for element in list:
		if type(element) == float or type(element) == int:
			result = "cislo"
		elif type(element) == str:
			result = "retazec"
		else:
			result = "iny typ"
		
		print(f"{element} - {result}")


vypis_typy(["god", ("satan", "Majchrak"), 13, 3.1415926535])

from typing import List


def merge(list1: List[int], list2: List[int] = []) -> List[int]:
    """Accepts two sorted
    """
    result: List[int] = []
    while len(list1) > 0 and len(list2) > 0:
        if list1[0] < list2[0]:
            result.append(list1.pop(0))
        else:
            result.append(list2.pop(0))

    if len(list1) > 0:
        for i in list1:
            result.append(i)
    else:
        for i in list2:
            result.append(i)
    return result


print(*merge([12, 13, 45, 46, 75, 89], [1, 2, 3, 4, 5, 6, 13, 13, 32, 34, 48]))

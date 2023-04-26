"""
Binary search
"""

def binary_search(arr, value):
    """
    Binary search algorithm
    we could simply use the built-in list.index() method
    but that would be cheating
    return search_list.index(value)

    search_list: list to search
    value: value to search for
    return: index of value in search_list
    """

    lf, rg = 0, len(arr) - 1

    while lf <= rg:
        mid = (rg + lf) // 2

        if arr[mid] < value:
            lf = mid + 1
        elif arr[mid] > value:
            rg = mid - 1
        else:
            return mid
    else:
        raise ValueError("value not in array")

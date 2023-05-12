import unittest

from bubble_sort import (
    bubble_sort,
)


def test_bubble_sort():
    # Test case 1: Sorting an already sorted array should return the same array
    arr1 = [1, 2, 3, 4, 5]
    bubble_sort(arr1)
    assert arr1 == [1, 2, 3, 4, 5]

    # Test case 2: Sorting a reversed array should return a sorted array
    arr2 = [5, 4, 3, 2, 1]
    bubble_sort(arr2)
    assert arr2 == [1, 2, 3, 4, 5]

    # Test case 3: Sorting an array with duplicates should return a sorted array with duplicates
    arr3 = [2, 5, 3, 2, 4]
    bubble_sort(arr3)
    assert arr3 == [2, 2, 3, 4, 5]

    # Test case 4: Sorting an empty array should return an empty array
    arr4 = []
    bubble_sort(arr4)
    assert arr4 == []

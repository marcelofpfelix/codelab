"""
Bubble sort algorithm
"""


def bubble_sort(arr):
    """
    Bubble sort algorithm
    arr: list to sort
    """

    lenght = len(arr)
    # Traverse through all array elements
    for i in range(lenght):
        swapped = False

        # Last i elements are already in place
        for j in range(0, lenght - i - 1):

            # traverse the array from 0 to n - i - 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # already sorted
        if not swapped:
            break

#include <stdio.h>
#include "bubble_sort.h"

void bubbleSort(int array[], int size) {
  // check if swapping occurs
  int swapped;

  // run loops two times: one for walking throught the array
  for (int i = 0; i < size - 1; ++i) {
    swapped = 0;
    // loop to compare array elements
    for (int j = 0; j < size - i - 1; ++j) {
      // compare two adjacent elements
      if (array[j] > array[j + 1]) {
        // swapping
        int temp = array[j];
        array[j] = array[j + 1];
        array[j + 1] = temp;

        swapped = 1;
      }
    }
    // already sorted
    if (swapped == 0) {
      break;
    }
  }
}

#include <stdio.h>
// Include the header file with the declarations of the functions you create.
#include "binary_search.h"

// Runs the test(s)
int main() {
  int arr[] = { 2, 3, 4, 5, 7, 9, 10 };
  int result, x = 7, n = sizeof(arr) / sizeof(arr[0]);

  result = binarySearch(arr, n - 1, x);
  if (result == -1) {
    printf("Element is not present in array\n");
  }
  else {
    printf("Element is present at index %d\n", result);
  }

  return 0;
}

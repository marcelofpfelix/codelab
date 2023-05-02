#include <stdio.h>
// Include the header file with the declarations of the functions you create.
#include "crystal_balls.h"

// Runs the test(s)
int main() {
  int arr[] = {0, 0, 0, 0, 0, 0, 1, 1, 1};
  int result, n = sizeof(arr) / sizeof(arr[0]);

  result = crystalBalls(arr, n - 1);
  if (result == -1) {
    printf("Element is not present in array\n");
  }
  else {
    printf("Element is present at index %d\n", result);
  }

  return 0;
}

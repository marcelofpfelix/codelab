#include <stdio.h>


int binarySearch(int arr[], int rg, int x) {
  int m, lf = 0;

  while (lf < rg) {
    m = lf + (rg - lf) / 2;
    // Check if x is present at mid
    if (arr[m] == x)
      return m;
    // If x greater, ignore left half
    else if (arr[m] > x)
      rg = m;
    // If x is smaller, ignore right half
    else
      lf = m - 1;
  }
  return -1;
}


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

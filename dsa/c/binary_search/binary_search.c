#include <stdio.h>
#include "binary_search.h"

int binarySearch(int arr[], int rg, int x) {
  int m, lf = 0;

  while (lf <= rg) {
    m = lf + (rg - lf) / 2;
    // If x is smaller, ignore right half
    if (arr[m] < x)
      lf = m + 1;
    // If x greater, ignore left half
    else if (arr[m] > x)
      rg = m - 1;
    // Check if x is present at mid
    else
      return m;
  }
  return -1;
}

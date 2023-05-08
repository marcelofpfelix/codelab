#include <stdio.h>
// Include the header file with the declarations of the functions you create.
#include "bubble_sort.h"

// Function declaration
void printArray(int*, int);


// print array
void printArray(int arr[], int size) {
  for (int i = 0; i < size; ++i) {
    printf("%d  ", arr[i]);
  }
  printf("\n");
}


// Runs the test(s)
int main() {
  int arr[] = { 9, 4, 2, 5, 1, 0, 3, 7 };
  int n = sizeof(arr) / sizeof(arr[0]);
  printArray(arr, n-1);
  bubbleSort(arr, n - 1);
  printArray(arr, n-1);


  return 0;
}

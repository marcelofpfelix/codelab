#include <stdio.h>
#include <math.h>
#include "crystal_balls.h"

int crystalBalls(int arr[], int lenght) {
  int i;
  int jump = ceil(1/2.0 * (sqrt(8 * lenght + 1) + 1));

  printf("jump: %d\n", jump);

  for (i = jump; i < lenght; i += jump) {
    if (arr[i] == 1) {
      break;
    }
    jump--;
  }
  for (int j = (i - jump); j < i; j++ ) {
    if (arr[j] == 1) {
      return j;
    }
  }
  return -1;
}

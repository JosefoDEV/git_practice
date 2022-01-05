#include <stdio.h>
#include <string.h>

void copy(char* dst, char* src){
  while (*src != '\0') {
    *dst = *src;
    src++;
    dst++;
  }
  *dst = '\0';
}

int main()
{
  int x = 1;
  int y = 2;
  int *p_x;
  int numbers[] = {1, 2, 3, 5, 8, 13};
  int *p_n = &numbers[0]; // points to first element of array
  int n_length = sizeof(numbers) / sizeof(int);
  int i;
  char srcString[] = "Just need to test new copy functions.";
  char dstString[strlen(srcString) + 1];
  
  // Reference operator -> '&'
  printf("Address of x: %p\n", &x);
  printf("Data of x: %d\n", x);
  printf("Address of y: %p\n", &y);
  printf("Data of y: %d\n", y);
  printf("Pointer p_x points to: %p\n", p_x);
  //printf("Data of p_x: %d\n", *p_x); 			// Here it would crash because the p_x was not initialized yet.
  p_x = &x;
  printf("Pointer p_x points to: %p\n", p_x);
  printf("Data of p_x: %d\n", *p_x);
  p_x = &y;
  printf("Pointer p_x points to: %p\n", p_x);
  printf("Data of p_x: %d\n", *p_x);
  
  // Dereference operator -> '*'
  printf("Data of p_x: %d\n", *p_x);
  
  // changing data thru pointer
  *p_x = 123;
  printf("Data of p_x: %d\n", *p_x);
  printf("Data of y: %d\n", y);
  
  
  // Iterate thru array using pointer
  for (i = 0; i < n_length; i++) {
    printf("numbers[%d]: %i\n", i, *p_n);
    p_n++;
  }


  copy(dstString, srcString);
  printf("%s\n", dstString);
  
  return 0;
}

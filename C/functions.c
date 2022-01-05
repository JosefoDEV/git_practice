#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// primitive function
void printMyFavoriteColor(void) {
  printf("My favorite color is blue\n");
}

// function that returns something
int getRandom1000() {
  int random1000 = rand() % 1000 + 1;
  return random1000;
}

// Function with one parameter
int getRandomNumber(int maxNumber) {
  int randomNumber = rand() % maxNumber + 1;
  return randomNumber;
}

int main(void) {
  srand(time(NULL));
  
  // call the primitive function
  printMyFavoriteColor();
  
  // Modify the code below
  int randomNumber = getRandom1000();
  printf("My random number is: %d", randomNumber);

  int randomNumber = getRandomNumber(50);
  printf("My random number is: %d", randomNumber);

}
#include <stdio.h>

// Task:
// Implement the fizzbuzz.
// Fizz Buzz is a classic developer interview question that is asked
// or referred to so often for so long, it is almost a cliche!
//
// Write a fizzbuzz.c program that outputs numbers from 1 to 100.
// But for multiples of 3, print "Fizz" instead of the number.
// For the multiples of 5, pring "Buzz" instead of the number.
// If the number os both, multiples of 3 an multiples of 5, print
// "FizzBuzz"

int main()
{
  int i;

  for (i = 1; i <= 100; i++) {
    if ( ((i % 3) == 0) || ((i % 5) == 0) ) {
      if ((i % 3) == 0) {
        printf("Fizz");
      }
      if ((i % 5) == 0) {
        printf("Buzz");
      }
    } else {
      printf("%d", i);
    }
    printf("\n");
  }
  return i;
}
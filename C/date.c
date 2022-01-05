#include <stdio.h>

// Task:
// Write a program that takes any user input in the format `mm/dd/yyyy`
// and prints it out in the style "January 1st, 2022" (derived in English from whatever input is given)

int main(void) {
  int month, day, year;

  // Standard date form
  printf("Enter date (mm/dd/yyyy): ");
  // Split the user input into 3 variables for the date
  // Don't worry about the `scanf()` below, you'll learn more about these later!
  scanf("%d /%d /%d", &month, &day, &year);

  // Print the month
  switch(month) {
    case 1:
      printf("January");
      break;
    case 2:
      printf("February");
      break;
    case 3:
      printf("March");
      break;
    case 4:
      printf("April");
      break;
    case 5:
      printf("May");
      break;
    case 6:
      printf("June");
      break;
    case 7:
      printf("July");
      break;
    case 8:
      printf("August");
      break;
    case 9:
      printf("September");
      break;
    case 10:
      printf("October");
      break;
    case 11:
      printf("November");
      break;
    case 12:
      printf("December");
      break;
  }

  printf(" ");

  // Print the day
  printf("%d", day);

  // Print the suffix for a given day
  if ( (day == 1) || (day == 21) || (day == 31) ) {
    printf("st");
  }
  else if ( (day == 2) || (day == 22) ) {
    printf("nd");
  }
  else if ( (day == 3) || (day == 13) || (day == 23) ) {
    printf("rd");
  } else {
    printf("th");
  }
  printf(", ");
  
  

  // Print the year
  printf("%d\n", year);
  
  return 0;
}
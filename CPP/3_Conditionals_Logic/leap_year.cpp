#include <iostream>

int main() {
  int year;
  
  std::cout << "Type a year: ";
  std::cin >> year;

  if (year > 999) {
    if (year % 4 == 0) {
      if ( (year % 100 == 0) && (year % 400 != 0) ) {
        std::cout << year << "is not a leap year";
      } else {
        if (year % 400 == 0) {
          std::cout << year << "is a leap year";
        } else {
	     std::cout << year << " is a not leap year";
	    }
      }
    } else {
	  std::cout << year << " is a not leap year";
	}
  }
}
#include <iostream>

// return type
// ^  name of function
// |  ^             function parameters 
// |  |             ^  
// |  |             |  
void printGreetings( ) {
// Here is definition of function inside curly parenthesis
  std::cout << "Hello\n";	
}

// above function is a subroutine (which has no return parameter) and it usually suppose to be used for print some text.

// if the return type is not void, there must be a value returned from the functions.
// the return value must be same as return type;
bool tired() {
	bool is_tired;
	std::cout << "Are you tired? (1: for Yes, 0: for No):";
	std::cin >> is_tired;
	return is_tired;
}

// below you can see function with parameters
double get_tip(double price, double tip_in_percent) {
	return price * tip_in_percent / 100.0;
}

int main() {
	
	// Function calloc
	printGreetings();
	
	std::cout << tired();
	
	std::cout << get_tip(15.50, 20.0);
	
}
#include <iostream>

int main() {
	// array declaration of size 5;
	char numbers[5];
	//array declaration with initialising => no need to define size of an array
	char vowels[] = { 'a', 'e', 'i', 'o', 'u' }; 
	
	std::cout << vowels[0]; // Prints: a
 
    vowels[0] = 'y';
 
    std::cout << vowels[0]; // Prints: r
	
}
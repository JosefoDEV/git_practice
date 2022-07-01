#include <iostream>

int main() {
  
  int power = 9000;
  
  // Not initialized pointer
  //int* ptr;
  
  // Initialize to Null pointer (old approach inherited from C lang)
  //int* ptr = NULL;

  // Initialize to Null pointer (modern approach)
  int* ptr = nullptr;

  // Later in the program...
  ptr = &power;
  
  // Print ptr
  std::cout << ptr << "\n";
  
}
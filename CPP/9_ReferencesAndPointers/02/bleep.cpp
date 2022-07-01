#include <iostream>
#include <string>
#include "functions.hpp"

int main() {
  std::string word = "broccoli";
  std::string text = "sadfbroccoliasdfbroccoli";

  std::cout << text << "\n";
  bleep(word, text);
  std::cout << text << "\n";
}
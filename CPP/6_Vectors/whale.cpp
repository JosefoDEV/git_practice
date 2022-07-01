#include <iostream>
#include <vector>
#include <string>

int main() {
  //std::string input = "turpentine and turtles";
  //std::string input = "hi, human";
  std::string input = "a whale of a deal!";
  std::vector<char> vowels = {'a', 'e', 'i', 'o', 'u' };
  std::vector<char> result;

  for (int i = 0; i < input.size(); i++) {
    for (int j = 0; j < vowels.size(); j++) {
      if (input[i] == vowels[j]) {
        result.push_back(vowels[j]);
        if (input[i] == 'e' || input[i] == 'u') {
          result.push_back(vowels[j]);
        }
      }
    }
  }

  for (int i = 0; i < result.size(); i++) {
    std::cout << result[i];
  }

}
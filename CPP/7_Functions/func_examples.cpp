#include <iostream>
#include <vector>

// Define tenth_power() here:
int tenth_power(int num) {
  int result = 1;
  for (int i = 0; i < 10; i++) {
    result *= num;
  }
  return result;
}

// Define first_three_multiples() here:
std::vector<int> first_three_multiples(int num) {
 std::vector<int> res;
 for (int i = 1; i <= 3; i++) {
   res.push_back(num * i);
 }
 return res;
}

std::string needs_water(int days, bool is_succulent) {
  if (is_succulent == false && days > 3) {
    return "Time to water the plant";
  }
  else if (is_succulent && days < 12 ) {
    return "Don't water the plant";
  }
  else if (is_succulent && days >= 13 ) {
    return "Go ahead and give the plant a little water.";
  }
  else {
    return "Don't water the plant!";
  }
}

/* A palindrome is any text that has the same characters backwards as it does forwards.
 * For example, “hannah” and “racecar” are palindromes, while “menu” and “aardvark” are not.
 */
bool is_palindrome(std::string text) {
  bool res = true;

  for (int i = 0; i < text.size() / 2; i++) {
    if (text[i] != text[text.size() - i - 1]) {
      res = false;
      break;
    }
  }
  return res;
}

int main() {
  
  std::cout << tenth_power(0) << "\n";
  std::cout << tenth_power(1) << "\n";
  std::cout << tenth_power(2) << "\n";
  
  for (int element : first_three_multiples(8)) {
    std::cout << element << "\n";
  }
  
  std::cout << needs_water(10, false) << "\n";
  
  std::cout << is_palindrome("madam") << "\n";
  std::cout << is_palindrome("ada") << "\n";
  std::cout << is_palindrome("lovelace") << "\n";
  
}
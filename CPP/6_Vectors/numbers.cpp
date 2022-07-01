#include <iostream>
#include <vector>

int main() {
  std::vector<int> nums = {2, 4, 3, 6, 1, 9};
  int sum_even, product_odd;

  sum_even = 0;
  product_odd = 1;

  for(int i = 0; i < nums.size(); i++) {
    if (nums[i] % 2 == 0) {
      sum_even += nums[i];
    } else {
      product_odd *= nums[i]; 
    }
  }

  std::cout << "Sum of even numbers is " << sum_even << "\n";
  std::cout << "Product of odd numbers is " << product_odd << "\n";

}
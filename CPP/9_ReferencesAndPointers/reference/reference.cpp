#include <iostream>

void swap_num(int &i, int &j) {
  int temp = i;
  i = j;
  j = temp;
}

int triple(int &i) {
  i = i * 3;
  return i;
}

int main() {
  
  int num = 1;
  int &numref = num;
  int i = 10;
  int j = 20;
  
  std::cout << "num = " << num << ", numref = " << numref << "\n";
  numref++;
  std::cout << "num = " << num << ", numref = " << numref << "\n";
  
  std::cout << triple(num) << "\n";
  std::cout << triple(num) << "\n";
  
  std::cout << "i = " << i << ", j = " << j << "\n";
  swap_num(i, j);
  std::cout << "i = " << i << ", j = " << j << "\n";

}

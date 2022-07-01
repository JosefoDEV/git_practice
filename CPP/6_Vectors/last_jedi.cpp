#include <iostream>
#include <vector>

int main() {
  
  std::vector<int> even = {2, 4, 6, 8, 10};
  std::vector<int> odd = (5);
  std::vector<std::string> last_jedi;
  
  // .push_back()
  // Add characters here:
  last_jedi.push_back("kylo");
  last_jedi.push_back("rey");
  last_jedi.push_back("luke");
  last_jedi.push_back("finn");
    
	odd[0] = 1;
	odd[1] = 3;
	odd[2] = 5;
	odd[3] = 7;
	odd[4] = 9;
 
  // .size()
  std::cout << "Number of last jedi's: " << last_jedi.size() << "\n"; 
  
  std::cout << last_jedi[0] << "\n";
  std::cout << last_jedi[1] << "\n";
  std::cout << last_jedi[2] << "\n";
  std::cout << last_jedi[3] << "\n";
  
  std::cout << "First 5 odd numbers\n";
  for(int i = 0; i < odd.size(); i++) {
	std::cout << odd[i] << "\n";  
  }
  
  // .pop_back()
  
  
  
}
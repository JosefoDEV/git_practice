#include <iostream>

int main() {
   double weight;
   int target;
   double target_weight;

   std::cout << "what is the earth weight?";
   std::cin >> weight;
  
   std::cout << "What is the target planet (destination)? ";
   std::cin >> target;
   
   switch (target) {
     case 1:
     case 3:
       target_weight = 0.38 * weight;
       break;
     case 2:
       target_weight = 0.91 * weight;
       break;
     case 4:
       target_weight = 2.34 * weight;
       break;
     case 5:
       target_weight = 1.06 * weight;
       break;
     case 6:
       target_weight = 0.92 * weight;
       break;
     case 7:
       target_weight = 1.19 * weight;
       break;
   }

   std::cout << "Destination planet weight: " << target_weight << "\n";
 
}
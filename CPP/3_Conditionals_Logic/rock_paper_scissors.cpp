// Rock, paper, scissors, spock, lizzard game
// How it works ...
// 1. Scissors cut paper
// 2. Paper covers rock
// 3. Rock crushes Lizzard
// 4. Lizzard poisons Spoc
// 5. Spock (Start Trek character) smashes scissors
// 6. Scissors decapitates lizard
// 7. Lizard eats paper
// 8. Paper disproove Spock
// 9. Spock vaporizes Rock
// 10. Rock crushes scissors

#include <iostream>
#include <stdlib.h>

int main() {

  srand(time(NULL));

  int computer = rand() % 3 + 1;

  int user = 0;

  std::cout << "====================\n";
  std::cout << "rock paper scissors!\n";
  std::cout << "====================\n";

 std::cout << "1) ✊\n";
 std::cout << "2) ✋\n";
 std::cout << "3) ✌️\n";

 std::cout << "shoot! ";

 std::cin >> user;

 if (user == computer) {
   std::cout << "Draw!\n";
 } else {
   if (user > computer) {
     if (user - computer == 1) {
       std::cout << "Winner is user with choice " << user; 
     } else {
       std::cout << "Winner is computer with choice " << computer; 
     }
   } else {
     if (computer - user == 1) {
       std::cout << "Winner is computer with choice " << computer; 
     } else {
       std::cout << "Winner is user with choice " << user;        
     }
   }
 }

}
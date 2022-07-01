#include <iostream>
#include <cstdlib>

int main() {
  int answer;
  std::cout << "MAGIC 8-BALL: ";
  srand(time(NULL));
  answer = std::rand() % 10;

  if (answer == 0) {
    std::cout << "It is certain";
  }
  else if (answer == 1) {
    std::cout << "Not sure";
  }
  else if (answer == 2) {
    std::cout << "Even tought";
  }
  else if (answer == 3) {
    std::cout << "Your right";
  }
  else if (answer == 4) {
    std::cout << "If you think so";
  }
  else if (answer == 5) {
    std::cout << "No way Man!";
  }
  else if (answer == 6) {
    std::cout << "Ohh, come on!";
  }
  else if (answer == 7) {
    std::cout << "Are you serious?";
  }
  else if (answer == 8) {
    std::cout << "Got it!";
  }
  else {
    std::cout << "Very doubtful";
  }
}
#include <iostream>
#include "song.hpp"

int main() {

  Song back_to_black("Back to Black", "Amy Winehouse");

  std::cout << "Title: " << back_to_black.get_title() << "\n";
  std::cout << "Artist: " << back_to_black.get_artist() << "\n";
    
}
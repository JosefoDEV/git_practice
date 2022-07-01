#include <iostream>
#include "profile.hpp"

Profile::Profile(std::string new_name, int new_age, std::string new_city, std::string new_country, std::string new_pronouns) {
  name = new_name;
  age = new_age;
  city = new_city;
  country = new_country;
  pronouns = new_pronouns;
}

std::string Profile::view_profile() {
  std::string info = "Name: " + name;
  info += "\nAge: " + std::to_string(age);
  info += "\nLive in: " + city + ", " + country;
  info += "\nPronouns: " + pronouns;

  for (int i = 0; i < hobbies.size(); i++) {
    info += "\nHobby: " + hobbies[i];
  }
  return info;
}

void Profile::add_hobby(std::string new_hobby) {
  hobbies.push_back(new_hobby);
}

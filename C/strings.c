#include<stdio.h>
#include<string.h>

int main() {
  char greeting[] = {'H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '\0'}; 
  char s1[] = "London";
  char s2[] = " Bridge";

  char n[] = "New";
  char y[] = " York";
  char c[] = " City";
  char pan[] = "How vexingly quick daft zebras jump!";
  int len = strlen(pan) + 1; // Checkpoint 2
  char dst2[len];

  // Code for checkpoint 1 goes here
  printf("strlen(s1): %lu\n", strlen(s1));
  strcat(s1, s2);
  printf("%s\n", s1);
  printf("strlen(s1): %lu\n", strlen(s1));
  // Code for checkpoint 2 goes here
  strcat(n, y);
  strcat(n, c);
  printf("%s\n", n);
  
  strcpy(dst2, pan);
  printf("%s\n", dst2);
  
}
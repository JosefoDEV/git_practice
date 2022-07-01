#include <string>

void bleep(std::string &word, std::string &text) {
  int idx_start, idx_stop;
  int i, j;
  for (i = 0; i < text.size(); i++) {
    idx_start = idx_stop = -1;
    for (j = 0; j < word.size(); j++) {
      if (word[j] == text[i + j]) {
        if (j == 0) {
          idx_start = i;
        }
        if ((j + 1) == word.size()) {
          idx_stop = i + j;
        }
      }
    }
    if ((idx_start != -1) && (idx_stop != -1)) {
      for (j = idx_start; j <= idx_stop; j++) {
        text[j] = '*';
      }
      i = j - 1;
    }
  }
}
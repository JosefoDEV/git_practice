# You can think of string as a list of characters
# Like any other list, each character in string has an index

vegetable = "couliflower"
# Follows indexes of string
#            012345678910

print(vegetable)

# Accessing specific index
print(vegetable[0])

# We can select chunks of characters from a string using following syntax
# string[fist_index:last_index]
# When we slice a string we are creating new string that starts at (and includes) the first_index and ends at (but excludes) the last_index
print(vegetable[2:7]) # should print: 'ulifl'

# There is also open-ended selection
# If we remove the first index, the slice starts at the begining
print(vegetable[:7])  # should print: 'coulifl'

# When we remove the last indes, the slice continue to the end of the string
print(vegetable[3:])  # should print: 'liflower'

# == Concatenating strings

word1 = "Jingle"
word2 = "Bells"
word3 = word1 + word2

print(word3)

# == Use built-in function len() to check length of the string for better slicing
print(word3[:len(word3) - 2])  # should print: 'JingleBel'

# print last character of string
print(word3[len(word3) - 1])

# print last three character of string
print(word3[len(word3) - 3:])

# == Using negative indices

# print lst character of the string
print(word3[-1])

# print last three character of string
print(word3[-3:])


# Strings are immutable. This means that when we are slicing or concatenating we are creating
# entirely new string
# Mutability means that if the data are mutable, then we can change them, if they are immutable, we cannot change them.

# Lets try to change the string
word = "try"
#word[0] = "c"
# we would get following error
# TypeError: 'str' object does not support item assignment

# == Escape characters using '\'
sentence = "He shout: \"Hey, stop!\""
print(sentence)

# == Strings and Conditionals

# using our custom function
def contains(word, letter):
  for w in word:
    if w == letter:
      return True
  return False

print(contains("Hello", "l"))
print(contains("Hello", "J"))

# using 'in' keyword. 'in' checks if on string is part of another string
# letter in word
print("l" in "Hello")
print("J" in "Hello")

# In fact the 'in' is more powerfull and allow us to check whether the string contains substring
print("llo" in "Hello")
print("llol" in "Hello")

# function that takes two strings and returns a list with all of the letters they have in common
def common_letters(string_one, string_two):
  str = []
  for i in range(len(string_one)):
    for j in range(len(string_two)):
      if string_one[i] == string_two[j]:
        if string_one[i] not in str:
          str.append(string_one[i])
        break
        
  return str
  
print(common_letters("banana", "cream"))
print(common_letters("python", "ruby on rails"))


# == String methods
#
# === Formatting methods
# .lower() returns the string with all lowercase characters.
# .upper() returns the string with all uppercase characters.
# .title() returns the string in title case, which means the first letter of each word is capitalized.
# all above methods create a new string (do not change actual string)

word4 = "BLACK"
print(word4.lower())
word5 = "yellow"
print(word5.upper())
sentence2 = "yes. naturelly, this has to be true."
print(sentence2.title())

# .split() takes one argument (string) and returns a list of substrings
# string_name.split(delimiter)
# default delimiter is space ' ' if you leave argument blank

days = "Monday Tuesday Wednesday Thursday Friday Saturday Sunday"
print(days.split())

numbers = "1;2;3;4;5;6;7;8;9"
print(numbers.split(';'))

text = \
"""The ocean is blue.
The water is also blue.
The sky is blue and clear.
Fire is bad master.
Mind is clean and clear.
"""

print(text)

# using escape sequence in splitting
# You can use favourite esc. sequences like '\n' -> newline , '\t' -> horizontal tab
sentences = text.split("\n")
print(sentences)

# .join() is the opposite of .split() and it will join list if strings together with a given delimiter
# 'delimiter'.join(list_you_want_to_join)

textcopy = '\n'.join(sentences)
print(textcopy)

my_name = ["My", "name", "is", "Josef"]

print(' '.join(my_name))
print(''.join(my_name))

# .strip() strips all whitespace characters frome the beginning and end.
text_with_whitespaces = "      Hello World!    "
print("'" + text_with_whitespaces + "'")
print("'" + text_with_whitespaces.strip() + "'")

# .strip(argument) can clean also custom characters from the string
text_with_mess = "###Hello Planet###"
print("'" + text_with_mess + "'")
print("'" + text_with_mess.strip('#') + "'")


# .replace() Takes two arguments and replaces all instances of the first argument in a string with the second argument
# string_name.replace(substring_being_replaced, new_substring)
nums = "1 2 3 4 5 6 7"
nums_with_commas = nums.replace(" ", "_")
print(nums)
print(nums_with_commas)

# .find() searches for string that is put as argument in the string on which was applied .find() 
#         and returns the first index value where that string is located
print("Jelly".find('l'))


# .format() useful method for including variables in strings
print("My favourite number is {}".format(3))

# We can use also keywords to remove ambiguity
print("Hello. My name is {name} and my favourite number is {number}".format(name="Josef", number=7))


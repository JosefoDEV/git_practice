# A list is defined inside square brackets. Items are separated by commas.
numbers = [1, 2, 3, 5, 8, 13]

# List can contain also strings
shapes = ["square", "circle", "rectangle"]

# List can contain different data types
combined_list = ["fork", 23, True]

# Even this is possible: list of lists
identities = [['Josef', 35], ['Marek', 23], ['Josh', 66]]

# There is available zip command that pair list with another list
names = ['Jack', 'Thomas', 'John']
ages = [26, 34, 13]

# apply zip
names_ages = zip(names, ages)
# prints object information
print(names_ages)

# print nested lists
print(list(names_ages))

# Empty list
e_list = []

# Append items to list
e_list.append("brick")

print(e_list)

# Append items to list
e_list.append("stone")

print(e_list)

# Removing items from list
e_list.remove("brick")

print(e_list)

# Adding multiple items using '+'
n_list = ['stone', 'paper']
e_list = n_list + ['scissors', 'cloth']

print(e_list)

# To add single element we need to put it into list
e_list += ['shoe']


# Range feature
# Range feature allows users to create list of consecutive numbers so instead of
#c_list = [0, 1, 2, 3, 4]
# we use following
c_list = range(5)
# Note: range generates numbers from 0 .. <input parameter> - 1
# range also returns object so to print the items use
print(list(c_list))

# Range with more parameters
# Two params, 1st: start number, 2nd up to number
# Following will generate numbers: 3, 4, 5, 6, 7, 8, 9
c_list2 = range(3, 10)
print(list(c_list2))


# Three params, 1st: start number, 2nd: up-to-number, 3rd: skip numbers
# Generates: 1, 3, 5, 7, 9
c_list3 = range(1, 10, 2)
print(list(c_list3))


# Access to first and last elements
n_list = [1, 2, 3, 4, 5]
print("List n_list: " + str(n_list))
print("First element of list n_list: " + str(n_list[0]))
print("Last element of list n_list: " + str(n_list[-1]))



tmp_list = [ "blue", "yellow", "gray", "violet", "gray", "black", "green", "blue" ]

# = List methods
# .count() : counts the number of occurrences of an element in a list
print(tmp_list.count("blue"))

print(tmp_list)
# .insert() : add an element into a specific index of a list
tmp_list.insert(1, "red")

print(tmp_list)

# .pop() : removes an element from a specific indesx or from the end of a list
# note that .pop() can have optional argument
tmp_list.pop()
print(tmp_list)
tmp_list.pop(-2)
print(tmp_list)



# .sort() : sorts a list
letters = [ 'F', 'E', 'J', 'A', 'L', 'T' ]
print(letters)

letters.sort()
print(letters)

letters.sort(reverse=True)
print(letters)



# = build-in functions
# range() : create a sequence of integers
# sorted() : sorts a list
# len() : find out length of list
# zip() : combines lists together



print("Number of items in tmp_list: " + str(len(tmp_list)))


# Slicing lists
# Syntax: my_list[start_index:end_index]
# Example:
colours = [ "red", "green", "blue", "magenta", "yellow", "cyan", "black", "white" ]
print(colours)

colours_rgb = colours[0:3]
print(colours_rgb)

# Slicing lists II
# get elements from start of list
# Syntax: my_list[:n]
# Example:
colours_first_five = colours[:5]
print(colours_first_five)

# get elements from tail of list
# Syntax: my_list[-n:]
# Example:
colours_last_two = colours[-2:]
print(colours_last_two)

# get elements from start of list (ignoring spefified number of last elements)
# Syntax: my_list[:-n]
# Example:
colours_sliceoff_last_four = colours[:-4]
print(colours_sliceoff_last_four)

# Using built-in sorted function
# Note: sorted() will generate new list rather than modifying it
words = [ "number", "cell", "digital", "car", "lost", "autonomous" ]
print(words)

words_sorted = sorted(words)
print(words_sorted)

# Would produces IndexError
#print(words[8])

nums = [65, 66, 67]
letters = ['A', 'B', 'C']

# zip() will combine the arrays together
nums_letters = zip(nums, letters)

print(nums_letters)
print(list(nums_letters))








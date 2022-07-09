# Lesson 1 basics
# variables

# A string type variable
# Definining string using double quotes
firstname = "John"
# Definining string using single quotes
lastname = 'Deer'
# Declaring very long string
description = """
This is an example of declaring very long
string that will take few
lines.
"""

# Number type variable (integer)
age = 36
# Number type variable (float)
height = 189.5

# Boolean type variable [True, False]
is_married = True
is_pregnant = False


# Basic built-in function:

greetings = "Hello World"

# Prints the string to standard output
print(greetings)
print("My name is " + firstname + " " + lastname)

# Using str() build-in function to convert number (integer) to string to be able to print it
# to console
print("I am " + str(age) + " years old")

print(description)

# Print data-types using build-in function type()
print("Data type of firstname: " + str(type(firstname)))
print("Data type of description: " + str(type(description)))
print("Data type of age: " + str(type(age)))
print("Data type of height: " + str(type(height)))
print("Data type of is_married: " + str(type(is_married)))
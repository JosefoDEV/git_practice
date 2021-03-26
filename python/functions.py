# Function contains a some code definitions that can be called from outside of function
# Use 'def' keyword to define function
# example:
def hello_world():
  print("Hello World!")
  print("GoodBye World!")

print("Hello python")
# Here we will call it
hello_world()


# Functions can accept parameters
def greeting(name):
  print("Hello " + name)
  print("Goodbye " + name)

greeting("Nick")

# Multiple parameters
def multiply(number1, number2):
  print(number1 * number2)

multiply(2, 5)


# There are three different types of arguments we can put to function
# 1. Positional arguments: called by their position in the function definition
#   Example
multiply(2, 5)

# 2. Keyword arguments: these can be called by their name
#   Example
#   + the order of parameters is not tied
multiply(number2=5, number1=2)

# 3. Default arguments: which sets the default values for the argument
#   Example
def say_hello(greetings="Hello"):
  print(greetings + " World!")

say_hello()
say_hello("Good Morning")

### Built-in functions
# Built-in functions are functions that we use and that are defined in python itself
# Example of built-in functions: 'print()', ...
# Here we can find list of supported built-in functions for python 3:
# https://docs.python.org/3/library/functions.html

num1 = 12.23
num2 = 3.45
num3 = 50.23

# using built-in min() function
num_min = min(num1, num2, num3)
print(num_min)


# using built-in max() function
num_max = max(num1, num2, num3)
print(num_max)



# using built-in round() function
rounded_num2_onedec = round(num2, 1)
print(rounded_num2_onedec)


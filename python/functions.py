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

# In Python there are 3 different types of arguments we can give a function.

# * Positional arguments: arguments that can be called by their position in the function
# * Keyword arguments: arguments that can be called by their name
# * Default arguments: arguments that are given default values.

# number1 is positioned as the first parameter, number2 is positioned as the second parameter.
def product(number1, number2, printit = False):
  if (printit):
    print(number1 * number2)
  return number1 * number2
 

# 5 is number1
# 10 is number2 
product(5, 10)

# calling the function using keyword arguments
product(number2=10, number1=5)

product(5, 10, True)

# Built-in functions are functions that are coming with language it self
# Example: print(), len(), str(), max(), ...

# Multiple returns
def getDays():
  return "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday";
  
  
days = getDays()

print(type(days))
print(days)
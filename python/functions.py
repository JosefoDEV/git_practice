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

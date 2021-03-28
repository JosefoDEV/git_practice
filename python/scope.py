# Scope of variable (access to variable)
# 1. Local -> defined only inside function
def printPrice():
  price = 100
  print("This costs " + str(price))

printPrice()

# We will get error: 'NameError: name 'price' is not defined'
#print(price)

# 2. Global -> defined outside function
weight = 100
def printWeight():
  print("My weigth is " + str(weight))


printWeight()
print(weight)

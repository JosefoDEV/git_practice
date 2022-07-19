# Dictionary is an unordered set of key: value pairs
# This is useful for association data, for example item: price

# example:
vegetables = { "onion": 4, "couliflower": 6, "potatoes": 3 }
# Dictionary begin and ends with curly braces '{ ... }'
# Each item consist of key ("onion") and value (4)
# Each item is separated by a comma

# Key does not need to be string. It can be also number. See followin example
times = { 1: 4.43, 2: 4.49, 3: 4.65 }

print(times) 

# Values can be of any type: string, number, list or another dictionary
skils = { "web design": ["html5", "css3", "javascript"], "data science": ["python", "bash", "git", "jubpyter"] }

# We can also mix key and value types
animal = { "species": "dog", "age": 2, "class": ["mammals", "canidae", "canis"] }
print(animal)

# Dictionaries in Python rely on each key having a hash value, a specific identifier for the key. 
# If the key can change, that hash value would not be reliable. So the keys must be
# always unchangeable, hashable data types, like numbers or strings.

# Following would produce TypeError: unhashable type: 'list'
#people = { ["Sarah", "Jessica", "Parker"]: "actor1" }

# An empty dictionary
my_dict = {}

print(my_dict)

# Add item using following syntax
my_dict["black"] = 3

print(my_dict)

my_dict["white"] = 5
my_dict["blue"] = 6

print(my_dict)

# Add multiple items using .update() method
my_dict.update( { "red": 7, "green": 9 } )

print(my_dict)

# Overwriting value can be done by:
my_dict["black"] = 4

print(my_dict)

# Dictionary comprehensions allows to join lists into one dictionary
# Example
l_items = ["banana", "flower", "joghurt", "bread", "water"]
l_prices = [4, 6, 7, 12, 15]

purchase = { key:value for key, value in zip(l_items, l_prices) }
print(purchase)

# Accessing a value thru specific key
print("Price for flower:", purchase["flower"])

# Accessing an non-existent item will result with KeyError:
#print("Price for apple:", purchase["apple"])
#KeyError: 'apple'

# To avoid such error use check conditional
if "apple" in purchase:
  print("Price for apple:", purchase["apple"])
  
# There is also another method to avoid such error which is called try/except blocks
try:
  print("Price for apple:", purchase["apple"])
except KeyError:
  print("The key 'apple' doesn't exists!")
  
# Using .get() method to search for a value instead dict[key]
# if the key does not exist a 'None' would be returned
print("Price for banana:", purchase.get("banana"))
print("Price for apple:", purchase.get("apple"))

# We can also specify a value to return if the key does not exist
print("Price for apple:", purchase.get("apple", "N/A"))

# Delete a Key using .pop() method that will remove the key-value pair from dictionary and also return the value
# dictionary.pop(key, default)
# default means default value if the key is not find
flower_price = purchase.pop("flower", 0)
print(purchase)
print(flower_price)

# Get All Keys
# We can use built-in function list() which will return all keys as list
print(list(purchase))

# As alternative we can use method .keys() which will returns 'dict_keys' object
# dist_keys object is read-only
purchase_keys = purchase.keys()
print(purchase_keys)
for key in purchase.keys():
  print(key)
  
# Get All Values
# Using method .values() we will obtain 'dict_values' object representing all values from dictionary
purchase_values = purchase.values()
print(purchase_values)
for val in purchase_values:
  print(val)
  

# Get All Items
# There is a method .items() that will retun 'dict_list' object representing all items from dictionary
# dist_list is a tuple consisting of (key, value)
for it, price in purchase.items():
  print("Item '" + it + "' price: " + str(price))
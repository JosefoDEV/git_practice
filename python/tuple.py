# Tuple in python build-in data type holding various information inside.
# Tuple object is immutable (once is created it cannot be modified)

item = ('bone', 'white', 4)

print(item)
print(item[0])
print(item[1])
print(item[-1])

# Unpacking tuple
name, colour, weight = item

print("Item name:", name)
print("Item colour:", colour)
print("Item weight:", weight)

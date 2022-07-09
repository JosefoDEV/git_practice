print("### for loops ###")
# for loop skeleton:
# for <temp_var> in <collection>:
#   <action>
# 

numbers = [1, 2, 3, 4, 5]

# using normal approach
for num in numbers:
    print(num)

print()    
# using one-liner (elegant loops)
for n in numbers: print(n)

print()
# new Error type: 'IndentationError' when you do not keep proper indentation
#for num in numbers:
#print(num)


# Using range()

for i in range(10):
    print(i)
print()
    
print("### while loops ###")
# While loops skeleton:    
#while <conditional statement>:
#  <action>
  
# example:  
cnt = 5

while cnt > 0:
    print(cnt)
    cnt -= 1
    
print()


# Elegant way:
cnt = 5
while cnt > 0: print(cnt); cnt -= 1
    
print("### Loop Control: Break ###")

# When the program hits break statement it immediately terminates a loop
# Example:

things = ['car', 'house', 'bicycle', 'computer', 'television']

print(things)

for item in things:
    print(item)
    if item == 'bicycle':
        break


print("### Loop Control: Continue ###")

# When the program hits continue statement it immediately skips the current iteration and moves onto the next element in the list
# Example:

numbers = [1, -2, -4, 2, -6, 3, -3, 5, 4, 5]

for num in numbers:
    if num < 0:
        continue
    print(num)


print("### Nested Loops ###")

animals = [['lion', 'tiger', 'dog'], ['throut', 'shark' 'bluefish']]

for species in animals:
    for animal in species:
        print(animal)



print("### List Comprehensions ###")

# Skeleton is
# new_list = [<expression> for <element> in <collection>]
# Example:
print(numbers)

numbers = [1, 2, 3, 4, 5]
print(numbers)
doubled_numbers = [num * 2 for num in numbers]
print(doubled_numbers)

print("### List Comprehensions: Conditionals ###")

# Skeleton is
# new_list = [<expression> for <element> in <collection> <conditional>]
# or 
# new_list = [<expression> <conditional> for <element> in <collection>]

doubled_odd_numbers = [num * 2 for num in numbers if num % 2 == 1]
print(doubled_odd_numbers)

double_odd_tripled_even_numbers = [num * 2 if num % 2 == 1 else num * 3 for num in numbers]
print(double_odd_tripled_even_numbers)

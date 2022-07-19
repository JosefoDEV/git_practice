# == Reading a file
# Using built-in open() function and .read() method from file object
# We can use foolowing syntax to open file, create file object ( 'text_file' ) and store the content of the file into
# variable 'text_data'
with open('welcome.txt') as text_file:
  text_data = text_file.read()
  
print(text_data)

# To get each line into separate variable use
with open('people.txt') as people:
  for line in people.readlines():
    print(line)
    
# Sometimes you need to read just one line from file for which is usefull method .readline()
with open('people.txt') as people:
  first = people.readline()
  second = people.readline()
  
print(first)
print(second)


# == Writing a file
# using 2nd optional parameter of built-in function open(<filen>, [mode])
# if mode parameter is not present, then "r" will be used which means Read (Opens a file for reading)
with open('created_file.txt', 'w') as created_file:
  created_file.write("This is my fist line I created in new text file!")


# Keep in mind that mode 'w' means that if the file already exist it will be overwritten (so you will  lost all data stored in)

# === Apending to a file
# use 'a' as mode
with open('created_file.txt', 'a') as file_to_append:
  file_to_append.write("I am appending some text to this file.")


# The 'with' keyword invokes something called a 'context manager' that
# takes care of opening the file when we call open() and then closing the file after
# we leave the indented block

# Using old syntax
file_to_append = open('created_file.txt', 'a')

# Do some operations with a file
file_to_append.write("I am appending another cool text to this file.")
# We need to manually close the file to prevent issues
file_to_append.close()


# Parsing CSV files
# CSV stands for Comma-Separated Values
# CSV format used as portable format (Microsoft Excel, Google Sheets, ...)
# See database.csv as a example
with open('database.csv') as database:
  print(database.read())

# Converting data to dictionary using DictReader
import csv

list_of_age = []
with open('database.csv', newline='') as people_csv:
  human = csv.DictReader(people_csv)
  for row in human:
    #print(row)
    list_of_age.append(row['Age'])

#print(human)
print(list_of_age)

# csv.DictReader() converts the lines of our CSV file to Python dictionaries which we can use access methods for.

# CSV files does not need to have comma as a separator.
# They can use tab, semicolon for example
# So we need to modify csv.DictReader to use delimiter option. For example:
# csv.DictReader(<file_object>, delimiter=';') # which will expect semicolon as delimiter
# For example file colors.csv is formatted as
#ColorName;HexValue
#white;FFFFFF
with open('colors.csv', newline='') as colors_csv:
  color = csv.DictReader(colors_csv, delimiter=';')
  for row in color:
    print(row['HexValue'])
    
# === Writing csv file
# We can use csv.DictWriter() for that

list_users = [
    {'name': 'John', 'age': 45},
    {'name': 'Brennan', 'age': 32},
    {'name': 'Alice', 'age': 54},
    {'name': 'Neil', 'age': 25},
    {'name': 'Ray', 'age': 75},
            ]
            
with open('users.csv', 'w') as output_csv:
  fields = ['name', 'age' ]
  output_writer = csv.DictWriter(output_csv, fieldnames=fields)
  output_writer.writeheader()
  for item in list_users:
    output_writer.writerow(item)


# === Reading a JSON file
# JSON is an abbreviation of JavaScript Object Notation
# JSON's format is endearingly similar to Python dictionary syntax, and so JSON files might be easy to read
# from a Python developer standpoint.
# Python comes with a 'json' package that will help us parse JSON files into actual Python dictionaries.
# Example of JSON file
# {
#   'firstname': 'John',
#   'lastname': 'Wick',
#   'age': 45
# }
#
# We can be able to read it using following code
import json

with open('personas.json') as personas_json:
  personas_data = json.load(personas_json)


print(personas_data["firstname"])


# === Writing a JSON file
# Do not forget to open file with 'w' mode which means write mode
# Use json.dump() method for writing.
import json

with open('codecademy.json', 'w') as codecademy_json:
  json.dump(list_users, codecademy_json)

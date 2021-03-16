# Here are described basics how to control the program flow using if/elif/else statements

age = 33

if age <= 3:
  print("Baby")
elif (age > 3) and (age < 18):
  print("Child")
elif (age >= 18) and (age < 70):
  print("Adult")
else:
  print("Senior")

flag = True
statement = "if flag or (1 != 2):";
if flag or (1 != 2):
  print(statement + " True")
else:
  print(statement + " False")

flag = False
statement = "if flag or (1 != 2):";
if flag or (1 != 2):
  print(statement + " True")
else:
  print(statement + " False")

statement = "if flag or (1 == 2):";
if flag or (1 == 2):
  print(statement + " True")
else:
  print(statement + " False")

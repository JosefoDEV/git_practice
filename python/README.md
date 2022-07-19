# Python

This directory contains usefull information about python language

## basics.py

Contains fundamental things like printing message to standard output, using variables with
various data types: **string**, **number**, **boolean**

## ctrlflow.py

Contains python control flow methodics. How to use **if**/**elif**/**else** statement.
Usage of relational operators: **>**, **>=**, **<**, **<=**
Includes also Boolean Operators: **and**/**or**/**not**

## errors.py

Describes basic types of errors in python which are: **SyntaxError**, **NameError** and **TypeError**

## functions.py

Contains tutorial for functions.

## import.py

How to import a module


## list.py


Contains introduction how to create list in python.
It also contains another usefull information for appending items to list. 
Creating combined list using **zip** function.
Also **range** function is documented with various examples.
list introduces new Error types:

List methods:
.append()
.remove()
.count()
.insert()
.pop()
.sort()

Built-in functions:
range()
len()
sorted()
zip()

* IndexError -> IndexError: list index out of range
* ValueError -> ValueError: list.remove(x): x not in list

## tuple.py

Contains information about tuple data structure.
Example:

```
student = ( "Joe", "Woods", 23, "student address" )
```

Typle is mutable, so you cannot change, add or remove items from it

## loops.py

Contains information about loops such as **for**, **while**, **foreach**

## strings.py

Additional information to strings. How are they working

## modules.py

Python allows us to package code into file or set of files called modules
A module is a collection of Python declarations intended broadly to be used
as a tool. They are also ofter referred to as 'libraries' or 'packages'.

A package is really a directory that holds a collection of modules

Basic syntax for using a module in code is
```
import module_name
```
Or if you need to import only part of module
```
from module_name import object_name
```

Most commonly used modules

* datetime
* random


Usefull code:
1. Create list of random numbers (length: 10 numbers, values from 1 to 100)
```
random_list = [random.randint(1,100) for i in range(10)]
```

Python default behavior for namespace is module name.
A namespace isolates the functions, classses and variables defined in the modle from the code
in the file doing the importing.
Sometimes, the module's name could also conflict with an object you have defined within your
local namespace.
Fortunately, this name can be altered by aliasing using *as* keyword
```
import module_name as name_you_pick_for_the_module
```

Using a package manager (like conda or pip3) you can install plenty of various modules


### Virtual environments with pipenv

VE are usefull in situations where you as a programmer are working on various projects and
each project is dependent on different version of module. 

So for example on project1 you are using module 'numpy' with latest version 1.23.1
On the other hand on project2 you are also using module 'numpy' but with older version 1.20.3

So for these situations we can use pipenv package that will allow us to create environment/folder
with specifi dependencies (specific versions of dependencies)

Dependencies:

* installed Python3
```
python --version
```  

* installed pip (Python package manager)
  you can check it using command
```
pip --version
```  

To install pipenv use following command:
```
pip install --user pipenv 
```

To create VE make project folder, switch to it and use following command:
```
pipenv --three
```

To download dependencies:
```
pipenv install numpy
```

or install with specific version
```
pipenv install numpy==<version>
```

example:
```
pipenv install numpy==1.20.3
```

To activate VE switch to project folder (where did you install specific versions of modules using 'pipenv install' command and run following command:
```
pipenv shell
```

To quit from VE use command:
```
exit
```


## dictionaries.py

Contains usefull information about dictionaries

## files.py
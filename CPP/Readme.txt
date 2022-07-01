Test driven development:
https://en.wikipedia.org/wiki/Test-driven_development

DRY code: Don't repeat yourself (using functions)


Following is from Codecademy:

* Scope is the region of code that has access to an element.
  Globally scoped variables are accessible everywhere.
  A variable created inside a function has local scope and can’t be accessed outside the function.

* C++ functions are usually split to make code more modular:
   + The declaration in a header file.
   + The definition in another .cpp file.

* Programs with multiple .cpp files need to be linked at compile time:

```
    g++ main.cpp fns.cpp
```

* Header files must be included in the file with main():
```
    #include "fns.hpp"
```

* You can define a function inline using the inline keyword, which may or may not improve execution speed.

* Default arguments can be added to function declarations so that you can call the function without including those arguments.

* You can overload C++ functions so that they handle different types of input and return different types.

* A function template enables a function to behave the same with different types of parameters.

* Classes and Objects (Object oriented programming)
  + Class is specification of new data-type
  + Object is an instance of a class
  + attributes, also known as member data
  + methods, member functions
  + contructor - a way to give the object some data right when it gets created.
  + desctructor - is a special method that handles object destruction
  
* References and Pointers
  A reference variable is an alias for something else, that is, another name for an already existing variable
   + anything we do to the reference also happens to the original
   + aliases cannot be changed to alias something else
   
   + Pass-by-reference refers to passing parameters to a function by using references. When called, the function can modify the value of the arguments by using the reference passed in.

     This allows us to:
       - Modify the value of the function arguments.
       - Avoid making copies of a variable/object for performance reasons.

   + The “address of” operator, &, is used to get the memory address, the location in the memory, of an object.
   
   + When & is used in a declaration, it is a reference operator.
   + When & is not used in a declaration, it is an address operator.
   
  A pointer variable is mostrly the same as other variables, which can store a piece of data.
  Ulinke normal variables, which sotre a value (such  as an int, double, char), a pointer
  stores a memory address.
  
  While references are a newer mechanism that originated in C++, pointers are an older mechanism that was inherited from C.
  We recommend avoiding pointers as much as possible; usually, a reference will do the trick.
  However, you will see pointers a lot in the wild, particularly in older projects, where they are used in a very similar way to references.

    * Dereference - is used to obtain the value pointed to by a variable.
	* Null Pointer (nullptr) - provides a typesafe pointer value representing an empty pointer.
	
* Memory Allocation
  To avoid wastage of memory, you can dynamically allocate any memory required during runtime using the new and delete operators in C++.
    + The Rule of Three

	  The rule of three is a rule of thumb in C++ that claims that if a class defines one of the following special member functions, it should define all three:

		Destructor
		Copy constructor
		Copy assignment operator

	+ The Rule of Five

	  With C++11, a new rule emerged: the rule of five. This adds two more special functions to the rule of three list:

		Destructor
		Copy constructor
		Copy assignment operator
		Move constructor
		Move assignment operator

	+ Standard Library Smart Pointers

	  A smart pointer is an abstract data type that was popularized by C++ during the early 1990’s.
	  It simulates a pointer while providing additional features, such as automatic memory management.

	  In the standard library, we have the following:

		unique_ptr: a smart pointer that owns and manages another object through and disposes of that object when the unique_ptr goes out of scope.
		shared_ptr: a smart pointer that retains shared ownership of an object through a pointer. Several shared_ptr objects may own the same object.

  
  
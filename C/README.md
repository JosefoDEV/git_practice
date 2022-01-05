# C

This directory contains usefull information about C language

## Variables

### Naming rules

* Names can be composed of upper and lower case letters, numbers and underscores.
* The first character must be a letter (upper or lower case).
* No keywords are allowed as the full name (`int` is not allowed but `int_count` would work).

### Data types

Main data types are: `int`, `float`, `double` and `char`

* `int` examples: -1, 3, 2345, 4356634
* `float` examples: -23.5, -0.3, 1.78, 3453.3453
* `double` examples: -12312.12, 0.2342, 35634.34637637
* `char` examples: 'a', '1', 'C', '_', ...

### Fload vs Double

A `float` has less precision than a `double`. 6 vs 15 possible decimal places respectively.
Therefore takes up less memory (4 vs 8 bytes). However, a `double` run faster, so you gain speed at the cost of more memory usage.

The other thing to be aware of is that the system is rouding the values you store in either.
This can cause unexpected resutls, especially with a `float` as they have less precision.
This is why you will see `double` being used any time accuracy is important, such as in scientific, medical or financial applications.

### Casting

```
int x = 1;
char c = 'c';

// Implicit
x = c;

// Explicit cast
x = (int) c;
```
Check out `variable_basics.c` program for basic work with variables.

## Operators

### Mathematical operations:

Basic mathematical operations in C: addition, subtraction, division, multiplication, inrementing, decrementing, modulo

```
int a = 1;
int b = 2;
int c = a + b;
ind d = b - a;
float e = a * b;
float f = a / 2;
```

### Module

It gives a remainder after the division. 

```
int a = 4;
int b = 11;
int c = a % 2; // result will be 0
int d = b % 2; // result will be 1
```

### Increment, Decrement

We can use shorthand tricks

```
int a = 1;
a++; // a will be 2
a--; // a will be 1
```

### Assignment

```
int a = 1;
int b = 3;

a = a + b;
// or using shorthand trick
a += b;
// we can use any of `+=`, `-=`, `*=`, `/=`, `%=` shorthands
```

### Comparisons

You can use following operators for comparison: 
* `==` is equal to
* `<` is less than
* `>` is greater than
* `<=` is less or equal to
* `>=` is greater or equal to 

Example:

```
int a = 3;
int b = 2; 
int c = 3;
int d = 5;

// are they equal ?
if (a == b) {
  a++;
}
```

### Logicatl operators

Below are logical operators:

`!=` is not equal to
`||` one or both are true
`&&` both are true

Example:

```
int a = 2;
int b = 5;

if (a == b && a == 2) {
  printf("both are true\n");
}

if (a == b || a == 2) {
  printf("one or both are true\n");
}

if (a != b) {
  printf("not equal\n");
}
```

### Ternary operators

Below is common scheme"

```
condition ? do something : do something else;
```

The above example is exactly the same as:

```
if (condition) {
  // do something
} else {
  // do something else
}
```

## Loops

The `while` loop:

```
while (condition) {
  // do something
}
```

Usecase:

```
int guess;

printf("I’m thinking of a number in the range 0 - 5.\n");
printf("Try to guess it: ");
scanf("%d", &guess);

while (guess != 0) {
  printf("Wrong guess, try again: ");
  scanf("%d", &guess);
}
```

The `do-while` loop:

```
do {
  // do something
} while(condition);
```

This loop is most often used when a program wants to do something at least once before checking the condition

The `for` loop:

```
for (int i = 0; i < 10; i++ ) {
  printf("i is equal to: %d\n", i);
}
```

The `for` loop contains three parts:

* initialication of a counter
* condition
* counter adjustment

### Breaking out

The keyword `break` allows us to, quite literally, “break” out of a loop and stop it from running any more times. 


Use case:

```
int tries = 0;

while (tries < 5) {
  scanf("%d", &guess);
 
  if (guess == 8) {
    break;
  }
 
  printf("Wrong guess, try again: ");
  tries++;
}
```

### Continuing

In a loop, if a `continue` is ever reached, it will immediately skip the rest of the statements inside the loop body
and "continue" into the next iteration.

Example:

```
for (int i = 0; i < 10; i++) {
  if (i % 2 == 0) {
    continue;
  }
  printf("%d is odd\n", i);
|
```

### Interesting notes about loops

1. All `for` loops can be rewritten as `while` loops.
2. Most `while` loops can be rewritten as `for` loops.
3. `for` loops are appropriate when looping a predetermined number of times
4. `break` and `continue` can be used in all loops.



## Errors in Casting


* Compile-time errors: Errors found by the compiler. We can further classify compile-time errors based on which language rules they violate, for example:
  * Syntax errors
```
int x = 1      // Error: missing a terminating semicolon
Int x = 1; 	   // Error: Int is not a types
printf("Error"; // Error: missing closing parenthesis
```	
  * Semantic errors
```
a + b = c;      // Error: value required as left operand of assignment

int i;
i = i + 2;      // Error: use of un-initialised variable
```


* Link-time errors: Errors found by the linker when it is trying to combine object files into an executable program
```
#include <stdio.h>

void Main() 				// In function `_start': (.text+0x18): undefined reference to `main'
{
  printf("Hello worlds");
}
```

* Run-time errors: Errors found by checks in a running program.
```
#include <stdio.h>

int main()
{
  float n = 10;
  float div;

  div = n / 0; // run-time error: Division by zero

  printf("div: %f\n", div);
  return 0;
}
```

* Logic errors: Errors found by the programmer looking for the causes of errorneous results.
   	
	
## Arrays

An array is a grouping of variables of the same type into contiguous blocks
of memory. This data structure is especially useful in applications when there are many
variables of the same type that are related to each other.


Use case:

```
int main() {
  int number1 = 1;
  int number2 = 2;
  int number3 = 3;
  int number4 = 4;
}
```

versus code using arrays:

```
int main() {
 int numbers[4] = {1, 2, 3, 4};
}
```

### Uninitialized array

```
int u_arr[4];
```

### Initialized array

```
int arr[] = {1, 2, 3, 4, 5};
```

### Modifying an array

Note that we use index value to access the specific element. Index starts from 0. So index 0 means that we access to 1st element.

```
int odds[] = {1, 3, 4, 6, 9, 11};

odds[2] = 5;  // fixing the number 4 to correct value -> 5
odds[3] = 7;  // fixing the number 6 to correct value -> 7
```

### Length of an array

Using `sizeof`

```
#include<stdio.h>

int main() {
  int arr[] = {3, 8, 4, 0, 9}; 
  int len = sizeof(arr)/sizeof(int); // Assign size of array to variable len
  printf("%i", len);
}
```


### Multidimensional arrays

Example:

```
int matrix[3][3];  // uninitialized
int matrix2[][4] = {{14, 10, 6, 4}, {3, 7, 18, 11}, {13, 9, 5, 17}, {19, 12, 2, 1}}; // initialized

// get row count
int rowDimension = sizeof(matrix) / sizeof(matrix[0]);
int columnDimension = sizeof(matrix[0]) / sizeof(int);
```

Refer to `multidim_array.c` source file.


## Strings

```
// creating string using initialized array
char greeting[] = {'H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '\0'};

// the '\0' is null terminating character. It indicates where the string ends.

// second way to create string is more simple
char str[] = "Hello World";

### Length of string

Use `strlen()` function to get the length (Do not forget to include <string.h>
Note that `strlen()` does not account for the null terminating character.

### Concatenating Strings

`strcat()` function

```
#include <stdio.h>
#include <string.h> // Don't forget to include this!

int main() {
  char s1[] = "abcd";
  char s2[] = "efgh";
  strcat(s1, s2);
  printf("%s", s1); 
  // Output will be "abcdefgh"
}
```

### Copying Strings

Use function `strcpy(dst, src)`.

Example:

```
#include<stdio.h>
#include<string.h>
 
int main() {    
  char s1[] = "Hello";
  char s2[6]; // Empty string
  strcpy(s2, s1);    
  printf("%s", s2); // Prints: Hello
}
```

## Memory in C

### Pointers

In C, a byte of memory can be accessed using a *pointer*.
A pointer containing the address of a variable is said to "point" to that variable.

```
int *ptr; // Pointer to an int

printf("%p", ptr); // %p is type pointer
```

Above program will output a hexadecimal integer that represents the address in memory that is storing a variable of type `int`.
This number will be different every time the program is executed.

### Reference Operator

Since pointers are used to store the memory address of a variable, we need to obtain this address firts.
This is done by using the `reference operator (&)`. The syntax for this is:

```
&variableName;
```

Example:
```
int x = 1;
printf("%p", &x);
```

### The Dereference Operator

If we want to access to data that are stored on the address we will use:

```
*pointerName;
```

Example:

```
int x = 1;
int p_x = &x;

printf("x: %d\n", x);
printf("*p_x: %d\n", *p_x);
```

### Pointer Arithmetic

The only arithmetic operations allowed for pointers are addition and subtraction.

Examples:

```
pointer = pointer + n;
pointer += n;
pointer++;
```

### Pointers and Arrays

```
int numbers[] = {1, 2, 3, 5, 8, 13};
int *p_n = &numbers[0]; // points to first element of array
int n_length = sizeof(numbers) / sizeof(int);

for (int i = 0; i < n_length; i++) {
  printf("%i\n", *p_n);
  p_n++;
}
```

### Memory Allocation

Program memory is organized into two main cateforeis:
* stack
  - A stack is a section of memory that is highly ordered and data stored on the stack
    are only available within a certain scope. 
	When you create a variable in the usual way, you are 
    statically allocating memory and it is stored on the stack. That memory will be released 
	by program when the variable is no longer needed.
* heap
  - Heap is not as ordered as a stack. Heap allows you to reserve as much available memory as you want
    and that memory will remain available until you explicitly release it. This is known as `dynamically allocating memory`.
	Forgetting to release dynamically allocated memory will cause a `memory-leak` leading to poor program performance.
	
  - C provides four special functions for you to dynamically allocate (and release) memory, provided it is available. They are:
    * `malloc()`
    * `calloc()`
    * `realloc()`
    * `free()`
  These functions are stored int the **stdlib** library.	
	
	
## Functions

For more details refer to functions.c	
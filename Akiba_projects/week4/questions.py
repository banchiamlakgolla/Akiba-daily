# Question 1: Mutable and Immutable Objects
'''
 Mutable and Immutable Objects
Explain the difference between mutable and immutable objects in Python.

   Mutable objects: objects whose content can be changed after they are created, without creating a new object.
       eg.list, dict, and set.
      -items can be modified directly. eg. my_list[0] = 10 is valid
   Immutable objects: objects whose contents cannot be changed after they are created.(for different value, we must create a new object)
      eg. str (string), int (integer), float, and tuple.
      -changing the values requires a new object. eg. my_string[0] = "H" raises an error.
Write a Python program that demonstrates the difference between modifying a list and modifying a string. Explain the output.
'''

list_items = [2, 3, 4, 5]

print("List before modification: ", list_items)

list_items[0] = 1
print("List after modification: ", list_items)

string_item = "Selam"

print("String before modification: ", string_item)

try: 
    string_item[0] = "L"
except TypeError as error:
    print("Error:", error)
    
# creating a new object instead
string_item = "L" + string_item[1:]
print("New string: ", string_item)

# Expected output
'''
List before modification:  [2, 3, 4, 5]
List after modification:  [1, 3, 4, 5]
String before modification: Selam
Error: 'str' object does not support item assignment
New string: Lelam

'''

# explanation of the output
'''
A. Modifying the list
list_items = [2, 3, 4, 5]
list_items[0] = 1
The list initially contains [2, 3, 4, 5].
list_items[0] = 1 changes the first element from 2 to 1.
This operation succeeds because lists are mutable.

The resulting list is [1, 3, 4, 5].

B. Modifying the string
string_item = "Selam"
string_item[0] = "L"
- The string initially contains "Selam".
- string_item[0] refers to the first character, S.
- Python does not allow assigning a new character directly to an existing string position because strings are immutable.
- Therefore, Python raises a TypeError.

Creating a new string
string_item = "L" + string_item[1:]
string_item[1:] extracts the characters from index 1 to the end, producing "elam".
"L" + "elam" creates the new string "Lelam".
The variable string_item is then assigned to this new string.

'''
# Question 2: References and Object Identity
a = [10, 20, 30]
b = a
c = [10, 20, 30]

print(a is b)
print(a is c)
print(a == c)

'''
*What is the output?*
True
False
True

*Explain the difference between is and ==.*
- is: checks whether two references points to the same object a is b ->True(same object)
- ==: checks whether two objects have equal value. a == c -> True(same value)

*Why do a and c have the same values but different identities?*
- Because python creates a new list each time we write a separate list literals. 
They are two separately created list objects. They contain the same values, but they occupy distinct object identities in Python.

'''

# Question 3: Shared References and Side Effects
numbers = [1, 2, 3]
values = numbers

values.append(4)

print(numbers)
print(values)

'''
* Predict the output.*
[1, 2, 3, 4]
[1, 2, 3, 4], both display same list

* Explain why modifying values also affects numbers.*
The statement values = numbers makes both variables refer to the same list object. 
Since lists are mutable, calling values.append(4) changes the shared list, which also affects what we see through numbers.

* Rewrite the code so that modifying values does not change numbers.*
'''
# Use values = numbers.copy() to create a separate list. Then modifying values will not change numbers
values = numbers.copy()

values.append(4)

print(numbers)  # [1, 2, 3]
print(values)  # [1, 2, 3, 4]

# Question 4: Function Arguments and Mutability


def update_list(items):
    items.append(100)


scores = [50, 60, 70]
update_list(scores)

print(scores)

'''
* What is the output?*
[50, 60, 70, 100], 100 is added to the original list.

* Explain why the original list changes after the function call.*
The parameter items refers to the same list object as scores. 
Since lists are mutable, items.append(100) modifies the original list, so the change is visible after the function call.

* Modify the function so that it creates and returns a new list without changing the original list.*
'''


def create_updated_list(items):
    new_list = items.copy()
    new_list.append(100)
    return new_list


scores = [50, 60, 70]

updated_scores = create_updated_list(scores)

print("Original list:", scores)
print("New list:", updated_scores)

# Question 5: Memory Management and Garbage Collection
'''
* Explain how Python manages objects in memory and how garbage collection works.*
When we create an object in Python, Python stores it in memory and allows us to access it through references. 
For example, numbers = [10, 20, 30] creates a list object, and the variable numbers refers to that object.
eg. numbers = [10, 20, 30]
Python creates a list object containing 10, 20, and 30. The variable numbers refers to that object.
Python manages memory automatically. We usually don't need to manually allocate and free memory as we might in some other programming languages.

-Memory management: How Python allocates, uses, and releases memory for objects.
-Garbage collection: How Python helps identify and clean up objects that are no longer needed, including certain groups of objects that reference one another.
In CPython, reference counting tracks how many references point to an object. 
When the reference count reaches zero, the object can generally be reclaimed. 
Python's garbage collector also detects certain unreachable groups of objects that refer to one another and helps clean them up.

* Write a Python program that creates a list, assigns it to another variable, and then removes one reference using del.*
-* What happens when del is used?*
- It removes a name or reference, or deletes a specified item or attribute, depending on how it is used. 
- It does not necessarily destroy the referenced object.
* Does deleting one variable always destroy the object?*
- No. If another variable still refers to the same object, that object can remain accessible.
* What happens when an object is no longer referenced?*
- It becomes eligible for memory cleanup. 
- Python manages this automatically through its memory-management mechanisms, including reference counting and garbage collection.

'''
numbers = [10, 20, 30]

# Assign the same list to another variable
values = numbers

print("Before deletion:")
print("numbers:", numbers)
print("values:", values)

# Delete one reference
# The program still works after del numbers. 
# The list is accessible through values.
del numbers

print("\nAfter deletion:")
print("values:", values)

# Akiba Technologies — Week 4 Python Assignment

## Mutability, References, and Memory Model in Python

**Student Name:** Banchiamlak Golla

**Assignment:** Week 4 — Mutability, References, and Memory Model in Python

**Program:** Akiba Technologies Software Engineering & Backend Bootcamp

---

## 1. Introduction

This assignment explores mutability, references, object identity, function arguments, memory management, and garbage collection in Python. It includes practical examples to demonstrate how Python handles mutable and immutable objects, how variables can refer to the same object, and how changes to objects affect different references.

The assignment also includes a practical mini-project called **Student Marks Manager**, which demonstrates shared references, copying lists, and object identity using student marks.

## 2. Question 1: Mutable and Immutable Objects

### Explanation

**Mutable objects** are objects whose contents can be changed after they are created without creating a new object. Examples include lists, dictionaries, and sets. For example, `my_list[0] = 10` changes the first element of a list.

**Immutable objects** are objects whose contents cannot be changed after they are created. Examples include strings, integers, floats, and tuples. For example, assigning a new character to `my_string[0]` raises a `TypeError` because strings are immutable.

### Program

The following program demonstrates the difference between modifying a list and modifying a string.

```python
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

# Creating a new string instead
string_item = "L" + string_item[1:]
print("New string: ", string_item)
```

### Expected Output

```text
List before modification:  [2, 3, 4, 5]
List after modification:  [1, 3, 4, 5]
String before modification:  Selam
Error: 'str' object does not support item assignment
New string:  Lelam
```

### Explanation of the Output

**A. Modifying the list**

The list initially contains `[2, 3, 4, 5]`. The statement `list_items[0] = 1` changes the first element from `2` to `1`. This operation succeeds because lists are mutable.

The resulting list is `[1, 3, 4, 5]`.

**B. Modifying the string**

The string initially contains `"Selam"`. The statement `string_item[0] = "L"` attempts to replace its first character, `S`, with `L`. However, strings are immutable, so Python raises a `TypeError`.

**C. Creating a new string**

The expression `string_item[1:]` extracts the characters after the first character, producing `"elam"`. Combining `"L"` with `"elam"` creates `"Lelam"`. The variable `string_item` is then assigned to the new string.

This demonstrates that a list can be modified directly, while a string cannot be changed in place.

## 3. Question 2: References and Object Identity

### Program

```python
a = [10, 20, 30]
b = a
c = [10, 20, 30]

print(a is b)
print(a is c)
print(a == c)
```

### Expected Output

```text
True
False
True
```

### Explanation

- **`is` operator:** Checks whether two variables refer to the same object.
- **`==` operator:** Checks whether two objects have equal values.

The statement `b = a` makes `b` refer to the same list object as `a`. Therefore, `a is b` returns `True`.

The statement `c = [10, 20, 30]` creates a separate list object with the same contents. Therefore, `a is c` returns `False`, while `a == c` returns `True`.

Although `a` and `c` contain the same values, they are two distinct list objects. Their values are equal, but their identities are different.

## 4. Question 3: Shared References and Side Effects

### Program

```python
numbers = [1, 2, 3]
values = numbers

values.append(4)

print(numbers)
print(values)
```

### Expected Output

```text
[1, 2, 3, 4]
[1, 2, 3, 4]
```

### Explanation

The statement `values = numbers` makes both variables refer to the same list object. When `values.append(4)` adds `4` to the list, the change is visible through both variables.

This is called a **shared reference**. Since lists are mutable, modifying the shared list affects every variable that refers to it.

### Creating an Independent Copy

To prevent changes to `values` from affecting `numbers`, we can use the `copy()` method.

```python
numbers = [1, 2, 3]
values = numbers.copy()

values.append(4)

print(numbers)
print(values)
```

### Expected Output

```text
[1, 2, 3]
[1, 2, 3, 4]
```

### Explanation

The `copy()` method creates a separate, shallow copy of the list. Therefore, `numbers` and `values` refer to different list objects. Appending `4` to `values` does not change `numbers`.

This demonstrates how copying a list can prevent unintended side effects when working with mutable objects.

## 5. Question 4: Function Arguments and Mutability

### Program: Modifying the Original List

```python
def update_list(items):
    items.append(100)


scores = [50, 60, 70]
update_list(scores)

print(scores)
```

### Expected Output

```text
[50, 60, 70, 100]
```

### Explanation

When `scores` is passed to `update_list()`, the parameter `items` refers to the same list object as `scores`. The statement `items.append(100)` modifies that list.

As a result, the original list changes, and `scores` contains `[50, 60, 70, 100]` after the function call.

### Creating and Returning a New List

To avoid modifying the original list, we can copy the list inside the function and return the modified copy.

```python
def create_updated_list(items):
    new_list = items.copy()
    new_list.append(100)
    return new_list


scores = [50, 60, 70]

updated_scores = create_updated_list(scores)

print("Original list:", scores)
print("New list:", updated_scores)
```

### Expected Output

```text
Original list: [50, 60, 70]
New list: [50, 60, 70, 100]
```

### Explanation

The function creates a separate copy using `items.copy()`. It adds `100` to the copy and returns it. Therefore, the original `scores` list remains unchanged, while `updated_scores` contains the new list.

This demonstrates how copying mutable objects inside a function can help avoid unintended changes to the original data.

## 6. Question 5: Memory Management and Garbage Collection

### Explanation

Python manages memory automatically. When an object is created, Python allocates memory for it and allows the program to access it through references.

For example:

```python
numbers = [10, 20, 30]
```

Python creates a list object containing `10`, `20`, and `30`, and the variable `numbers` refers to that object.

**Memory management** is the process of allocating, using, and releasing memory for objects.

**Garbage collection** helps Python identify and clean up objects that are no longer reachable or needed, including certain groups of objects that refer to one another.

In CPython, reference counting tracks how many references point to an object. When the reference count reaches zero, the object can generally be reclaimed. Python's garbage collector also helps detect and collect unreachable groups of objects that refer to one another.

### Program: Deleting a Reference

```python
numbers = [10, 20, 30]

# Assign the same list to another variable
values = numbers

print("Before deletion:")
print("numbers:", numbers)
print("values:", values)

# Delete one reference
del numbers

print("\nAfter deletion:")
print("values:", values)
```

### Expected Output

```text
Before deletion:
numbers: [10, 20, 30]
values: [10, 20, 30]

After deletion:
values: [10, 20, 30]
```

### Explanation

**1. What happens when `del` is used?**

The statement `del numbers` removes the name `numbers` from the current scope. It does not necessarily destroy the object that the variable referred to.

**2. Does deleting one variable always destroy the object?**

No. In this example, `values` still refers to the same list object. Therefore, the list remains accessible through `values`.

**3. What happens when an object is no longer referenced?**

When an object is no longer reachable, it becomes eligible for memory cleanup. Python manages this process automatically. The exact timing of memory reclamation depends on the Python implementation.

## 7. Practical Mini-Project: Student Marks Manager

### Project Objective

The objective of this project is to develop a simple Python program that demonstrates mutability, shared references, object identity, and copying lists using student marks.

### Program

The following code is implemented in `student_marks_manager.py`.

```python
# Creates a list containing five student marks
original_mark = [75, 80, 65, 90, 85]

# Assigns the original list to another variable
shared_ref = original_mark

# Creates an independent copy of the original list
copied_mark = original_mark.copy()

# Adds a new mark to the copied list
copied_mark.append(95)

print("Original marks:", original_mark)
print("Shared reference:", shared_ref)
print("Copied marks:", copied_mark)

print("\nOriginal and shared reference are identical:",
      original_mark is shared_ref)

print("Original and copied lists have equal values:",
      original_mark == copied_mark)

print("Original and copied lists are identical:",
      original_mark is copied_mark)
```

### Expected Output

```text
Original marks: [75, 80, 65, 90, 85]
Shared reference: [75, 80, 65, 90, 85]
Copied marks: [75, 80, 65, 90, 85, 95]

Original and shared reference are identical: True
Original and copied lists have equal values: False
Original and copied lists are identical: False
```

### Project Explanation

1. **Original marks:** The `original_mark` list stores five student marks.
2. **Shared reference:** The statement `shared_ref = original_mark` makes both variables refer to the same list object.
3. **Independent copy:** The `copy()` method creates a separate list object.
4. **Adding a mark:** The statement `copied_mark.append(95)` adds a new mark to the copied list without changing the original list.
5. **Identity comparison:** `original_mark is shared_ref` returns `True` because both variables refer to the same object.
6. **Equality comparison:** `original_mark == copied_mark` returns `False` because the lists contain different values.
7. **Copy identity:** `original_mark is copied_mark` returns `False` because the original and copied lists are separate objects.

### Project Reflection Questions

**1. Why does modifying a shared reference affect the original list?**

When we assign `shared_ref = original_mark`, both variables refer to the same list object. Therefore, modifying the list through either variable changes the same object, and the change is visible through both variables.

**2. Why does modifying the copied list not affect the original list?**

The `copy()` method creates a separate, shallow copy of the original list. The copied list is a different object, so adding a new mark to it does not change the original list.

**3. What is the difference between equality and identity in Python?**

Equality, checked using `==`, compares the values of two objects. Identity, checked using `is`, checks whether two variables refer to the exact same object. Two separate lists can have equal values but different identities.

## 8. General Project Reflection

Through this assignment, I learned how Python handles mutable and immutable objects, references, object identity, function arguments, and memory management.

I understood that assigning one variable to another does not necessarily create a new object. For mutable objects such as lists, multiple variables can refer to the same object, so changes made through one variable may be visible through another.

I also learned the difference between `is` and `==`, how to use `copy()` to create a separate list, and how to prevent a function from modifying an original list. Finally, I learned that Python manages memory automatically and that deleting a variable does not always destroy the object it referred to.

These concepts will help me write clearer code and avoid unintended side effects when developing Python applications.

## 9. Project Structure

The assignment repository contains the following files:

```text
week-4-python-task/
├── README.md
├── questions.py
└── student_marks_manager.py
```

- **`README.md`** — Contains the assignment title, theoretical explanations, expected outputs, project reflection, and instructions for running the programs.
- **`questions.py`** — Contains the Python code solutions for Questions 1–5.
- **`student_marks_manager.py`** — Contains the complete Student Marks Manager mini-project.

## 10. How to Run the Programs

### Prerequisites

- Python 3 installed on your computer.
- A terminal or command prompt.

### Run the Questions

Open a terminal in the project folder and execute:

```bash
python questions.py
```

### Run the Student Marks Manager

Execute:

```bash
python student_marks_manager.py
```

If your computer uses the `py` command instead of `python`, you can run:

```bash
py questions.py
py student_marks_manager.py
```
---

## 11. Submission Checklist

- [X] All five questions answered.
- [X] Mini-project completed.
- [x] `README.md` included.
- [x] `questions.py` included.
- [x] `student_marks_manager.py` included.
- [x] Both Python programs tested successfully.
- [x] Changes committed and pushed to GitHub.
- [x] Repository link submitted to the instructor.

**GitHub Repository:** `https://github.com/banchiamlakgolla/Akiba-daily/tree/main/Akiba_projects/week4`

**Submission Method:** GitHub repository link


---

**Akiba Technologies**

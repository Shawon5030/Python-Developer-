### Explanation of the First 100 Lines of Python Code - In English

This document thoroughly explains the first 100 basic lines of Python code for beginners. Each section below expands on a block of 10 lines, detailing how and why each line works, so you understand both the syntax and the logic.

---

#### Lines 1-10: Variables and Data Types

```python
x = 10
y = 5.5
name = "Shawon"
is_active = True
a, b, c = 1, 2, 3
PI = 3.1416
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_set = {1, 2, 3}
my_dict = {"name": "Shawon", "age": 22}
```

* **x = 10**: Assigns the integer 10 to the variable `x`.
* **y = 5.5**: Assigns the float 5.5 to the variable `y`.
* **name = "Shawon"**: A string value assigned to a variable.
* **is\_active = True**: A boolean value.
* **a, b, c = 1, 2, 3**: Assigns multiple variables at once.
* **PI = 3.1416**: Constants can be written in uppercase.
* **my\_list**: A mutable list that can store multiple values.
* **my\_tuple**: An immutable version of a list.
* **my\_set**: An unordered collection of unique elements.
* **my\_dict**: Key-value pair mapping, a dictionary.

These represent Python's most fundamental data types.

---

#### Lines 11-20: Input and Output

```python
print("Hello, World!")
name = input("Enter your name: ")
print("Welcome,", name)
age = int(input("Enter your age: "))
print("In 5 years, you'll be", age + 5)
print("Name length:", len(name))
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Starts with S?", name.startswith("S"))
print("Ends with n?", name.endswith("n"))
```

* **print()**: Displays output.
* **input()**: Takes string input from user.
* **int(input())**: Converts input to integer.
* **len()**: Returns the number of characters.
* **str.upper()/lower()**: Converts string to upper/lowercase.
* **startswith()/endswith()**: Checks string beginning or end.

Great for understanding user interaction and string manipulation.

---

#### Lines 21-30: Conditional Statements

```python
num = 7
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

* **if, elif, else**: Python's conditional blocks.
* **Indentation is required**.
* Makes decisions based on conditions.

---

#### Lines 31-40: Loops

```python
for i in range(5):
    print("Loop:", i)

i = 0
while i < 5:
    print("While loop:", i)
    i += 1
```

* **for loop**: Iterates over a range of numbers.
* **while loop**: Repeats as long as condition is true.
* **range()**: Generates a sequence from 0 to 4.

---

#### Lines 41-50: Functions

```python
def greet(name):
    print("Hello,", name)

greet("Shawon")

def add(a, b):
    return a + b

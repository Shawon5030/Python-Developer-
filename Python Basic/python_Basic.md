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

print("Sum:", add(3, 4))
```

* **def**: Declares a function.
* **return**: Sends back the result.
* **Functions**: Help organize code.

---

#### Lines 51-60: List Operations

```python
nums = [1, 2, 3, 4]
nums.append(5)
nums.remove(2)
nums.insert(1, 99)
print("List:", nums)
print("Sorted:", sorted(nums))
print("Sum:", sum(nums))
print("Max:", max(nums))
print("Min:", min(nums))
print("Slice:", nums[1:3])
```

* **append()**: Adds an item.
* **remove()**: Removes specific value.
* **insert(index, value)**: Adds item at index.
* **sorted()**, **sum()**, **max()**, **min()**: List utilities.
* **slicing**: Accessing parts of the list.

---

#### Lines 61-70: Dictionary Usage

```python
person = {"name": "Alice", "age": 30}
print("Name:", person["name"])
person["city"] = "Dhaka"
for key, value in person.items():
    print(key, "=>", value)
print("Keys:", list(person.keys()))
print("Values:", list(person.values()))
```

* **Dictionaries** store data in key-value format.
* **Access** values using keys.
* **Looping** through dictionary using `.items()`.

---

#### Lines 71-80: String Formatting

```python
name = "Shawon"
age = 22
print(f"My name is {name} and I am {age} years old.")
print("My name is {} and I am {} years old.".format(name, age))
print("%s is %d years old." % (name, age))
```

* **f-strings** (Python 3.6+): Cleaner formatting.
* **format()**: Older method.
* **%s %d**: Even older C-style formatting.

---

#### Lines 81-90: List Comprehension & Built-ins

```python
squares = [x*x for x in range(5)]
print("Squares:", squares)
even = list(filter(lambda x: x % 2 == 0, range(10)))
print("Even numbers:", even)
double = list(map(lambda x: x * 2, range(5)))
print("Doubled:", double)
print("Any true?", any([False, True, False]))
print("All true?", all([True, True, True]))
```

* **List comprehensions**: Compact loop-based list creation.
* **lambda**: Anonymous function.
* **filter/map**: Functional programming tools.
* **any() / all()**: Boolean evaluators.

---

#### Lines 91-100: File Handling & Exception

```python
try:
    with open("sample.txt", "w") as f:
        f.write("Hello file!\n")
        f.write("Second line\n")

    with open("sample.txt", "r") as f:
        content = f.read()
        print("File Content:\n", content)
except FileNotFoundError:

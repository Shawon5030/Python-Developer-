# 1-10: Variables and Data Types
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

# 11-20: Basic Input and Output
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

# 21-30: Conditional Statements
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

# 31-40: Loops
for i in range(5):
    print("Loop:", i)

i = 0
while i < 5:
    print("While loop:", i)
    i += 1

# 41-50: Functions
def greet(name):
    print("Hello,", name)

greet("Shawon")

def add(a, b):
    return a + b

print("Sum:", add(3, 4))

# 51-60: List Operations
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

# 61-70: Dictionary Usage
person = {"name": "Alice", "age": 30}
print("Name:", person["name"])
person["city"] = "Dhaka"
for key, value in person.items():
    print(key, "=>", value)
print("Keys:", list(person.keys()))
print("Values:", list(person.values()))

# 71-80: String Formatting
name = "Shawon"
age = 22
print(f"My name is {name} and I am {age} years old.")
print("My name is {} and I am {} years old.".format(name, age))
print("%s is %d years old." % (name, age))

# 81-90: List Comprehension & Built-ins
squares = [x*x for x in range(5)]
print("Squares:", squares)
even = list(filter(lambda x: x % 2 == 0, range(10)))
print("Even numbers:", even)
double = list(map(lambda x: x * 2, range(5)))
print("Doubled:", double)
print("Any true?", any([False, True, False]))
print("All true?", all([True, True, True]))

# 91-100: File Handling & Exception
try:
    with open("sample.txt", "w") as f:
        f.write("Hello file!\n")
        f.write("Second line\n")

    with open("sample.txt", "r") as f:
        content = f.read()
        print("File Content:\n", content)
except FileNotFoundError:
    print("File not found!")
except Exception as e:
    print("Error:", e)
